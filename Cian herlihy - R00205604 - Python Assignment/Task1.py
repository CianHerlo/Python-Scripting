"""
Cian Herlihy - R00205604 - Python Assignment

To complete this task. I wanted to take a list and check if the words (Strings) have '?' in them.
I did this by iterating through the list of words and use '.count()' to check how many times it includes
the character '?'. If it contains the character then I print out that word saying it contains it.

I also had to check what letters were common, so I took the first word on the list and compared it against
the other words in the list. I check if the first letter is in all words and if it is then I add it to a list.
I increment a counter to show it was in the word, but I only increment it by 1 even if it is in twice or more.
This is because I only want to know if it was in the word or not for a later check to see if it was in all the words.
I do this by checking if the counter is equal to the list size - 1. -1 is because I already know it is included in the
first word, so I don't check it again. This gives me a list of all the common letters. However, I need to remove
duplicates, so I only add it to a common letter list if it's not already in it.

Lastly, I check to see how many times that letter appears in that word and that's a simple for loop print statement.
I use the same '.count()' on each word and print out the count to show how many times it appears.
"""

list_of_strings = ["barack", "obar?ma", "war", "russia?", "mak?er"]
list_size = len(list_of_strings)


def check_for_question_mark(list_strings):
    for i in range(list_size):
        if list_strings[i].count("?") > 0:
            print(f'{list_strings[i]} does contain a "?"')


def common_letters(list_strings):
    common_chars = []
    for char in list_strings[0]:  # Iterate through characters in first word
        matching_char_count = 0
        for i in range(1, list_size):  # Iterate through words in list and check if it contains character
            if list_strings[i].count(char) > 0:
                matching_char_count = matching_char_count + 1
                continue
            else:
                break

        if matching_char_count >= list_size - 1:
            if common_chars.count(char) == 0:  # Does not add unique char if it is already in list
                common_chars.append(char)

    for letter in range(len(common_chars)):
        print(f'\nCharacter {common_chars[letter]} appears in all items')
        for i in range(list_size):
            print(f'{list_strings[i]} contains "{common_chars[letter]}" '
                  f'{list_strings[i].count(common_chars[letter])} time(s)')


def main():
    check_for_question_mark(list_of_strings)
    common_letters(list_of_strings)


if __name__ == "__main__":
    main()
