from vars import PATH, alphabet_map

def word_count(contents):
    return len(contents.split())

def read_file(path):
    with open(path) as f:
        return f.read() 

def letter_count(contents: str):
    copy = alphabet_map.copy()
    for c in list(contents.lower()):
        if c.isalpha():
            copy[c] += 1
    return copy

def main():
    contents = read_file(PATH)
    print(word_count(contents))
    print(letter_count(contents))

if __name__ == "__main__":
    main()
    
