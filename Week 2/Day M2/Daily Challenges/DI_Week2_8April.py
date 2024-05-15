#Solve the Matrix
matrix = [
    ['7', "i", "i"],
    ["T", "s", "x"],
    ["h", "%", "?"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]
max_length = max(len(row) for row in matrix)
for row in matrix:
    row += [''] * (max_length - len(row))
columns = []
for col_index in range(max_length):
    column = ''
    for row in matrix:
        column += row[col_index]
    columns.append(column)
message = ''
for column in columns:
    alpha_chars = ''
    for char in column:
        if char.isalnum():
            alpha_chars += char
        else:
            if alpha_chars:
                message += alpha_chars + ' '
                alpha_chars = ''
    if alpha_chars:
        message += alpha_chars + ' '
print("Decrypted message:", message.strip())

print('Are we still in the matrix?')




list_of_strings=[['7ii'],["Tsx"],["h%?"],["i #"],["sM "],["$a "],["#t%"],["^r!"]]
list_of_lists=[list(srings) for string in list_of_strings]
def decoder(user_list):
    password=""
    for col in range(len(list_of_lists[0])):
        for row in range(len(list_of_lists)):
            x=