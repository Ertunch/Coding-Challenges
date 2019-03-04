str = 'ddddeeeeaaaabbbbcccc'
unique_list = sorted(list(set(str)))
count_dict = {i:str.count(i) for i in unique_list}
sorted_dict = [(k, count_dict[k]) for k in sorted(count_dict, key=count_dict.get, reverse=True)]
for k,v in sorted_dict[:3]:
    print(v,k)
