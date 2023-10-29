from random import shuffle as l_shuffle

def reverse(name):
    reverse_string = name[::-1]
    return reverse_string

def str_shuffle(name):
    shuffle_list = list(name)
    l_shuffle(shuffle_list)
    return "".join(shuffle_list)