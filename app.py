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


root.mainloop()