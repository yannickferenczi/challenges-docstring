def nb_voyelles(phrase: str)->int :
    return sum(phrase.count(el) for el in "aeiou")

if __name__ == "__main__":
    text = "Whatever you think of"
    print(nb_voyelles(text))
