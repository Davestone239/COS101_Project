import tkinter as tk
from tkinter import messagebox

Igbo_dict ={
    'bia' : 'come >> To move towards a person, place or point in space.' ,
    'anu' : 'meat >> The flesh of animals used as food.' ,
    'oyi' : 'cold >> A condition or sensation of temperature.' ,
    'iko' : 'cup >> A small, bowl-shaped container used to hold liquids like water, tea excetera.' ,
    'mmiri' : 'water >> A transparent, tasteless liquid essential for all forms of life, covering most of the earths surface.' ,
    'ntutu' : 'hair >> The fine thread-like strands growing on the head or body of humans and animals. ' ,
    'chi' : 'God >> A supreme being or deity worshiped as the creator and ruler of the universe in spiritual beliefs.' ,
    'kedu' : 'How are you >> A common Igbo greeting used to inquire about someones well-being.' ,
    'Ulo' : 'house >> A building for human habitation, typically with rooms and a roof.' ,
    'Ego' : 'money >> A medium of exchange in form of coins, banknotes, or digital currency.' ,
    'Akpu' : 'cassava fufu >> A starchy food made from cassava tubers, commonly eaten in West Africa.' ,
    'ututu' : 'morning >> The early part of the day, typically before noon.' ,
    'ahu' : 'body >> The physical structure of a living being, including flesh, bones, and organs. ' ,
    'obi' : 'heart/soul/mind >> The central organ of circulation; also refers to emotions, intellect, or essence of a person.' ,
    'ike' : 'strength/power >> The quality or state of being physically or mentally strong; ability to exert force or influence.' ,
    'udo' : 'peace >> A state of tranqulity, abesence of conflict or war.' ,
    'aka' : 'hand >> A vital part of the human body attached to the wrist, used for holding and manipulating objects. ' ,
    'oru' : 'work >> Physical or mental effort done to acheive a certain result. ' ,
    'ebe' : 'place/location >> A specific area, position or point in space. ' ,
    'okike' : 'creation/nature >> The proccess or act of bringing something to existence; also refers to the natural world.' ,
    'uwa' : 'world >> The Earth, along with all its inhabitants or the universe as a whole.' ,
    'aku' : 'wealth / riches >> Abundance of valuables, possessions, money or resources.'


}

Igala_dict = {
    'enu' : 'mouth >> The part of the body used for speaking,eating,drinking and breathing.' ,
    'ebole' : 'food >> Substance consumed to provide nutritional support to the body.' ,
    'oma' : 'child >> A young human being, typically below the age of puberty.' ,
    'olojo' : 'sun >> A celestial body; a star at the center of the solar system the provides light to the planets and heat to plants and animals for survial.' ,
    'echo' : 'water >>  A transparent, tasteless liquid essential for all forms of life, covering most of the earths surface.' ,
    'egbon' : 'elder sibling >> An older brother or sister in a family.' ,
    'ojo' : 'day >> A 24-hours period starting from midnight; also refers to the time of light between sunrise and sunset.' ,
    'ena' : 'part/road >> A portion of something; can also refer to a path or way of travelling.' ,
    'eko' : 'knoweledge/education >> The proccess of acquiring information,skill or understanding of a subject matter.' ,
    'ene' : 'person >> An individual human being.' ,
    'ujo' : 'House >> A structure for human habitation, typically done to acheive a purpose or earn income.' ,
    'ekojo' : 'work >> Acivity involving effort or skill, typically done to acheive a purpose or earn income.' ,
    'elubi' : 'yam >> A starchy tuber grown in tropical regions and commonly used as food.' ,
    'ebe' : 'ground >> The solid surface of the Earth; also refers to the soil or floor.' ,
    'elele' : 'sky >> The region of the atmosphere and outer space seen from the earth.' ,
    'okuko' : 'chicken >> A domesticated bird raised for food and eggs.' ,
    'efo' : 'leaf >> The green, flat part of a plant that is typically used for photosynthesis.' ,
    'je' : 'eat >> To consume food br chewing and swallowing.' ,
    'mi' : 'drink >> To consume liquids through the mouth.' ,
    'kwu' : 'speak >> To convey thoughts, feelings, or information through words.' ,
    'ojoo' : 'bad >> Something harmful or unpleasant. ' ,
    'omomi' : 'beautiful >> Pleasing to the senses or mind, esspecially in appearance.'


}

