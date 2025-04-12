dic = {'a': 200, 'b': 40, 'c': 100}
print(sorted([(v,k) for k,v in dic.items()]))

dic1 = {'a': 200, 'b': 40, 'c': 100}
lst = []
for k, v in dic1.items():
    n = (v, k)
    lst.append(n)
lst = sorted(lst)
print(lst)