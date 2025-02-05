import tkinter as tk
import pymongo

# connect to mongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["PyChat"]
messager_col = db["messages"]

# Tkinter GUI
root = tk.Tk()
root.title("PyChat")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def send_messages():
  if entry.get():
    messager_col.insert_one({"text": entry.get()})
    entry.delete(0, tk.END)
    fetch_messages()

send_button = tk.Button(root, text="Send", command=send_messages)
send_button.pack(pady=5)

messages_label = tk.Label(root, text="Messages:\n", justify="left")
messages_label.pack(pady=5)

def fetch_messages():
  messages = messager_col.find().sort("_id", 1)
  messages_label.config(text="Messages:\n" + "\n".join(f"-{m['text']}" for m in messages))
  root.after(2000, fetch_messages)

fetch_messages()
root.mainloop()