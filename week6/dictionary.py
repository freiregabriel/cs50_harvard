words = set()

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n"))
    file.close()
    return True

def check(word):
    return word.lower() in words

def size():
    return len(words)

def unload():
    return True