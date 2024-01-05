import random
import sys

try:
    print(f"Received argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random argument {args[0]}")
except (IndexError, KeyError) as err:
    print(f"Error: no arguments, please provide at least one {err}")
    sys.exit(1)
except NameError:
    print(f"Error: random module not loaded")
    sys.exit(1)
else:
    print("else is running")
finally:
    print("Finally is running")