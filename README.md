# Reverser
Code Explained
This Reverser uses an iterator
to loop through the indexes of
the word given by the user. The 
iterator is set to len(word)-1,
because setting it to len(word)
raises string index out of range
because of the range differences
in Python 3. The iterator decrements
as the loop progresses, and it word[iterator]
to an external list. To make up 
for subtracting 1 from the iterator
in len(word), the first element of the
original word is appended to the reversed
list outside of the loop. The list is joined
using the joined function. Then the polished
product is printed to the console.


Protected by MIT License
reverser.py - written by Samarth Kittur
main.py - written by Samarth Kittur
README.md - written by Samarth Kittur
