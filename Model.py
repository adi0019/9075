from collections import Counter

from textblob import TextBlob



# from language_tool_python import LanguageTool
# from language_tool_python import LanguageTool
# import GingerIt


class WordCountResponse:
    def __init__(self, count):
        self.count = count

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")

    #  self.grammar_check = LanguageTool('en-US')
    # self.grammar_check = GingerIt()
    def correct_spell(self, text):
        # Helo,World, subscribe, to my channel
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)
       # model = SpellCheckerModule

    # class WordCountResponse:
    #     def __init__(self, count):
    #         self.count = count





# if __name__ == "__main__":
#     obj = SpellCheckerModule()
#     message = "Hello, subscride, to my chanel"
#     print(obj.correct_spell(message))

# print(obj.correct_grammar(message))


