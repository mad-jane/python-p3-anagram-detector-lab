class Anagram:
    def __init__(self, word):
        self.word = sorted([letter for letter in word])

    def match(self, word_list):
        self.word_list = word_list

        matches = []
        
        for word in word_list:
            if sorted([letter for letter in word]) == self.word:
                matches.append(word)
        return matches