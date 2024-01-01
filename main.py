from vars import PATH

def word_count(contents):
    return len(contents.split())

def read_file(path):
    with open(path) as f:
        return f.read() 

def symbol_count(contents: str):
    char_map = {}
    for c in contents:
        low = c.lower()
        if low in char_map:
            char_map[low] += 1
        else:
            char_map[low] = 1
    return char_map

def print_symbols(char_map):
    print("Chars: ")
    chars = list(char_map)
    chars.sort()
    for c in chars:
        if c.isalpha():
            print(f"The '{c}' appeared in book {char_map[c]} times.") 
    print("-------------------------------------")

def main():
    contents = read_file(PATH)
    symbols = symbol_count(contents)

    print(word_count(contents))
    print_symbols(symbols)

if __name__ == "__main__":
    main()

