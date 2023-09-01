def nb_voyelles(phrase: str) -> int:
    return len([letter for letter in phrase if letter in "aeiou"])

if __name__ == "__main__":
    text = "Whatever you think of"
    print(nb_voyelles(text))
