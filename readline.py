'''
with open('file1.txt','r') as file:
    lines = files.readlines()
print("list of lines:",lines)
'''
'''
with open('file1.txt','r') as file:
    for line in file:
        print(line.strip())
'''
'''
with open('file1.txt','r') as file:
    seperate_lines = [line.strip() for line in file.readlines()]
    print(seperate_lines)
'''

#["Hello","students","how","are","you","today"]
'''
program to create a txt file access the text file data and use the data to split the lines into series of words
and use space to perform split operation
sample.txt
Hello students 
how are you today
'''

'''
fileobj.mode - opening access
fileobj.name - returns the file name

file methods:-
fileno() - file number in your tool
flushy() - clears the write buffer from i/o
isatty() - returns boolean o/p , file steam is iterable or not
readline(n) - particular line from the file
truncate(n) - truncates the file to a specific length
'''
with open('sample.txt','r') as file:
    lines = file.readlines()
    words = []
    for line in lines:
        words.extend(line.strip().split())
    print(words)  