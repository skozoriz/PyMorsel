# PyMorsel count_words
from collections import defaultdict
import re

def count_words(s):
    """
    string -> dict 
    words count
    mixed case
    punctuation accounted
    """
     
    d = defaultdict(int)  
    ss = s.lower().split()
    for i in ss:
        d[re.sub(r"\W^'", "", i)] += 1                
    return d
        

if __name__ == "__main__":
        s = "oh what a day what a lovely day"
        print(count_words(s))  
        # {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

        s = "Oh what a day, what a lovely day!"
        print(count_words(s))
        # {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

        s = "don't stop believing, do not"
        print(count_words(s))
        # {"don't": 1, 'stop': 1, 'believing': 1, 'do': 1, 'not': 1}