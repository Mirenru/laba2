import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class NoteApp(tk.Tk):
        def __init__(self):
        super().__init__()
        self.title("Заметки")
        self.geometry("500x700")
        self.notes = {}

        # Меню
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Настройки", command=self.settings_window)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Поле для ввода заголовка заметки
        self.title_label = ttk.Label(self, text="Заголовок:")
        self.title_label.pack(pady=5)
        self.title_entry = ttk.Entry(self)
        self.title_entry.pack(pady=5)

        # Текстовое поле для ввода содержимого заметки
        self.content_label = ttk.Label(self, text="Содержимое:")
        self.content_label.pack(pady=5)
        self.content_text = tk.Text(self, height=10)
        self.content_text.pack(pady=5)

        # Кнопка "Добавить"
        add_button = ttk.Button(self, text="Добавить", command=self.add_note)
        add_button.pack(pady=5)

        # Список заметок
        self.notes_listbox = tk.Listbox(self, width=50, font=('Arial', 10))
        self.notes_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

        # Кнопки управления списком
        control_frame = tk.Frame(self)
        delete_button = ttk.Button(control_frame, text="Удалить", command=self.delete_note)
        edit_title_button = ttk.Button(control_frame, text="Ред. заголовок", command=self.edit_title)
        edit_content_button = ttk.Button(control_frame, text="Ред. содержимое", command=self.edit_content)
        
        delete_button.pack(side=tk.LEFT, padx=5)
        edit_title_button.pack(side=tk.LEFT, padx=5)
        edit_content_button.pack(side=tk.LEFT, padx=5)
        control_frame.pack()


