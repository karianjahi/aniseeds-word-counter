"""
This is the python code that counts words in a sentence
"""
import re
# from bs4 import BeautifulSoup
class WordCounter:
    """
    We want to have a class that counts words
    """
    def __init__(self):
        pass
    
    def __repr__(self):
        """
        This is the class represenation method
        Returns
        -------
        str
            what is the class all about!
        """
        return "This is a word counter instance"
    
    def count_words(self, sentence):
        """This method counts words in a sentence

        Parameters
        ----------
        sentence : str
            Just a sentence

        Returns
        -------
        int
            no of words in a sentence
        """
        assert isinstance(sentence, str), "Input must be a string"
        sentence = self._deal_with_hyphens(sentence)
        splitted_text = sentence.split()
        return len(splitted_text)
    
    def _deal_with_hyphens(self, sentence):
        """
        Replace hyphens with space

        Parameters
        ----------
        sentence : str
            text
        """
        return re.sub("-", " ", sentence)
        
        

if __name__ == "__main__":
    inst = WordCounter()
    text = "school"
    print(inst.count_words(sentence=text))
