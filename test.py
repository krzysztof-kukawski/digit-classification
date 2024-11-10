s = "PAYPALISHIRING"
numRows = 4
rows = []
for i in range(numRows):
    rows.append([])
c = 0
row = 0
ascending = True

while c < len(s):
    if row == numRows -1 and ascending:
        ascending = False
    elif row == 0 and not ascending:
        ascending = True
    if(ascending):
        rows[row].append(s[c])
        row+=1
    else:
        rows[row].append(s[c])
        row-=1
    c+= 1
word = ''
for row in rows:
    for part in row:
        word += part

print(word)

