from random import sample

# Do not modify or remove this
with open("/usr/share/dict/words", "r") as f:
    WORD_LIST = [w.strip("\n") for w in f.readlines()]