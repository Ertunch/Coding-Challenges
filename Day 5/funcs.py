# sample_message = '323123541'*4000
# sample_message = '253106'
# message = '323156421351'*4000


def decode(message, verbose=1):
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
    # possible_decodings = tree.count(len(message)-1)
    # Subtracting 1 for dummy char 'q'

    # v2
    possibilities = {i: [i+b for b in possibilities[i]]
                     for i in possibilities}
    finish = {len(message) - 1: 1}
    for i in reversed(list(possibilities.keys())):
        finish[i] = sum([finish[j] for j in possibilities[i]])
    possible_decodings = finish[0]

    print(possible_decodings) if verbose else None
    return possible_decodings, possibilities


def find_partition(message, sequence_length=3, buffer=1):
    """Searches for sequences of specified length larger than 2
    (3 by default)
    Returns:
    partition_locations, list of integers
    """
    partition_locations = []
    i = 0
    start_ind = 0
    end_ind = 0
    while i < len(message):
        large_count = 0
        if int(message[i]) > 2:
            start_ind = i + buffer + 1
        while i < len(message) and int(message[i]) > 2:
            large_count += 1
            i += 1
        if large_count >= sequence_length:
            end_ind = i - buffer
            partition_locations += [start_ind, end_ind]
        while i < len(message) and int(message[i]) <= 2:
            i += 1
    return partition_locations


def solve_partial(message, sequence_length=3, verbose=1):
    """Finds combinations for partitioned message.
    """
    partition_flag = False
    if not isinstance(message, str):
        message = str(message)
    partitions = []
    print('Finding partitions...') if verbose else None
    partition_locations = find_partition(str(message),
                                         sequence_length=sequence_length)
    partition_locations.append(len(message))
    partition_locations.insert(0, 0)
    print('Done.') if verbose else None
    print('Partitioning message...') if verbose else None
    for i in range(len(partition_locations) - 1):
        try:
            if i % 2 == 0:
                partitions \
                    .append(message[partition_locations[i]:
                                    partition_locations[i+1]])
        except IndexError:
            partition_flag = True
            print('Warning: Partitioning is not functional.')
            return decode(message)[0]
            # import pdb; pdb.set_trace()
    # partitions = partitions[::2]
    print('Done.') if verbose else None
    # import pdb; pdb.set_trace()
    possibilities = []
    print('Decoding partitions...') if verbose else None
    for partition in partitions:
        possibilities.append(decode(partition, verbose=0)[0])
    print('Done.') if verbose else None
    print('Calculating combinations...') if verbose else None
    total_possibilities = 1
    for possibility in possibilities:
        total_possibilities *= possibility
    print('Done.') if verbose else None
    print(total_possibilities)
    return total_possibilities


# decode(sample_message)[0] == solve_partial(sample_message, sequence_length=3)
