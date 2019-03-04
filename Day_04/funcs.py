
def func1(s):
    """Python's dict comprehension,
    more efficiently implemented for tuple sorting."""
    letter_dict = {}
    for letter in s:
        if -ord(letter) not in letter_dict:
            letter_dict[-ord(letter)] = 1
        else:
            letter_dict[-ord(letter)] += 1

    tup = list(tuple(reversed(i)) for i in letter_dict.items())
    tup.sort(reverse=True)

    show_items = min(3, len(tup))
    for i in range(show_items):
        print('%s %s' % (chr(-tup[i][1]),tup[i][0]))
