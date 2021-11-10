import tkinter as tk
from definitions import Definitions
from widgets.definition_widgets import English_widget

class Clictionary(Definitions):
    def __init__(self, root, title, geometry, welcome_message):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.text = tk.StringVar()
        self.text.set(welcome_message)
        self.last_clipboard = 'Copy a word!'
        self.label = tk.Label(self.root, textvariable=self.text)
        self.label.pack()
        self.meaning = English_widget(self.root)
     



      
        self.clipboard_watcher()

    

    def clipboard_watcher(self):
        try:
            word = (self.root.clipboard_get()).strip()
        except tk.TclError:
            word = None

        
        if word != self.last_clipboard and word!=None:
            self.last_clipboard = word
            lang = self.check_language(word)
            if lang == "bn":
                definition_list = self.bangla_definition(word)
                tk.Label(self.root, text=str(definition_list)).pack()
            elif lang == 'en':
                definition_json, error = self.english_definition(word)
                self.meaning.destroy()
                self. meaning = English_widget(self.root, word, definition_json, error)
        
            
        self.label.after(1000, self.clipboard_watcher)

    def english_widget(self, master, word,parts_of_speech, definition, example):
        frame = tk.LabelFrame(master, text=word, padx=5, pady=5)
        frame.pack(padx=10, pady=10)
        
        part_of_speech_widget = tk.Label(frame, text=parts_of_speech)
        part_of_speech_widget.grid(row=0, column=0)
        definition_widget = tk.Label(frame, text=definition, wraplength = 200, justify = "left")
        definition_widget.grid(row=1, column=1)
        example_widget = tk.Label(frame, text=f'example: {example}', wraplength = 200, justify = "left")
        example_widget.grid(row=3, column=1)



            
        


if __name__ == "__main__":
    root= tk.Tk()
    app = Clictionary(root, "Clictionary", '350x400', "Welcome to clicktionary. Copy a word to get its meaning.")
    root.mainloop()