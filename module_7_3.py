import string


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    class WordsFinder:
        def __init__(self, *file_names):
            self.file_names = file_names

        def get_all_words(self):
            all_words = {}
            for file_name in self.file_names:
                words_list = []
                with open(file_name, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                        words_list.extend(line.split())
                all_words[file_name] = words_list
            return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[name] = count
        return result


finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
result = finder.find('пример')  # Ищем слово 'пример'
print(result)  # Выводит словарь с названиями файлов и позициями первого вхождения