tiv_dict = {
    'Ter' : 'Father :a male elder or a respected man. ' ,
    'Mumya' : 'Mother :to a woman in a nurturing or caregiving role.' ,
    'Amaa' : 'Elder sibling :gender-neutral term that refers to an older brother or sister.' ,
    'Mba' : 'Child :ones offspring.' ,
    'Vaa' : 'Come :the action of moving or traveling toward or reaching a specific place or person. ' ,
    'Mba' : 'Eat : consuming food by taking it into the mouth.' ,
    'Ityo' : 'Thank you : an expression of gratitude or appreciation to someone. ' ,
    'Mzugh u sha' : 'Good morning :typically used in the early part of the day.' ,
    'Mbakange' : 'Food :any substance that is consumed by living organisms to provide nutritional support, energy, and maintain bodily functions.' ,
    'Amande' : 'Clothes : items worn to cover, protect, and adorn the body.' ,
    'Ityo' : 'Day :refers to the 24-hour period, from sunrise to sunset, or generally to daylight hours.' ,
    'Ikyô' : 'Heart : the muscular organ in the body that pumps blood through the circulatory system.' ,
    'Ita' : 'House :a building or structure that serves as a dwelling for people.' ,
    'Ityo' : 'Amen :an expression used to affirm or conclude a prayer, meaning "so be it" or "let it be' ,
    'Mzungu sha' : 'Good evening :greeting used in the evening, typically after the afternoon and before nightfall, to wish someone well during that time of day.' ,
    'Aondona' : 'Friend : refers to a person with whom one has a close, trusting, and supportive relationship.' ,
    'Mumya' : 'Wife :a woman who is married to a man, typically within the context of a legal or religious union.' ,
    'Mzugh sha' : 'Good  afternoon :a greeting used in the afternoon, typically between midday and evening, to wish someone well during that time of day.' ,
    'Ikyôr' : 'Month :refers to one of the twelve periods into which a year is divided, typically based on the cycles of the moon.' ,
    'Kwagh' : 'speak : To say words.' ,
    'Atyô' : 'bad : Something harmful or unpleasant. ' ,
    'Tyo' : 'beautiful : Something pleasant to look at.'

  
}



Yoruba_dict = {
    'ibi': 'place',
    'owo': 'money',
    'omo': 'child',
    'jeun': 'eat',
    'mun': 'drink it',
    'ba': 'meet him',
    'fa': 'pull it',
    'fun': 'give it',
    'sun': 'sleep',
    'ose': 'thank you',
    'rin': 'walk',
    'ri': 'see',
    'aiye': 'world',
    'ekun': 'tears',
    'ata': 'pepper',
    'aaye': 'life',
    'aile': 'evening',
    'gba': 'take',
    'gbe': 'to lift',
    'ole': 'thief'
}


def search_words(dictionary,entry_field):
    word = entry_field.get().strip().lower()
    meaning = dictionary.get(word,"Word not found in the dictionary.")
    

    
    messagebox.showinfo("Search Result" , f"{word.capitalize()} : {meaning}")
    

def open_igbo_dictionary():
    # Dickson Igbo code
    dict_window = tk.Toplevel(root)
    dict_window.title("Igbo dictionary")

    tk.Label(dict_window, text="Search Igbo Dictionary").pack(pady=5)
    entry_field=tk.Entry(dict_window, width=30) 
    entry_field.pack(pady=5)

    search_button = tk.Button(dict_window, text="Search", width=30, command=lambda: search_words(Igbo_dict, entry_field))
    search_button.pack(pady=5)


def open_igala_dictionary():
    # David Igala code
   dict_window = tk.Toplevel(root)
   dict_window.title("Igala Dictionary")

   tk.Label(dict_window, text="Search Igala Dictionary").pack(pady=5)
   entry_field=tk.Entry(dict_window, width=30 )
   entry_field.pack(pady=5)

   search_button = tk.Button(dict_window, text="Search" ,width=30, command=lambda: search_words(Igala_dict, entry_field) )
   search_button.pack(pady=5)

def open_tiv_dictionary():
    # David Tiv code
    dict_window = tk.Toplevel(root)
    dict_window.title("Tiv Dictionary")
    
    tk.Label(dict_window, text="Search Igala Dictionary").pack(pady=5)
    entry_field=tk.Entry(dict_window, width=30 )
    entry_field.pack(pady=5)

    search_button = tk.Button(dict_window, text="Search" ,width=30, command=lambda: search_words(Igala_dict, entry_field) )
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
    "Igala Language": open_igala_dictionary,
    "Igbo Language" : open_igbo_dictionary,
    "Tiv Language" : open_tiv_dictionary,
    "Yoruba Language" : open_yoruba_dic,
}

for language, command in languages.items():
    button = tk.Button(root, text=language, font=("Times New Roman", 10), width=20, command=command)
    button.pack(pady=5)

# Run the GUI for general project setup
root.mainloop()
