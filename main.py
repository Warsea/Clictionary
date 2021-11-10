import tkinter as tk
from definitions import Definitions
from widgets.definition_widgets import English_widget, Bangla_widget

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
                self.meaning.destroy()
                self.meaning = Bangla_widget(self.root, word, definition_list)
            elif lang == 'en':
                definition_json, error = self.english_definition(word)
                self.meaning.destroy()
                self. meaning = English_widget(self.root, word, definition_json, error)
        
            
        self.label.after(1000, self.clipboard_watcher)




            
        


if __name__ == "__main__":
    root= tk.Tk()
    app = Clictionary(root, "Clictionary", '350x350', "Welcome to clicktionary. Copy a word to get its meaning.")
    root.mainloop()