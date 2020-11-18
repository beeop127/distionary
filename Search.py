import json

data = json.load(open("data.json"))


def searchData(word):

    if word in data:
        return data[word]

    elif word.upper() in data:
        return data[word.upper()]

    else:
        print("invalid word")
        return " "
