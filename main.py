
path_to_file = "books/frankenstein.txt"

def word_count(string_of_words):
    words = string_of_words.split()
    return len(words)

def count_letters(string_of_words):
    letter_dict = {}
    for letter in string_of_words:
        if  letter.lower() in letter_dict:
           letter_dict[letter.lower()] = letter_dict.get(letter.lower()) + 1
        else:
           letter_dict[letter.lower()] = 1

    return letter_dict


def report_alpha_letters(letter_dict):
    letter_dict = list(letter_dict.items())
    # sort the list of tuples by the number index in high to low order
    letter_dict.sort(key=lambda elem: elem[1], reverse=True)
    letter_report = []
    for key in letter_dict:
        if key[0].isalpha():
            report_string = f"The '{key[0]}' character was found {key[1]} times"
            letter_report.append(report_string)
    letter_report

    return letter_report 

with open(path_to_file) as f:
    file_contents = f.read()
    # print(file_contents)

    words = word_count(file_contents)
    # print(words)

    letter_counts = count_letters(file_contents)
    # print(letter_counts)
  
    letters_report = report_alpha_letters(letter_counts)

    # printing the report of letters in the file
    print(f"\n--- Begin report of {path_to_file} ---")
    print(f"{words} words found in the document\n")

    for line in letters_report:
        print(line)
    
    print("--- End report ---")
    