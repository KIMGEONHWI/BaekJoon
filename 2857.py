agents = [input().strip() for _ in range(5)]
fbi_indices = []

for idx, name in enumerate(agents, 1):
    if 'FBI' in name:
        fbi_indices.append(str(idx))

if fbi_indices:
    print(' '.join(fbi_indices))
else:
    print("HE GOT AWAY!")
