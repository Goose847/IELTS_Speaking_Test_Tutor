import sounddevice as sd
import numpy as np
import wave
from openai import OpenAI
import time
from scipy.io import wavfile
from utils import answer_question, clean_directory, flush_input
API_KEY = 'INSERT API KEY HERE'
def test():
    max_questions = 5

    test_prompt = "You are a helpful assistant tutor for a company which is an online language learning platform for individuals to learn and get IELTS certified in English. Your job is to help a student prepare for an IELTS spoken test. You will ask questions about the student such as what their mourning routine is like, what their hobbies are, what sports they play, and whether they're studying or working. Ask basic follow up questions to their responses but no more than two per question. At the end of the test, I will append a message to the user input that says:  ----- THIS IS THE LAST QUESTION. PROVIDE FEEDBACK ON THE USER'S PERFORMANCE -----  at which point you must produce a score out of 10 according to the IELTS criteria: - Fluency & Coherence: Timing, pauses, and logical flow. - Lexical Resource: Vocabulary usage and suggestions. - Grammatical Range & Accuracy: Sentence structure and grammar. Provide detailed feedback alongside this score.In the last question, instead of providing a question, use this response for feedback."
    Q1 = "Greet the user, encourage them to relax and enjoy the practise and ask them to introduce themselves. Do not respond directly to this query"


    chat_history = [
        {
            "role": "system", 
            "content": test_prompt
         },
        {
            "role": "user",
            "content": Q1
        }
    ]
    client = OpenAI(api_key=API_KEY)

    # Get welcome message and first from GPT
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
        )
    assistant = completion.choices[0].message.content
        
    chat_history.append({"role":"assistant",
                         "content":assistant})
    print("-----------------------------beginning of test-----------------------------------")
    print("Tutor: " + assistant)
    for i in range(1, max_questions, 1):
        print()
        time.sleep(1)
        user = answer_question(i)
        print("User:" + user)
        if max_questions - i == 1:
            user_meta = "----- THIS IS THE LAST QUESTION. PROVIDE FEEDBACK ON THE USER'S PERFORMANCE -----"
        else:
            user_meta = "----- THIS IS NOT THE LAST QUESTION. DO NOT PROVIDE FEEDBACK UNTIL INSTRUCTED.-----"
        user += user_meta
        
        print()
        chat_history.append({"role":"user",
                             "content":user})
        
        # Get question from GPT
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat_history
            )
        assistant = completion.choices[0].message.content
        print("Tutor: " + assistant)
        
        chat_history.append({"role":"assistant",
                             "content":assistant})


def welcome():
    print("Welcome to the IELTS Speaking Test Tutor.")
    print("Please select a mode:")
    print("1. Test Mode")
    print("2. Practise Mode")
    print("3. Exit")

def practise():
    round = True # Used to detirmine whether or not to do another practice round
    question_number = 0
    commence = ""
    practice_prompt = "You are a helpful assistant tutor for a company  which is an online language learning platform for individuals to learn and get IELTS certified in English. Your job is to help a student prepare for an IELTS spoken test. Specifically you will be engaging in a practise quick round with the student. You will ask them a question about themselves, their interests, their routine, hobbies, work or studies, why they're learning english, and any other relevant content. The student will record their response which will be transcribed by OpenAI's whisper model. This will be fed in as a query after which point you must evaluate them on the following criteria: : - Fluency & Coherence: Timing, pauses, and logical flow. - Lexical Resource: Vocabulary usage and suggestions. - Grammatical Range & Accuracy: Sentence structure and grammar. Following this, the user will be prompted to decide whether to do another question with you or to quit to the main menu of the program. If they choose to do a new question the text ---NOT THE USER. PLEASE ASK A NEW QUESTION--- will be given as input. Do not respond to this message. Just ask a new or followup question directly."
    Q1 = "Greet the user, encourage them to relax and enjoy the practise and ask a question for them to respond to. Do not respond directly to this query"

    chat_history = [
        {
            "role": "system", 
            "content": practice_prompt
         },
        {
            "role": "user",
            "content": Q1
        }
    ]
    client = OpenAI(api_key=API_KEY)
    
    while round:
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
        )
    
        assistant = completion.choices[0].message.content
        
        chat_history.append({"role":"assistant",
                         "content":assistant})
        print("Tutor: " + assistant)

        user = answer_question(question_number)
        print("User:" + user)
        print()
        chat_history.append({"role":"user",
                             "content":user})
        
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
        )
        assistant = completion.choices[0].message.content
        print("Tutor: " + assistant)
        print()

        while True:
            flush_input()
            commence = input("Do you want to continue? (Y/N) ")
            if commence.upper() == "N":
                round = False
                break
            elif commence.upper() == "Y":
                question_number += 1
                chat_history.append({"role":"user",
                             "content":"---NOT THE USER. PLEASE ASK A NEW QUESTION--- "})
                break
            else:
                print("Invalid choice. Please try again.")

        
def main():
    clean_directory()
    welcome()
    mode = ""
    while mode not in ["1", "2", "3"]:
        mode = input("Enter your choice: ")
        if mode == "1":
            test()
            print("Test completed.")
            print()
            welcome()
            mode = ""
        elif mode == "2":
            practise()
            print("Practise completed")
            print()
            welcome()
            mode = ""
        elif mode == "3":
            print("Exiting...")
            clean_directory()
            exit()
        else:
            print("Invalid choice. Please try again.")
        flush_input()

if __name__ == "__main__":
    main()