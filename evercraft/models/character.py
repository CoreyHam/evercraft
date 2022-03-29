import pytest

# def func(x):
#     return x + 1

# def func2(x):
#     return x * 2


# this is where your character code will go

class Character():
    def __init__(self):
        self.values = {
            "key" : "value",
            "name" : "default",
            "alignment" : "default"
        }

    def set_name(self, name):
        self.values["name"] = name
    
    def set_alignment(self, alignment):
        self.values["alignment"] = alignment