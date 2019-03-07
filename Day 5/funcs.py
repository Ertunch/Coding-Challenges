# message = '111111'
# message = '33333333333'

def decode(message):
    """Counts the number of possibilities to decode a given message.
    """
    keycodes = {chr(i): str(i-ord('a')+1)
                for i in range(ord('a'), ord('z')+1)}  # Create keycode dict
    message = str(message) + 'q'  # Append a dummy to count last char
    possibilities = {}
    for i in range(len(message) - 1):
        # print(i)
        possibilities[i] = []
        if message[i:i+2] in keycodes.values():
            possibilities[i].append(2)
        if message[i:i+1] in keycodes.values():
            possibilities[i].append(1)
    # v1
    # Incrementally append branches
    # tree = [0]
    # for i in possibilities:
    #     for j in possibilities[i]:
    #         for k in tree:
    #             if k == i:
    #                 tree.append(k + j)
    # Appending to binary tree part can be improved significantly

    # v2
    possibilities = {i:[i+b for b in possibilities[i]] for i in possibilities}
    finish = {len(message) - 1:1}
    for i in reversed(list(possibilities.keys())):
        finish[i] = sum([finish[j] for j in possibilities[i]])  # Counting leaf nodes, starting from the bottom

    # possible_decodings = tree.count(len(message)-1)  # Subtracting 1 for dummy char 'q'
    possible_decodings = finish[0]
    print(possible_decodings)
    return possible_decodings, possibilities

# a, p = decode(message)
