from flask import Flask, render_template, jsonify, request
import random
import requests
import time

app = Flask(__name__)


class TypingSpeedTest:
    API_URL = "https://random-word-api.herokuapp.com/word?number=100"

    def __init__(self):
        self.word_list = []
        self.current_word = ""
        self.start_time = None
        self.total_words_typed = 0

        self.get_word_list()
        self.new_word()

    def get_word_list(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            self.word_list = response.json()
        else:
            # Use a fallback list if API request fails
            self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi",
                              "lemon"]

    def new_word(self):
        self.current_word = random.choice(self.word_list)

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.start_time = None

    def check_word(self, typed_word):
        if self.start_time is None:
            return False
        if typed_word == self.current_word:
            self.total_words_typed += 1
            self.new_word()
            return True
        return False

    def reset(self):
        self.current_word = ""
        self.start_time = None
        self.total_words_typed = 0
        self.get_word_list()
        self.new_word()


typing_speed_test = TypingSpeedTest()


@app.route("/")
def index():
    return render_template("index.html", current_word=typing_speed_test.current_word)


@app.route("/start", methods=["POST"])
def start():
    typing_speed_test.start_timer()
    return jsonify({"success": True})


@app.route("/check", methods=["POST"])
def check():
    typed_word = request.form.get("typed_word", "")
    if typing_speed_test.check_word(typed_word):
        return jsonify({"correct": True, "next_word": typing_speed_test.current_word})
    return jsonify({"correct": False})


@app.route("/stop", methods=["POST"])
def stop():
    typing_speed_test.stop_timer()
    wpm = int(typing_speed_test.total_words_typed / 1)
    return jsonify({"wpm": wpm})


@app.route("/reset", methods=["POST"])
def reset():
    typing_speed_test.reset()
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run()
