class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        words = ""
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                for line in file:
                    for char in line:
                        if char not in punct:
                            words += char.lower()
                words = words.split()
                all_words.update({i: words})
                return all_words

    def find(self, word):
        res = {}
        counter = 0
        for name, words in self.get_all_words().items():
            counter += 1
            if words == word.lower():
                res = {name: counter}
        return res

    def count(self, word):
        res = {}
        counter = 0
        for name, words in self.get_all_words().items():
            if words == word.lower():
                counter += 1
                res = {name: counter}
        return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

