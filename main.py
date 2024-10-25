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

    def add_note(self):
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()
        if title and content:
            self.notes[title] = content
            self.update_notes_list()
            self.clear_fields()

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def update_notes_list(self):
        self.notes_listbox.delete(0, tk.END)
        for title, content in self.notes.items():
            preview = ' '.join(content.split()[:15])
            self.notes_listbox.insert(tk.END, f"{title}\n{' ' * len(title)}{preview}")

    def delete_note(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            selected_item = self.notes_listbox.get(selected_index)
            lines = selected_item.split('\n')
            title = lines[0].strip()
            del self.notes[title]
            self.update_notes_list()
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите заметку для удаления")

    def edit_title(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            selected_item = self.notes_listbox.get(selected_index)
            lines = selected_item.split('\n')
            old_title = lines[0].strip()
            new_title = simpledialog.askstring("Изменение заголовка", "Введите новый заголовок")
            if new_title:
                self.notes[new_title] = self.notes.pop(old_title)
                self.update_notes_list()
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите заметку для изменения заголовка")

    def edit_content(self):
        try:
            selected_index = self.notes_listbox.curselection()[0]
            selected_item = self.notes_listbox.get(selected_index)
            lines = selected_item.split('\n')
            title = lines[0].strip()
            new_content = simpledialog.askstring("Изменение содержимого", "Введите новое содержимое", initialvalue=self.notes[title])
            if new_content:
                self.notes[title] = new_content
                self.update_notes_list()
        except IndexError:
            messagebox.showwarning("Ошибка", "Выберите заметку для изменения содержимого")

    def settings_window(self):
        settings = tk.Toplevel(self)
        settings.title("Настройки")

        width_label = ttk.Label(settings, text="Ширина:")
        height_label = ttk.Label(settings, text="Высота:")

        width_entry = ttk.Entry(settings)
        height_entry = ttk.Entry(settings)

        apply_button = ttk.Button(settings, text="Применить", command=lambda: self.apply_settings(width_entry, height_entry))

        width_label.grid(row=0, column=0, padx=5, pady=5)
        width_entry.grid(row=0, column=1, padx=5, pady=5)
        height_label.grid(row=1, column=0, padx=5, pady=5)
        height_entry.grid(row=1, column=1, padx=5, pady=5)
        apply_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def apply_settings(self, width_entry, height_entry):
        try:
            width = int(width_entry.get())
            height = int(height_entry.get())
            self.geometry(f"{width}x{height}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целочисленные значения")

if __name__ == "__main__":
    app = NoteApp()
    app.mainloop()
