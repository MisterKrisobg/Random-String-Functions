
def CapLastLetter(msg):
    word = ""
    let = msg[-1].capitalize()
    word = msg[0:-1] + let
    print(word)

def ReverseWord(msg):
    word = ""
    i = len(msg)
    while i > 0:
        word += msg[i-1]
        i -= 1
    print(word)

def CapEvery2ndLet(word):
    NewWord = ""
    i = len(word)
    for let in word:
        if i % 2 == 1:
            NewWord += let.upper()
        else:
            NewWord += let
        i -= 1
    print(NewWord)
