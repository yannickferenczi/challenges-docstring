import pytest

@pytest.mark.parametrize("sentence, expected", [
    ("", 0),
    ("docstring", 2),
    ("bonjour comment allez-vous ?", 9),
    ("je vais à paris", 5),
    ("vas-y !", 1),
]) 
def test_should_return_the_sum_of_the_vowels_countained_in_the_input_string(sentence, expected):
    got = nb_voyelles(sentence)
    assert got == expected
