with open('./input.txt', 'r') as f:
    for line in f:
        line: str = line.strip().lower()
        inverted_line: str = line[::-1]
        characters: set = {character for character in line}
        if line == inverted_line:
            print(f"YES, {len(characters)}")
        else:
            print("NO, -1")