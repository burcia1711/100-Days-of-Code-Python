PLACEHOLDER = "[name]"


#TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
#for each name in invited_names.txt
with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_contents = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        # Replace the [name] placeholder with the actual name.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
