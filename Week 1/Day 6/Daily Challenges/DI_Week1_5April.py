#Challenge 1
word = input("Enter a word: ")

letter_index_dict = {}

for index, letter in enumerate(word):
    if letter in letter_index_dict:
        letter_index_dict[letter].append(index)
    else:
        letter_index_dict[letter] = [index]

print(letter_index_dict)


#Challenge 2
wallet_amount = float(input("Enter the amount in your wallet: ").replace('$', '').replace(',', ''))

store_items_1 = [
    {"name": "Apple", "price": "$1.50"},
    {"name": "Banana", "price": "$0.75"},
    {"name": "Milk", "price": "$3.25"},
    {"name": "Bread", "price": "$2.50"}
]

affordable_items = sorted(item['name'] for item in store_items_1 if float(item['price'].replace('$', '').replace(',', '')) <= wallet_amount)

if affordable_items:
    print("Affordable items in alphabetical order:", affordable_items)
else:
    print("Nothing")

wallet_amount_2 = float(input("Enter the amount in your wallet: ").replace('$', '').replace(',', ''))

store_items_2 = [
    {"name": "Water", "price": "$10"},
    {"name": "TV", "price": "$500"},
    {"name": "Fertilizer", "price": "$37"},
    {"name": "Phone", "price": "$750"},
    {"name": "Speakers", "price": "$250"},
    {"name": "Laptop", "price": "$1300"},
    {"name": "Monitor", "price": "$350"}
]

affordable_items_2 = sorted(item['name'] for item in store_items_2 if float(item['price'].replace('$', '').replace(',', '')) <= wallet_amount)

if affordable_items_2:
    print("Affordable items in alphabetical order:", affordable_items_2)
else:
    print("Nothing")
