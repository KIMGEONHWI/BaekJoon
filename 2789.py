word = input().strip()
ban = set("CAMBRIDGE")
result = ''.join([ch for ch in word if ch not in ban])
print(result)
