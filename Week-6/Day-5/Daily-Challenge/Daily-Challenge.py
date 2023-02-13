#Exercise1
word = input('Write a word: ')
new_dict = {}
uniq_let = []
for letter in word:
    if letter not in uniq_let:
        uniq_let.append(letter)

for letter in uniq_let:
    new_dict[letter] = []
    for i, letter2 in enumerate(word):
        if letter == letter2:
            new_dict[letter].append(i)

print(new_dict)

#Exercise2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20"
}

wallet = int(input('Enter amount of money you have in the wallet: '))
can_afford = []

for key, value in items_purchase.items():
    int_value = int(value.replace('$', ''))
    if int_value <= wallet:
        can_afford.append(key)

can_afford.sort()

if len(can_afford) > 0:
    print(can_afford)
else:
    print('Nothing')