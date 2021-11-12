import csv
import requests
import langid
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Definitions:
    def bangla_definition(self, word):
        file_path = resource_path('./BanglaDictionary.csv')
        with open(file_path, 'r',encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            definitions = []
            for row in csv_reader:
                if word in row[2]:
                    definitions.append(row)
                    
            return definitions
    def english_definition(self, word):
        call = word.lower()
        try:
            r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{call}')
            j = r.json()
            if r.status_code == 200:
                return j, False
            else:
                return f'''Sorry! Couldn't find the meaning of "{word}"''', True
            
        except requests.exceptions.ConnectionError:
            return "Can't connect to the internet!!", True
        except Exception:
            return f'''Sorry! Couldn't find the meaning of "{word}"''', True

    def check_language(self, word):
        (lang, _) = langid.classify(word)
        return lang
