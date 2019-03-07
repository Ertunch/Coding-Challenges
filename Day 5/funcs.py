# message = '251036'
# message = '33333333333'

def decode(message):
    """Counts the number of possibilities to decode a given message.
    """
    keycodes = {chr(i):str(i-ord('a')+1) for i in range(ord('a'),ord('z')+1)}
    message = str(message) + 'q'
    possibilities = {}
    for i in range(len(message) - 1):
        # print(i)
        possibilities[i] = []
        if message[i:i+2] in keycodes.values():
            possibilities[i].append(2)
        if message[i:i+1] in keycodes.values():
            possibilities[i].append(1)
    # possibilities
    tree = [0]
    for i in possibilities:
        for j in possibilities[i]:
            for k in tree:
                if k == i:
                    tree.append(k + j)

    possible_decodings = tree.count(len(message)-1)
    print(possible_decodings)
    return possible_decodings

# decode(message)
