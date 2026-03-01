import tkinter as tk
from tkinter import messagebox

def get_year_word(k):
    if 11 <= k % 100 <= 14:
        return "лет"
    elif k % 10 == 1:
        return "год"
    elif 2 <= k % 10 <= 4:
        return "года"
    else:
        return "лет"

def show_age():
    try:
        k = int(entry.get())
        if 1 <= k <= 99:
            word = get_year_word(k)
            result_label.config(text=f"Мне {k} {word}")
        else:
            messagebox.showerror("Ошибка", "Введите число от 1 до 99")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число")


root = tk.Tk()
root.title("Возраст")

tk.Label(root, text="Введите возраст (1-99):").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Показать", command=show_age).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
