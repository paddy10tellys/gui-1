#!/usr/bin/env python

import argparse  # parse sys.argv for the target textfile to analyze
import tkinter as tk
from tkinter import ttk

print("running word counter program as a gui...")

def show_count():
    aLabel.configure(foreground='red')

def on_return(event):
    print("you hit return")
    analyse()
    show_count()


def on_click():
    print("you clicked the button")
    analyse()
    show_count()

def on_exit():
    win.destroy()


def analyse():
    try:
        parser = argparse.ArgumentParser()  # create parser object
        parser.add_argument('filename')  # give the parser obj the file
        args = parser.parse_args()  # use string 'args' to create output file

        with open(args.filename) as sourcefile:  # open sourcefile
            suffixstr = args.filename[-4:]  # last 4 chars is ".txt"
            prefixstr = args.filename[0:-4] # the chars before ".txt"
            outputfilename = prefixstr + "-count" + suffixstr
            print("\n" + "Analysing {}".format(args.filename))
            print("Results saved in " + '"' + outputfilename + '"' + "\n")

            data = sourcefile.read()
            data = data.lower()  # make everything lower case
            for ch in '"''!@#$%^&*()-_=+,<.>/?;:[{]}~`\|':
                data = data.replace(ch," ")  # replace punctuation with whitespace

#  do something with the data eg count & list words in freq order

            wordDict = {}  # create empty dictionary

            for word in data.split():
                if word not in wordDict:
                    wordDict[word] = 1  # add the word
                else:
                    wordDict[word] = wordDict[word] + 1  # increment count

            commonest = sorted(wordDict.items(), key=lambda x: (x[1], x[0]), reverse=True)
            for word, freq in commonest:
                print("%-13s %d" % (word, freq))

# write results
            with open(outputfilename, "w") as outputfile:
                args = ("total words: ", len(data.split()), " Unique words: ", len(commonest))
                summary = ("{} {} {} {}".format(*args))
                print("\n" + summary + "\n")
                outputfile.write(summary)
                for word, freq in commonest:
                    outputfile.write("\n\n%-13s %d \n" % (word, freq))

        aLabel.configure(text=" "+summary)

    except IOError as e:
        print("Error: %s not found." % args.filename)
        print("Usage>> ./wordsort.py sometext.txt")

# Python lists have a built-in sort() method that modifies the list in-placs
# and a sorted() built-in function that builds a new sorted list from an
# iterable the sorted() function returns a list, even if that is not the type
# that was passed in the iterable can be a dictionary. A dictionary is
# actually a mapping rather than a list - so, an unordered set of key:value
# pairs. Each key is unique within the dictionary the iterable here is all of
# the items contained in the dictionary wordDict, you iterate through the
# (word:no of occurrences of the word, key:value pairs) in wordDict the second
# parameter in the sorted function, the key parameter, should not be confused
# with the key in the key:value pairs in the dictionary, they are different
# things in the sorted function, the key (in this example) specifies (another)
# function (a lambda) to be called on each key:value mapping prior to making
# the sorting comparison x is all of the key:value mappings in wordDict, and
# x[1] just tells the sorted function to sort on the second element in each
# pair, e.g., the value, rather than x[0] the key if the values are the same
# then x[0] tellts the sorted function to sort on the first element in each
# pair, e.g., the word, alphabetically, but this is reversed by reverse = True
# i.e., pass a function that looks up the value associated with a key... to
# sort just the keys, based on their associated values, that's what lambda is
# doing here lambda's are anonymous functions. Function parameter(s) are
# specified before the colon. The function expression is specified after the
# colon. what is expressed is what is returned reverse = True returns largest
# to smallest order Commonest is the sorted list of words, sorted from most
# common to least common, extracted from wordDict
# Python lists have a built-in sort() method that modifies the list in-placs
# and a sorted() built-in function that builds a new sorted list from an
# iterable the sorted() function returns a list, even if that is not the type
# that was passed in the iterable can be a dictionary. A dictionary is
# actually a mapping rather than a list - so, an unordered set of key:value
# pairs. Each key is unique within the dictionary the iterable here is all of
# the items contained in the dictionary wordDict, you iterate through the
# (word:no of occurrences of the word, key:value pairs) in wordDict the second
# parameter in the sorted function, the key parameter, should not be confused
# with the key in the key:value pairs in the dictionary, they are different
# things in the sorted function, the key (in this example) specifies (another)
# function (a lambda) to be called on each key:value mapping prior to making
# the sorting comparison x is all of the key:value mappings in wordDict, and
# x[1] just tells the sorted function to sort on the second element in each
# pair, e.g., the value, rather than x[0] the key if the values are the same
# then x[0] tellts the sorted function to sort on the first element in each
# pair, e.g., the word, alphabetically, but this is reversed by reverse = True
# i.e., pass a function that looks up the value associated with a key... to
# sort just the keys, based on their associated values, that's what lambda is
# doing here lambda's are anonymous functions. Function parameter(s) are
# specified before the colon. The function expression is specified after the
# colon. what is expressed is what is returned reverse = True returns largest
# to smallest order Commonest is the sorted list of words, sorted from most
# common to least common, extracted from wordDict


win = tk.Tk()
win.geometry('450x450+500+300')
win.resizable(width=False, height=False)
win.title("Word Counter")
win.bind('<Return>', on_return)

button = ttk.Button(win, text="Count", command=on_click)
button.grid(row=0, column=0)

aLabel = ttk.Label(win, width=45, text=" click to analyse the words in this .txt File")
aLabel.grid(row=0, column=1)

exit_button = ttk.Button (win, text = "Good-bye.", command = on_exit)
exit_button.grid(row = 12, column=0)

win.mainloop()
input('Press ENTER to exit')
