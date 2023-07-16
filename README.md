# Typing Speed Test

![image](https://github.com/Bogwhite4990/Speed-Test-Typing/assets/103454208/bb3d0d84-8399-4629-890f-1d948dc21fd3)


This is a simple typing speed test application implemented in Python using the tkinter library. 
The application presents random words for the user to type and calculates their typing speed.

# Prerequisites

Make sure you have the following requirements installed:
- Python 3.x
- tkinter library
 requests library

# Getting Started

1. Clone the repository to your local machine:
git clone https://github.com/your-username/typing-speed-test.git

2. Change into the project directory:
cd typing-speed-test

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the application:
python main.py

# How to Use

1. Once you run the application, a window will open with a timer, a word to type, and an input box.
2. Start typing the word displayed in the input box.
3. If you type the word correctly, the input box will clear, and a new word will be displayed.
4. If you make a mistake, the input box will turn red.
5. The timer will count down from 60 seconds. After the time is up, the application will display your typing speed in words per minute.
6. To reset the test and start over, click the "Reset" button.

# API Usage

The application uses an API to fetch a list of random words. The API endpoint is:
https://random-word-api.herokuapp.com/word?number=100

If the API request fails, a fallback list of words is used instead.

_______________________________________________________________________________________________________________________________________________

# Typing Speed Test Flask Application

![image](https://github.com/Bogwhite4990/Speed-Test-Typing/assets/103454208/0e37f8ec-1a85-43da-82ec-c5c81f46ea0d)


This is a Flask application that implements a typing speed test. The application presents random words for the user to type and calculates their typing speed.

# Prerequisites
Make sure you have the following requirements installed:

1. Python 3.x
2. Flask
3. requests library

# Getting Started

1. Clone the repository to your local machine:
git clone https://github.com/your-username/typing-speed-test.git

2. Change into the project directory:
cd typing-speed-test

3. Install the required dependencies:
pip install -r requirements.txt

4. Run the application:
python app.py

5. Open a web browser and navigate to http://localhost:5000 to access the application.

# How to Use

1. The application will display a random word for the user to type.
2. Start typing the word displayed on the screen.
3. If you type the word correctly, the application will display the next word for you to type.
4. If you make a mistake, the application will indicate it and you can try again.
5. The application keeps track of the number of words you type correctly and calculates your typing speed in words per minute (WPM).
6. To start the typing test, click the "Start" button.
7. To check your typed word, click the "Check" button.
8. To stop the typing test, click the "Stop" button. Your typing speed will be displayed.
9. To reset the typing test and start over, click the "Reset" button.

# API Usage
The application uses an API to fetch a list of random words. The API endpoint is:


https://random-word-api.herokuapp.com/word?number=100
If the API request fails, a fallback list of words is used instead.
