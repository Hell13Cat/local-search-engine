import random
import db

def whatisthis(s):
    if isinstance(s, str):
        print("ordinary string")
    elif isinstance(s, unicode):
        print("unicode string")
    else:
        print("not a string")
    print(type(s))

def gen_id():
    symbols = list("qwertyuiopasdfghjklzxcvbnm1234567890")
    text = ""
    for ii in range(30):
        text += random.choice(symbols)
    return text
