from tkinter import Tk, Frame, TOP, X, Button, LEFT, Entry, Label
import os
import requests
import json


class Main(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.init_main()

    def init_main(self):
        toolbar = Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=TOP, fill=X)

        label = Label(toolbar, text="Введите ID:")
        label.pack(pady=10)

        self.entry = Entry(toolbar)
        self.entry.pack(pady=10)

        fetch_button = Button(toolbar, text="Получить данные", command=self.fetch_data)
        fetch_button.pack(pady=20)


    def fetch_data(self):
        item_id = self.entry.get()
    
        url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"

        response = requests.get(url)

        data = response.json()
        self.save_data(data)
    
    
    def save_data(self,data):
        folder_name = "json_data"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            file_name = f"{data['id']}.json"
            file_path = os.path.join(folder_name, file_name)
    
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)

window = Tk()
app = Main(window)
window.title("Сохранение файла json")
window.geometry("400x300")
window.mainloop()