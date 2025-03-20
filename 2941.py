s = input()

croatia_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_a:
    s = s.replace(i, '*')
print(len(s))
    