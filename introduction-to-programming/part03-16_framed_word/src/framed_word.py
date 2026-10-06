word = input("Please type in a string: ")
w = "*"
s = " "

total_inside = 28  # inner width between the side stars

# If the word length is even or odd, adjust spacing
if len(word) % 2 == 0:
    left_spaces = (total_inside - len(word)) // 2
    right_spaces = left_spaces
else:
    left_spaces = (total_inside - len(word)) // 2
    right_spaces = left_spaces + 1  # add one more space to balance the odd length

print(w * 30)
print(f"*{s * left_spaces}{word}{s * right_spaces}*")
print(w * 30)