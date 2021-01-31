"""
Write a function get_positions that receives two arguments: sentence (a string) and word_list (a list with 3 strings).
The first argument contains 2 words that appear in the second argument concatenated with a single space in between.
The function returns a string with the position in the list of the first word and the position of the second word in the list, separated by a single space. When any of the words of the sentence are not in the list, the function returns the empty string. Positions start counting at zero.

"""

def get_positions(sentence, word_list):
    sentence = sentence.split()
    if (sentence[0] in word_list) and (sentence[1] in word_list):
        a = str(word_list.index(sentence[0]))
        word_list[int(a)] = "jlopes"
        b = str(word_list.index(sentence[1]))
        return "{0} {1}".format(a, b)
    else:
        return ""