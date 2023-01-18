"""We test the count_words.py module here
"""
from count_words import WordCounter
class TestWordCounter:
    """
    This is the class that tests the WordCounter
    """
    
    def test_empty(self):
        """
        test zero words
        """
        text = ""
        assert WordCounter().count_words(text) == 0
    
    def test_one_word(self):
        """
        test one word
        """
        text = "moritz"
        assert WordCounter().count_words(text) == 1
    
    def test_multiple_words(self):
        """
        test multiple words
        """
        text = "Test multiple words"
        assert WordCounter().count_words(text) == 3
        
    def test_linebreak(self):
        """
        Testing for line breaks e.g.
        I am going\nfor lunch\nwith my two\nfriends
        """
        text = "I am going\nfor lunch\nwith my two\nfriends"
        assert WordCounter().count_words(text) == 9
    
    def test_hyphens(self):
        """
        Sometimes text has hyphens in between words
        """
        text = "This-text-has-hyphens"
        assert WordCounter().count_words(text) == 4
        
    def test_html(self):
        """
        Test html
        Try to modify the function to deal with html notation
        """
        text = "<h1> This is my heading <\h1>"
       # assert WordCounter().count_words(text) == 4
        