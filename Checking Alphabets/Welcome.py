letter = input("Enter a Letter: ")

if letter >= "a" and letter <= "z":
    print(f"The letter {letter} is a LOWERCASE Alphabet")
elif letter >= "A" and letter <= "Z":
    print(f"The letter {letter} is a UPPERCASE Alphabet")
else:
    print("It is not an Alphabet")