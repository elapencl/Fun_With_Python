row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


index1 = int(position[0]) - 1
index2 = int(position[1]) - 1
map[index2][index1] = 'x'

print(f"{row1}\n{row2}\n{row3}")
