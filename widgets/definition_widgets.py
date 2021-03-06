import tkinter as tk

class English_widget:
    def __init__(self, master, word=None, definition_json="Let's go!!", error=True):
        self.frame = tk.LabelFrame(master, text=word, font='bold', foreground='blue4', padx=5, pady=5)
        self.frame.pack(padx=10, pady=10)
        if error==False:
            data = self.data_extractor(definition_json)
            self.part_of_speech_widget = tk.Label(self.frame, text=data.get('part_of_speech'))
            self.part_of_speech_widget.grid(row=0, column=0)
            self.definition_widget = tk.Label(self.frame, text=(data.get('definition') + '\n'), wraplength = 250, justify = "left")
            self.definition_widget.grid(row=1, column=1, sticky='W')
            if data.get('example') != None:
                example = f"example: {data.get('example')}"
                self.example_widget = tk.Label(self.frame, text=example, wraplength = 250, justify = "left")
                self.example_widget.grid(row=2, column=1, sticky='W')
            synonyms = f"""synonyms: {data.get('synonyms')}"""
            self.synonym_widget = tk.Label(self.frame, text=synonyms, wraplength = 250, justify = "left")
            self.synonym_widget.grid(row=3, column=1, sticky='W')
            antonyms = f"""antonyms: {data.get('antonyms')}"""
            self.antonym_widget = tk.Label(self.frame, text=antonyms, wraplength = 250, justify = "left")
            self.antonym_widget.grid(row=4, column=1, sticky='W')
        else:
            self.error = tk.Label(self.frame, text=definition_json, wraplength = 250, justify = "left")
            self.error.pack()

    def destroy(self):
        self.frame.destroy()

    def data_extractor(self, definition_json):
        data={}
        meaning = definition_json[0].get('meanings')[0]
        data['part_of_speech'] = meaning.get('partOfSpeech')
        data['definition'] = meaning.get('definitions')[0].get('definition')
        data['example'] = meaning.get('definitions')[0].get('example')
        synonyms = meaning.get('definitions')[0].get('synonyms')
        data['synonyms'] = str(synonyms[:5])
        antonyms = meaning.get('definitions')[0].get('antonyms')
        data['antonyms'] = str(antonyms[:5])
        return data


class Bangla_widget:
    def __init__(self, master, word, definition_list):
        self.frame = tk.LabelFrame(master, text=word,font='bold', foreground='dark green', padx=5, pady=5)
        self.frame.pack(padx=10, pady=10)
        
        meaning = ', '
        if len(definition_list)!=0:
            eng_list = []
            for i in definition_list[:30]:
                eng_list.append(i[1])
            meaning = meaning.join(eng_list)
        else:
            meaning = 'No english meaning found!'
        self.eng = tk.Label(self.frame, text=meaning, wraplength = 250, justify = "left")
        self.eng.grid(row=0, column=0)
    
    def destroy(self):
        self.frame.destroy()


