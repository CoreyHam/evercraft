import pytest
from evercraft.models.character import Character

# def test_answer():
#     assert func(4) == 5

# def test_whatever():
#     assert func2(4) == 8


# Make sure we have access to Character class
def test_CreateChar():
    c = Character()
    assert isinstance(c, Character)

# Set character name
def test_CreateCharName():
    data = {
        "name":"Billy"
    }
    c = Character(data)
    # c = Character(c1)
    assert c.name == "Billy"

# Two Characters
def test_CreateTwoCharName():
    c1 = Character()
    c1.set_name("Billy")
    c2 = Character()
    c2.set_name("Jeff")
    assert c1.values["name"] == "Billy" and c2.values["name"] == "Jeff"

def test_CreateAlignment():
    c = Character()
    c.set_alignment("Good")
    assert c.values["alignment"] == "Good"
    

def test_CreateTwoAlignment():
    c1 = Character()
    c1.set_alignment("Good")
    assert c1.values["alignment"] == "Good"
    c2 = Character()
    c2.set_alignment("Evil")
    assert c2.values["alignment"] == "Evil"
    