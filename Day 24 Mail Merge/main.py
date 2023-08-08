#This Python code is designed to automate the process of mail merge by generating personalized letters using template files. 
#It first reads a list of names from the "invited_names.txt" file and stores them in the `names` list. 
#Then, it opens the "starting_letter.txt" template file, which contains a letter with a placeholder "[name]" to be replaced. 
#For each name in the `names` list, it strips any whitespace, replaces the placeholder in the template letter with the current name, and creates a new personalized letter. 
#The new letter content is written to a separate text file named "letter_for_[name].txt" based on the stripped name. 
#This process generates a set of personalized letters, each addressed to an individual name, by replacing the placeholder with the actual name from the list. 
#This code facilitates efficient creation of personalized letters for mail merge tasks.


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
