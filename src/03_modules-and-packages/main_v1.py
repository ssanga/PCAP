# import helpers

# name = "Keith Thompson"
# print(f"Lowercase Letters {helpers.extract_lower(name)}")
# print(f"Uppercase Letters {helpers.extract_upper(name)}")

# import helpers as h

# name = "Keith Thompson"
# print(f"Lowercase Letters {h.extract_lower(name)}")
# print(f"Uppercase Letters {h.extract_upper(name)}")


# from helpers import extract_lower, extract_upper

# name = "Keith Thompson"
# print(f"Lowercase Letters {extract_lower(name)}")
# print(f"Uppercase Letters {extract_upper(name)}")

# from helpers import extract_lower as e_low, extract_upper

# name = "Keith Thompson"
# print(f"Lowercase Letters {e_low(name)}")
# print(f"Uppercase Letters {extract_upper(name)}")


# antes de usar el package
# print(f"We're import 'helpers' from 'main'")
from helpers import *

# print(f"We're import 'extras' from 'main'")
import extras

# print(f"__name__ in main.py {__name__}")

name = "Keith Thompson"
print(f"Lowercase Letters {extract_lower(extras.name)}")
print(f"Uppercase Letters {extract_upper(extras.name)}")
print(f"Hidden Function {_hidden_function(extras.name)}")