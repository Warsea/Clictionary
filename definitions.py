import csv
import requests
import langid



class Definitions:
    def bangla_definition(self, word):
        with open('BanglaDictionary.csv', 'r',encoding="utf8") as csv_file:
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
            # print(j[0].get('meanings')[0].get('definitions')[0])
            return j
        except requests.exceptions.ConnectionError:
            return "Can't connect to the internet!!"
        except Exception:
            return f'''Sorry! Couldn't find the meaning of "{word}"'''

    def check_language(self, word):
        (lang, _) = langid.classify(word)
        return lang
