import pytest

# def func(x):
#     return x + 1

# def func2(x):
#     return x * 2


# this is where your character code will go

class Character():
    DEFAULT_VALUES = {
        "name": "Billy",
        "alignment": "Good"
    }

    def __init__(self, obj=None):
        if obj:
            for key, value in obj:
                print(DEFAULT_VALUES[key])
        # else self.name = DEFAULT_VALUES

    # def set_name(self, name):
    #     self.values["name"] = name

    # def set_alignment(self, alignment):
    #     self.values["alignment"] = alignment
