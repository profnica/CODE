import json
import difflib
from difflib import get_close_matches

data= json.load(open("076 data.json"))

word= input("Enter word: ")

def translate(W):
    W= W.lower()
    if W in data:
        return data[W]
    elif W.title() in data:
        return data[W.title()]
    elif W.upper() in data:
        return data[W.upper()]
    elif len(get_close_matches(W, data.keys())) > 0:
        # elif is used when you have multiple condition
        #  to give the user a word suggestion (the get_close_matches will cater for the word suggestion)
        suggestion = input("Did you mean %s instead? Enter Y if yes, N if no:" % get_close_matches(W, data.keys())[0]) 
    # the arg %s will be the word that is most similar to the input word
    # the arg [0] means to give a word that is most similar to the input
        if suggestion == "Y":
            return data[get_close_matches(W, data.keys())[0]]
        elif suggestion=="N":  
            return "This word does not exist. Please double check it"
        else:
            # to cater for when the user input a word that doesn't make sense
            return "We did not understand your entry"
    else:
        return "This word does not exist. Please double check it"


output=translate(word)
if type(output) ==list:
    for item in output:
        print(item)
else:
    print(output)




 
