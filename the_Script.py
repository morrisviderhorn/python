### Task Script that when you run, it will search for a file or files you provide for specific word and print out the line number that contain the word ###

### In order to view colored text please install termcolor by opening python terminal and run the command $ pip install termcolor ###

### Import all modules that require for the script to run ###
import re
import  string  
from termcolor import colored
import argparse

### Parser - Script accept list optional parameters which are mutually exclusive ###
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-f','--files', help='Indication for the file name', required=True)

### Arguments
args = vars(parser.parse_args())

### Print the arguments ###
print(args['files'])

### Command to get input of the word to search in the document ###
search_word = input("Enter a word you want to search in the document/s ?")

### The ability to enter and search multipe documents ###
documents = args['files'].split(",")

### create the for loop to search the specific word in all document lines and print out the result ###
for document in documents:
    opened_document = open(document, encoding="utf8")
    line_number = 0
    for line in opened_document:
        line_number +=1
        if re.search(r'\b\b' + search_word, line, line_number >=0):
            print(line,"Match word", search_word, "in line number", line_number, "in the file", opened_document.name)
           

