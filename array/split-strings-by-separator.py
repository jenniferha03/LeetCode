class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        current_word = ""
        final_list = []
        for word in words:
            word += separator
            for letter in word:
                if letter != separator:
                    current_word += letter
                elif current_word != "":
                    final_list.append(current_word)
                    current_word = ""
        return final_list
