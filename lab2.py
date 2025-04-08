import os
import re


# This function will get the list of words and dictionary of symbol table and make a list of tuples from them.
# It takes word from words and categorize them with comparing it using regex.
def lex(words: list[str], symbol_table: dict[str, int]) -> list[tuple[str, str]]:
    res = []
    for word in words:
        # [-\+]?\d+ will check if the word is negative/positive integer
        if re.fullmatch(r"[-\+]?\d+", word):
            res.append(("INTEGER", word))
        # it will check if the word is negative/positive float
        elif re.fullmatch(r"[-\+]?\d+\.\d+", word):
            res.append(("FLOAT", word))
        elif word == "&":
            res.append(("BITWISE_AND", word))
        elif word == "&&":
            res.append(("LOGICAL_AND", word))
        elif word == "|":
            res.append(("BITWISE_OR", word))
        elif word == "||":
            res.append(("LOGICAL_OR", word))
        # it will check if the word is starting with a letter
        elif re.fullmatch(r"([a-zA-Z]+(\d+)?)+", word):
            res.append(("ID", word))
            if word not in symbol_table.keys():
                symbol_table[word] = len(symbol_table)
        else:
            res.append(("ERROR", word))
    return res


filename = input("Please enter filename to read: ")
# checks if the file exists
while not os.path.exists(filename):
    print(f"Filename '{filename}' doesn't exist")
    filename = input("Please enter filename to read: ")
# reads the file as the list of words
with open(filename, encoding="utf-8") as f:
    words: list[str] = f.read().split()

symbol_table: dict[str, int] = {}
while True:
    print(
        "Please enter one of the following options",
        "\n1)Lex",
        "\n2)Show table %s"
        % (
            "(Table will be filled only after lexer was run)"
            if len(symbol_table) == 0
            else ""
        ),
        "\n3)Exit",
    )
    option = input()
    print("-" * 20)
    match option.lower():
        case "lex" | "1" | "1)":
            for i in lex(words, symbol_table):
                print(i)
            print("-" * 20)
        case "show table" | "2" | "2)":
            if len(symbol_table) == 0:
                print("You need to do lex first")
            else:
                for word, id in symbol_table.items():
                    print(f"{word}:{id}")
        case "exit" | "3" | "3)":
            break
        case _:
            print("Option is not present")
            continue
