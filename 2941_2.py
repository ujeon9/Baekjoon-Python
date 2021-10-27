a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

str = input()
for i in a:
    str = str.replace(i, "a")
print(len(str))
