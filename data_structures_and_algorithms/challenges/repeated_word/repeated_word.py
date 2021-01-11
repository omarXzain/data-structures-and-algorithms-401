import re

def repeat_word(sentence):
    dicts = []
    repeat = None
    words = re.sub(r'[^\w\s]','',sentence, re.UNICODE) 
    single_word = words.split()

    for word in single_word: 
        if word in dicts: 
            repeat = word
            break
        dicts.append(word) 
    return repeat

if __name__ == "__main__":
    print(repeat_word('hi my name is jordan and i live in jordan '))
    print(repeat_word('can you can a can in a can'))
    print(repeat_word('eye eye iphone head troll head iphone troll iphone'))

