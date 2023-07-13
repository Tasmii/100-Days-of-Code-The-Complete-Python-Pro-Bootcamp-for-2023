PLACEHOLDER = "[name]"
with open(r"Day 24 Mail Merge\invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Day 24 Mail Merge\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Day 24 Mail Merge\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
