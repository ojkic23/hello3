import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Kviz")
        self.master.geometry("600x400")
        self.master.config(bg="#F5F5F5")

        self.questions = [
            {
                "question": "Ko je bio prvi čovek na Mesecu?",
                "answers": ["Neil Armstrong", "Buzz Aldrin", "Alan Shepard", "Yuri Gagarin"],
                "correct_answer": "Neil Armstrong"
            },
            {
                "question": "Koji je glavni grad Francuske?",
                "answers": ["London", "Rim", "Pariz", "Berlin"],
                "correct_answer": "Pariz"
            },
            {
                "question": "Ko je napisao 'Rat i mir'?",
                "answers": ["Leo Tolstoj", "Fjodor Dostojevski", "Jane Austen", "Charles Dickens"],
                "correct_answer": "Leo Tolstoj"
            },
            {
                "question": "Ko je pronalazač struje?",
                "answers": ["Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", "Albert Einstein"],
                "correct_answer": "Nikola Tesla"
            },
            {
                "question": "Koliko je godina trajao Prvi svetski rat?",
                "answers": ["4 godine", "6 godina", "2 godine", "8 godina"],
                "correct_answer": "4 godine"
            },
            {
                "question": "Koji je najviši vrh sveta?",
                "answers": ["Everest", "Kilimanjaro", "Makalu", "Mont Blanc"],
                "correct_answer": "Everest"
            },
            {
                "question": "Koji je najveći okean na svetu?",
                "answers": ["Atlantski okean", "Indijski okean", "Severni ledeni okean", "Tihi okean"],
                "correct_answer": "Tihi okean"
            },
            {
                "question": "Ko je napisao 'Ana Karenjina'?",
                "answers": ["Fjodor Dostojevski", "Leo Tolstoj", "Virginia Woolf", "Jane Austen"],
                "correct_answer": "Leo Tolstoj"
            },
            {
                "question": "Ko je osvojio najviše Gremi nagrada?",
                "answers": ["Michael Jackson", "Beyoncé", "Taylor Swift", "Quincy Jones"],
                "correct_answer": "Quincy Jones"
            },
            {
                "question": "Ko je režirao film 'Pulp Fiction'?",
                "answers": ["Steven Spielberg", "Quentin Tarantino", "Martin Scorsese", "Christopher Nolan"],
                "correct_answer": "Quentin Tarantino"
            },
            {
                "question": "Ko je najpoznatiji slikar renesanse?",
                "answers": ["Leonardo da Vinci", "Michelangelo", "Rafaelo", "Titian"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "Ko je autor knjige 'Romeo i Julija'?",
                "answers": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Fjodor Dostojevski"],
                "correct_answer": "William Shakespeare"
            },
            {
                "question": "Ko je osnivač kompanije Apple?",
                "answers": ["Steve Jobs", "Bill Gates", "Elon Musk", "Mark Zuckerberg"],
                "correct_answer": "Steve Jobs"
            },
            {
                "question": "Koji je najveći kontinent na svetu?",
                "answers": ["Afrika", "Azija", "Evropa", "Severna Amerika"],
                "correct_answer": "Azija"
            },
            {
                "question": "Ko je prvi američki predsednik?",
                "answers": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"],
                "correct_answer": "George Washington"
            },
            {
                "question": "Ko je osvojio najviše Oskara za glumu?",
                "answers": ["Meryl Streep", "Katharine Hepburn", "Jack Nicholson", "Daniel Day-Lewis"],
                "correct_answer": "Katharine Hepburn"
            },
            {
                "question": "Ko je izumeo telegraf?",
                "answers": ["Samuel Morse", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla"],
                "correct_answer": "Samuel Morse"
            },
            {
                "question": "Koji je najveći grad u Sjedinjenim Američkim Državama?",
                "answers": ["New York City", "Los Angeles", "Chicago", "Houston"],
                "correct_answer": "New York City"
            },
            {
                "question": "Ko je najpoznatiji naučnik koji je iznio teoriju relativiteta?",
                "answers": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "correct_answer": "Albert Einstein"
            },
            {
                "question": "Koja je najveća pustinja na svetu?",
                "answers": ["Sahara", "Atakama", "Gobi", "Kalahari"],
                "correct_answer": "Sahara"
            }
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.master, text="", font=('Arial', 16), bg="#F5F5F5", wraplength=500)
        self.question_label.pack(pady=10, padx=20)

        self.answer_var = tk.StringVar()
        self.answer_var.set("")
        self.answers_frame = tk.Frame(self.master, bg="#F5F5F5")
        self.answers_frame.pack()

        self.next_button = tk.Button(self.master, text="Sledeće pitanje", font=('Arial', 12), command=self.current_question)
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        self.question_label.config(text=self.questions[self.current_question]["question"])
        
        for widget in self.answers_frame.winfo_children():
            widget.destroy()

        answers = self.questions[self.current_question]["answers"]
        random.shuffle(answers)
        for answer in answers:
            btn = tk.Button(self.answers_frame, text=answer, font=('Arial', 12), bg="#4CAF50", fg="white", width=30, height=2, command=lambda ans=answer: self.check_answer(ans))
            btn.pack(pady=5)

    def check_answer(self, selected_answer):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_score()

    def show_score(self):
        messagebox.showinfo("Kviz je završen", f"Osvojili ste {self.score} od {len(self.questions)} poena.")

# Kreiranje prozora
window = tk.Tk()
window.configure(bg="#F5F5F5")
game = QuizGame(window)

# Pokretanje petlje za prikazivanje prozora
window.mainloop()