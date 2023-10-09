import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                'question': "What is the capital of France?",
                'options': ["London", "Berlin", "Paris"],
                'correct_answer': "Paris"
            },
            {
                'question': "Which planet is known as the Red Planet?",
                'options': ["Venus", "Mars", "Jupiter"],
                'correct_answer': "Mars"
            },
            {
                'question': "What is the largest mammal in the world?",
                'options': ["Elephant", "Giraffe", "Blue Whale"],
                'correct_answer': "Blue Whale"
            },
        ]

        self.label = tk.Label(root, text="")
        self.label.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        for i, option in enumerate(self.questions[self.question_number]['options']):
            rb = tk.Radiobutton(root, text=option, variable=self.radio_var, value=option)
            rb.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.question_number]['correct_answer']

        if selected_answer == correct_answer:
            self.score += 1

        self.question_number += 1

        if self.question_number < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Result", f"You scored {self.score}/{len(self.questions)}")
            self.root.destroy()

    def show_question(self):
        self.label.config(text=self.questions[self.question_number]['question'])
        self.radio_var.set(None)
        for i, option in enumerate(self.questions[self.question_number]['options']):
            self.root.nametowidget(self.root.winfo_children()[i + 2]).config(text=option)

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
