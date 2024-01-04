class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update


class MappingSubClass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

    def print_something(self):
        print("Print something")

    __update = print_something


# Mapping.__update
print(dir(Mapping))
print(dir(MappingSubClass))