words = input().upper()
unique_words = list(set(words))
list = []

for i in unique_words:
    count = words.count(i)
    list.append(count)

if list.count(max(list)) >= 2:
    print("?")
else:
    print(unique_words[(list.index(max(list)))])