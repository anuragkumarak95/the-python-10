r'''Author Anurag Kumar(mailto:anuragkumarak95@gmail.com)
This Example uses data.json file in same directory as its data source,
and returns meaningsfor word input by user.

It is a standard example for Shell Bases user inetractive application build on python.
'''
from  difflib import get_close_matches
import json

data = json.load(open("data.json"))

def means(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    else:
        similars = get_close_matches(word, data.keys(),n=1, cutoff=0.8)
        if len(similars)==1:
            resp = input("Did you meant %s [Y/n]? :" % similars[0])
            if resp.lower() == 'y':
                return data[similars[0]]
            else:
                return "Word not found in dictionary!"
        else:
            return "Word not found in dictionary!"


if __name__=="__main__":
    word = input("Enter a Word :")
    meaning = means(word)
    if type(meaning) == list:
        for idx, i in enumerate(meaning):
            print (idx,i)
    else:
        print(meaning)
