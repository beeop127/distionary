import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def searchData(word):
    if word in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %
              get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("invalid word ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("invalid word")
        return " "
