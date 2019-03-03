def looping(x):
    a = x.copy()
    a.sort()
    i = 0
    missing = 0
    while i < len(a) and a[i] <= 0:
        i += 1
    while i < len(a):
        if i == len(a) - 1:
            missing = a[i] + 1
            i += 1
            break
        elif a[i] == a[i+1]:
            i += 1
        elif a[i] == a[i+1] - 1:
            i += 1
        else:
            missing = a[i] + 1
            i += 1
            break
    if a[i - 1] <= 0:
        missing = 1
    print('Missing positive integer : ', missing)
    return missing

def gener(a):
    return next(i for i in range(1,len(a)+1) if i not in a)


def negate(a):
    i = 0
    positives = []
    while i < len(a):
        if a[i] > 0:
            positives.append(a[i])
        i += 1
    if len(positives) == 0:
        missing = 0
        return missing
    positives.sort()
    i = 0
    while i < len(positives):
        if i == len(positives) - 1:
            missing = positives[i] + 1
            i += 1
            return missing
        elif positives[i] == positives[i+1]:
            i += 1
        elif positives[i] == positives[i+1] - 1:
            i += 1
        else:
            missing = positives[i] + 1
            i += 1
            return missing
