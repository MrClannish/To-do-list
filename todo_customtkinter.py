import customtkinter as ctk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.tasks = []

        # Set appearance mode and color theme
        ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

        # GUI Elements
        self.task_entry = ctk.CTkEntry(root, placeholder_text="Enter a task", width=300)
        self.task_entry.pack(pady=20)

        self.add_button = ctk.CTkButton(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = ctk.CTkTextbox(root, width=300, height=200, state="disabled")
        self.task_listbox.pack(pady=20)

        self.remove_button = ctk.CTkButton(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.clear_button = ctk.CTkButton(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, ctk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        if self.tasks:
            self.tasks.pop()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "No tasks to remove.")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()
        messagebox.showinfo("Info", "All tasks cleared.")

    def update_task_listbox(self):
        self.task_listbox.configure(state="normal")
        self.task_listbox.delete("1.0", ctk.END)
        for task in self.tasks:
            self.task_listbox.insert(ctk.END, f"- {task}\n")
        self.task_listbox.configure(state="disabled")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ToDoApp(root)
    root.mainloop()