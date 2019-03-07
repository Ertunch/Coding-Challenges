
def func1(array):
    outcome = []
    result = []
    for i in range(len(array)):
        ret = array.copy()
        intermediate = 1
        del ret[i]
        for j in ret:
            intermediate *= j
        outcome.append(result)
    return outcome

def func2(array):
    ind = 0
    ret = []
    intermediate = 1
    while ind < len(array):
        for i, j in enumerate(array):
            if i != ind:
                intermediate *= j
        ret.append(intermediate)
        intermediate = 1
        ind += 1
    return ret

def func3(array):
    i = 0
    left = [0] * len(array)
    while i < len(array):
        if i == 0:
            left[i] = array[i]
        else:
            left[i] = left[i-1] * array[i]
        i += 1
    right = [0] * len(array)
    i -= 1
    while i >= 0:
        if i == len(array) - 1:
            right[i] = array[i]
        else:
            right[i] = right[i+1] * array[i]
        i -= 1
    products = [0] * len(array)
    i = 0
    while i < len(array):
        if i == 0:
            products[i] = right[i+1]
        elif i == len(array) - 1:
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
