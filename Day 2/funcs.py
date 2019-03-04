
def func1(a):
    outcome = []
    result = []
    for i in range(len(a)):
        b=a.copy()
        r = 1
        del b[i]
        for j in b:
            r*=j
        outcome.append(result)
    return outcome

def func2(a):
    e =0
    b = []
    r=1
    while e < len(a):
        for i,j in enumerate(a):
            if i != e:
                r*=j
        b.append(r)
        r = 1
        e+=1
    return b

def func3(a):
    i = 0
    left = [0] * len(a)
    while i < len(a):
        if i == 0:
            left[i] = a[i]
        else:
            left[i] = left[i-1] * a[i]
        i += 1
    right = [0] * len(a)
    i -= 1
    while i >= 0:
        if i == len(a) - 1:
            right[i] = a[i]
        else:
            right[i] = right[i+1] * a[i]
        i -= 1
    products = [0] * len(a)
    i = 0
    while i < len(a):
        if i == 0:
            products[i] = right[i+1]
        elif i == len(a) - 1:
            products[i] = left[i-1]
        else:
            products[i] = left[i-1] * right[i+1]
        i += 1
    return products


def solution(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result
