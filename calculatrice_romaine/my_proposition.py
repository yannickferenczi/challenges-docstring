from sys import exit

NOMBRES_ROMAINS = {
    "I": {"value": 1, "reduced_by": "", "smaller_than": "VXLCDM", "forbidden_after": {"L", "C", "D", "M"}},
    "V": {"value": 5, "reduced_by": "I", "smaller_than": "XLCDM", "forbidden_after": {"V", "X", "L", "C", "D", "M"}},
    "X": {"value": 10, "reduced_by": "I", "smaller_than": "LCDM", "forbidden_after": {"D", "M"}},
    "L": {"value": 50, "reduced_by": "X", "smaller_than": "CDM", "forbidden_after": {"L", "C", "D", "M"}},
    "C": {"value": 100, "reduced_by": "X", "smaller_than": "DM", "forbidden_after": {}},
    "D": {"value": 500, "reduced_by": "C", "smaller_than": "M", "forbidden_after": {"M"}},
    "M": {"value": 1000, "reduced_by": "C", "smaller_than": "", "forbidden_after": {}},
}

# L'index de chaque tuple correspond à la place du nombre dans un chiffre
# (unité -> 1, dixaine -> 2, centaine -> 3 et millier -> 4)
# et chaque nombre romain est à l'index correspondant à sa valeur (en unités, dizaines, ...)
EQUIVALENCE_ARABIAN_TO_ROMAN = (
    None,
    ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
    ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
    ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC","CM"),
    ("", "M", "MM", "MMM"),
)


def add_romans(calculate:str)->str:
    """ Calculate the roman expression """
    # Create a list of roman numbers from the string
    list_of_numbers = get_numbers_if_valid(calculate)
    # Convert each roman number into arabian number and sum them all
    arabian_total = sum([convert_roman_to_arabian(number) for number in list_of_numbers])
    if arabian_total >= 4000:
        print("Débordement, doit respecter la plage de I à MMMCMXCIX inclus")
        exit()
    roman_total = convert_arabian_to_roman(arabian_total)
    return roman_total


def get_numbers_if_valid(roman_expression:str):
    """ Interpret roman_expression to get the roman numbers """
    # Check if characters are allowed
    for char in roman_expression:
        if not char in "IVXLCDM +-*":
            print(f"{char} ne fait pas partie de la liste des chiffres romains")
            exit()
    # Check if something else than addition is requested
    for symbol in "-*/":
        if symbol in roman_expression:
            print("Seule l'addition est permise")
            exit()
    list_of_numbers = [i.strip() for i in calculate.split("+")]
    for element in list_of_numbers:
        # Check if the amount of characters is respected
        for letter in "IXCM":
            if 4*letter in element:
                print(f"Plus de 3x {letter} à la suite n'est pas valide")
                exit()
        for letter in "VLD":
            if element.count(letter) > 1:
                print(f"{element.count(letter)}x {letter} n'est pas valide")
                exit()
        # Check if the order of characters is respected
        forbidden_letters = {"T"}
        for letter in element:
            if letter in forbidden_letters:
                print(f"{element} n'est pas valide")
                exit()
            forbidden_letters.update(NOMBRES_ROMAINS[letter]["forbidden_after"])
    # Check if at least two numbers can be identified
    if len(list_of_numbers) < 2:
        print("2 éléments minimum")
        exit()
    return list_of_numbers
        

def convert_roman_to_arabian(roman_number:str) -> int:
    """ Convert a roman number into an arabian number. """
    total = 0
    sub_total = 0
    last_letter = "nothing yet"
    for letter in roman_number:
        if last_letter in NOMBRES_ROMAINS[letter]["reduced_by"]:
            total += (NOMBRES_ROMAINS[letter]["value"] - sub_total)
            sub_total = 0
        elif last_letter in NOMBRES_ROMAINS[letter]["smaller_than"]:
            total += sub_total
            sub_total = NOMBRES_ROMAINS[letter]["value"]
        else:
            sub_total += NOMBRES_ROMAINS[letter]["value"]
        last_letter = letter
    total += sub_total
    return total


def convert_arabian_to_roman(number:int) -> str:
    """ Convert an arabian number into a roman number. """
    roman_result = ""
    for i in range(1, len(str(number)) + 1):
        roman_result = EQUIVALENCE_ARABIAN_TO_ROMAN[i][int(str(number)[-i])] + roman_result
    return roman_result


if __name__ == "__main__":
    calculate = "MMMCX + DCII"
    print(add_romans(calculate))
