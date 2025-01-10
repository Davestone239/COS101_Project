import tkinter as tk
from tkinter import messagebox

hausa_dict = {
    'zo': 'Come',
    'kia': 'Head',
    'je': 'Go',
    'sannu': 'Hello',
    'kudi': 'Money',
    'na gode': 'Thank you',
    'gobe': 'Tomorrow',
    'babba': 'Big',
    'yau': 'Today',
    'dare': 'Night',
    'dogon yaro': 'neem tree',
    'rakee': 'Sugar cane',
    'ruwa': 'Water',
    'dadi': 'delicious',
    'dauka': 'take',
    'kyau': 'beautiful',
    'uwa': 'mum',
    'baba': 'dad',
    'rubutu': 'text'
}

def search_words(dictionary,entry_field):
    word = entry_field.get().strip().lower()
    meaning = dictionary.get(word,"Word not found in the dictionary.")
    

    
    messagebox.showinfo("Search Result" , f"{word.capitalize()} : {meaning}")
    

def open_hausa_dictionary():
    # Daniel hausa code
    dict_window = tk.Toplevel(root)
    dict_window.title("Hausa Dictionary")
    
    tk.Label(dict_window, text="Search Hausa Dictionary").pack(pady=5)
    entry_field=tk.Entry(dict_window, width=30 )
    entry_field.pack(pady=5)

    search_button = tk.Button(dict_window, text="Search" ,width=30, command=lambda: search_words(hausa_dict, entry_field) )
    search_button.pack(pady=5)



# Create the main window
root = tk.Tk()
root.title("Nigerian Languages Dictionary")
root.geometry("600x250")

# Add a label
label = tk.Label(root, text="DICTIONARY\nNIGERIAN LANGUAGES\nClick Preferred Language", font=("Times New Roman", 13), justify="center")
label.pack(pady=5)

# Add buttons for each language
languages = {
    "Hausa Language": open_hausa_dictionary
}

for language, command in languages.items():
    button = tk.Button(root, text=language, font=("Times New Roman", 10), width=20, command=command)
    button.pack(pady=5)

# Run the GUI for general project setup
root.mainloop()