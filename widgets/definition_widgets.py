import tkinter as tk

class English_widget:
    def __init__(self, master, word,parts_of_speech, definition, example):
        frame = tk.LabelFrame(master, text=word, padx=5, pady=5)
        frame.pack(padx=10, pady=10)
        
        part_of_speech_widget = tk.Label(frame, text=parts_of_speech)
        part_of_speech_widget.grid(row=0, column=0)
        definition_widget = tk.Label(frame, text=definition, wraplength = 250, justify = "left")
        definition_widget.grid(row=1, column=1)
        example_widget = tk.Label(frame, text=f'example: {example}', wraplength = 250, justify = "left")
        example_widget.grid(row=3, column=1)