import requests
import json
import os
import tkinter as tk


def fetch_data():
    item_id = entry.get()
    
    url = f"https://jsonplaceholder.typicode.com/posts/{item_id}"

    response = requests.get(url)

    data = response.json()
    save_data(data)
        


def save_data(data):
    folder_name = "json_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_name = f"{data['id']}.json"
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
window = tk.Tk()
window.title("Сохранение файла json")

label = tk.Label(window, text="Введите ID:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

fetch_button = tk.Button(window, text="Получить данные", command=fetch_data)
fetch_button.pack(pady=20)

window.mainloop()
