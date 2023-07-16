# Typing Speed Test

# This is a simple typing speed test application implemented in Python using the tkinter library. 
# The application presents random words for the user to type and calculates their typing speed.

# Prerequisites

# Make sure you have the following requirements installed:
# - Python 3.x
# - tkinter library
# - requests library

# Getting Started

# 1. Clone the repository to your local machine:
#    git clone https://github.com/your-username/typing-speed-test.git

# 2. Change into the project directory:
#    cd typing-speed-test

# 3. Install the required dependencies:
#    pip install -r requirements.txt

# 4. Run the application:
#    python main.py

# How to Use

# 1. Once you run the application, a window will open with a timer, a word to type, and an input box.

# 2. Start typing the word displayed in the input box.

# 3. If you type the word correctly, the input box will clear, and a new word will be displayed.

# 4. If you make a mistake, the input box will turn red.

# 5. The timer will count down from 60 seconds. After the time is up, the application will display your typing speed in words per minute.

# 6. To reset the test and start over, click the "Reset" button.

# API Usage

# The application uses an API to fetch a list of random words. The API endpoint is:
# https://random-word-api.herokuapp.com/word?number=100

# If the API request fails, a fallback list of words is used instead.
