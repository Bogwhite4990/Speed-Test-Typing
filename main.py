import tkinter as tk
import random
import requests
import time


class TypingSpeedTest:
    API_URL = "https://random-word-api.herokuapp.com/word?number=100"

    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        self.master.geometry("500x300")

        self.word_list = []
        self.current_word = ""
        self.start_time = None
        self.total_words_typed = 0

        self.timer_label = tk.Label(self.master, text="60", font=("Arial", 16))
        self.timer_label.place(x=450, y=10, anchor="ne")
        self.word_label = tk.Label(self.master, text=self.current_word, font=("Arial", 20))
        self.word_label.place(x=50, y=100)
        self.entry_box = tk.Entry(self.master, font=("Arial", 20))
        self.entry_box.place(x=50, y=200)
        self.reset_button = tk.Button(self.master, text="Reset", font=("Arial", 16), command=self.reset)
        self.reset_button.place(x=225, y=250)

        self.entry_box.bind("<KeyRelease>", self.check_word)
        self.entry_box.focus()

        self.get_word_list()
        self.new_word()

    def timer(self):
        if self.start_time is None:
            self.start_time = time.time()
        time_left = int(60 - (time.time() - self.start_time))
        if time_left >= 0:
            self.timer_label.config(text=str(time_left))
            self.master.after(1000, self.timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.entry_box.config(state="disabled")
            self.word_label.config(text="")
            wpm = int(self.total_words_typed / 1)
            message = f"You typed {wpm} words per minute!"
            self.timer_label.config(text=message)

    def get_word_list(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            self.word_list = response.json()
        else:
            # Use a fallback list if API request fails
            self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

    def new_word(self):
        self.current_word = random.choice(self.word_list)
        self.word_label.config(text=self.current_word)

    def check_word(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.timer()
        typed_word = self.entry_box.get()
        if typed_word == self.current_word:
            self.total_words_typed += 1
            self.entry_box.delete(0, tk.END)
            self.entry_box.config(bg="green")
            self.new_word()
        else:
            self.entry_box.config(bg="red")

    def reset(self):
        self.current_word = ""
        self.start_time = None
        self.total_words_typed = 0
        self.timer_label.config(text="60")
        self.entry_box.delete(0, tk.END)
        self.entry_box.config(state="normal")
        self.word_label.config(text="")
        self.get_word_list()
        self.new_word()
        self.entry_box.focus()


root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
