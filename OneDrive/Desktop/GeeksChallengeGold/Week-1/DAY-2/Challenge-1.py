import re

matrix_lines = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!",
]

matrix = [list(row) for row in matrix_lines]

rows = len(matrix)
cols = len(matrix[0])

raw_message = ""
for col in range(cols):
    for row in range(rows):
        raw_message += matrix[row][col]


decoded_message = re.sub(r'(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])', ' ', raw_message)

print("Message caché :")
print(decoded_message)
