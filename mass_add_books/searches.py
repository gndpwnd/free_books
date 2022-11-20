# open names in browser tab

books = [
"Gibson, James J: An Ecological Approach to Visual Perception",
"Goldberg, Elkhonon: The New Executive Brain",
"Gray, Jeffrey and Neil McNaughton: The Neuropsychology of Anxiety",
"LeDoux, Joseph: The Emotional Brain",
"Panksepp, Jaak: Affective Neuroscience",
"Sacks, Oliver: The Man who Mistook his Wife for a Hat",
"Sacks, Oliver: Awakenings",
"Sacks, Oliver: An Anthropologist on Mars",
"Swanson, Larry: Brain Architecture: Understanding the Basic Plan",
]


import webbrowser

for name in books:
    name = name + " free pdf download"
    webbrowser.open_new_tab("https://www.google.com/search?q=" + name)
    while True:
        if input("Continue? (y/n)") == "y":
            break


print("\n\nDone...")