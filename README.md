# IELTS Speaking Test Tutor

## Overview

The IELTS Speaking Test Tutor is a Python-based interactive program designed to help users prepare for the IELTS speaking test. It simulates both test and practice scenarios, providing real-time feedback on responses based on IELTS scoring criteria. This project uses the OpenAI API for generating prompts, evaluating responses, and OpenAI Whisper for transcribing recorded audio.

## Features

 - Test Mode: Simulates a structured IELTS speaking test with scoring and feedback at the end.
 - Practice Mode: Allows users to practice responses to IELTS-style questions with iterative feedback.
 - Audio Recording: Records user responses using a spacebar toggle and saves them as .wav files.
 - Automatic Transcription: Transcribes user recordings using OpenAI Whisper.
 - Feedback Evaluation: Scores responses based on:
    - Fluency & Coherence
    - Lexical Resource
    - Grammatical Range & Accuracy
- Directory Cleanup: Deletes temporary `.wav` files to maintain a clean working directory.


## Requirements

 - Python 3.8 or higher
 - Required Python libraries:
 - sounddevice
 - numpy
 - wave
 - scipy
 - pynput
 - openai
 - termios (for Unix-based systems)
Install dependencies using:

```pip install sounddevice numpy scipy pynput openai```

## Setup

 1. Obtain an OpenAI API key:
    - Sign up at OpenAI.
    - Generate an API key and replace the placeholder in both main.py and utils.py with your key.
 2. Clone the repository:

```git clone https://github.com/goose847/IELTS_Speaking_Test_Tutor```

```cd IELTS_Speaking_Test_Tutor```

 3. Run the program:
```python main.py```

## File Structure

`main.py`: The main script that orchestrates the user interface, test, and practice modes.
`utils.py`: Contains helper functions for audio recording, playback, transcription, and file cleanup.

## How to Use

 1. Run the program using:
```python main.py```
 2. Follow the prompts to choose between:
    - Test Mode: Complete a full test session and receive feedback at the end.
    - Practice Mode: Practice individual questions and decide whether to continue or quit.
 3. Use the spacebar to start/stop audio recording when prompted.
 4. At the end of the session, the program will:
    - Provide detailed feedback (Test Mode).
    - Allow iterative practice (Practice Mode).

## Important Notes

 - API Key Security: Replace hardcoded API keys with environment variables for enhanced security.
 - Platform Dependency: The termios module is used for flushing input, which may not work on Windows.

## Future Enhancements

 - Add support for Windows systems.
 - Improve feedback with more nuanced scoring.
 - Implement a graphical user interface (GUI).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Powered by OpenAI GPT and Whisper models.
Special thanks to the Python community for their libraries and resources.
