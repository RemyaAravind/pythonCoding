

#Reading entire file 
with open('file.txt', 'r') as f:
    content = f.read()  # Returns entire file as string

#Reading line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Remove newline characters

#Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()  # Returns list of lines

#Read one line
with open('file.txt', 'r') as f:
    first_line = f.readline()


    #line1
    #line2
    #line3
    #line4