import json
import re
import os


class Parser:
    """Class parsing text input from user.

    Its role is to remove unwanted words and extract relevant keywords.
    """

    def __init__(self, input):
        """Inits a Parser"""

        PATH_TO_STOPWORDS = f"{os.path.dirname(os.path.abspath(__file__))}/static/resources/stopwords.json"
        try:
            with open(PATH_TO_STOPWORDS) as stopwords_file:
                self.stopwords = json.load(stopwords_file)
        except IOError as err:
            print(f"Loading file error : {str(err)}")
            self.stopwords = ""
        self.input = input
        self.parsed_text = ""
        self.location = False
        self.address = False
        self.parse()
        self.location_or_address()

    def parse(self):
        """Extract relevant words in an easily readable format."""

        lower_text = self.input.lower()
        text_without_punctuation = re.sub(r'[^\w\s]', ' ', lower_text)
        words_to_process = text_without_punctuation.split()
        relevant_words = []
        for word in words_to_process:
            if word not in self.stopwords:
                relevant_words.append(word)
        self.parsed_text = ' '.join(relevant_words)

    def location_or_address(self):
        """Determine wether user is looking for an address or a location."""

        if "adresse " in self.parsed_text:
            self.location = True
            self.parsed_text = self.parsed_text.split(' ', 2)[2]
        else:
            self.address = True


if __name__ == "__main__":
    """For testing purposes."""
    user_input = input("Message? ")
    ut = Parser(user_input)
    print(f"{ut.parsed_text}")
    if ut.location:
        print("Location")
    if ut.address:
        print("Address")
