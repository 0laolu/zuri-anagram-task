# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # checking if the two arguments are the same length, if not don't proceed
    word_length = len(word)
    anagram_length = len(anagram)

    # if the number of letters in the arguments are not the same, don't proceed. If they are, then proceed
    if word_length != anagram_length: 
        print('Invalid input')
    
    # turning the words in the argument to a list
    word_to_list = list(word)
    anagram_to_list = list(anagram)

    # sorting the words in the list for comparison
    sorted_list = sorted(word_to_list)
    sorted_anagram = sorted(anagram_to_list)

    # comparing the two arguments 
    if sorted_list == sorted_anagram: 
        print(True)
    else: 
        print(False)

# defining the arguments for the function's parameters
word_var = input('Enter your first word: ')
anagram_var = input('Enter your second word: ')

# calling the function
find_anagram(word_var, anagram_var)
