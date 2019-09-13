'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # need a base case. if i am checking every single every in order from the first one to the letter next to it, i need to stop at the last letter.
    if not word:
        return 0
    # check if letter [0] and [1] are 'th'
    if word[0:2] == 'th':
        # increment count and continue on
        return 1 + count_th(word[1:])
    # if not continue with the next letter
    else:
        return count_th(word[1:])
