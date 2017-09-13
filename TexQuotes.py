import fileinput
import string

first = True

for line in fileinput.input():
    for word in line:
        for char in word:
            if first and char == "\"":
                char = "``"
                print(char, end = "")
                first = False
            elif not first and char == "\"":
                char = "\'\'"
                print(char, end = "")
                first = True
            else:
                print(char, end = "")