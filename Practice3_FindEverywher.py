class WordsFinder:
    def __init__(self, *file_name: str):
        self.file_name = [*file_name]
    def get_all_words(self):
        all_words = dict.fromkeys(self.file_name)
        for file_name in self.file_name:
            with open(file_name, encoding='utf-8') as file:
                word_list = []
                clear_file = ''
                for line in file:
                    clear_line = ''
                    index = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for i in line:
                        if i not in index:
                            clear_line = clear_line + str(i)
                    clear_file += clear_line.lower()
                word_list = clear_file.split()
                all_words[file_name] = word_list
        return all_words

    def find(self, word):
        result = {str: int}
        result.pop(str)
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word.lower()) + 1
        return result
    def count(self, word):
        result = {str: int}
        result.pop(str)
        for name, words in self.get_all_words().items():
             counter = 0
             for i in words:
                 if word.lower() == i:
                     counter += 1
             if counter != 0:
                 result[name] = counter

        return result
finder2 = WordsFinder('test.txt', 'products.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

