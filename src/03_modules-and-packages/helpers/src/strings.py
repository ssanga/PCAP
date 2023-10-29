# Hiding module entities
# __all__ = ['extract_upper', 'extract_lower']

def extract_upper(phrase):
    """
    extract_upper takes a string and return a list cointaining
    only the upper letters
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

def _hidden_function(phrase):
    pass


# print(f"__name__ in helpers.py {__name__}")

if __name__ == "__main__":
    print("HELLO FROM HELPERS")