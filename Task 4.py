#Read file and handle error:

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: file 'sample.txt' not found")


#Write and append data to a file:

file = open("output.txt", "w")
file.write("Hello, Python")
file.close()

file = open("output.txt", "r")
y = file.read()
file.close()

file = open("output.txt", "a")
file.write("\nLearning file handling in Python")
file.close()

file = open("output.txt", "r")
y = file.read()
print(y)
file.close()