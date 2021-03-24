def reverse_string(str):
    """Reverse the given string with reversed() and join()"""
    reversed_str = "".join(reversed(str))
    return reversed_str # return the reversed string to the caller


str = "TechTalent Academy"

print(f"The original string is: {str}")
print(f"The reverse string is : {reverse_string(str)}") # call function


"""The reversed() function creates an iterator for a string that goes backward 
through the string.
The join() method can work with an iterator.
    separator.join(iterable/iterator)
Join all the elements together, separated by separator, and return the result.

The following is taken from https://realpython.com/python-for-loop/
Term       Meaning
Iteration  The process of looping through the objects or items in a collection.
Iterable   An object (or the adjective used to describe an object) that can be
           iterated over.
Iterator   The object that produces successive items or values from its
           associated iterable.
iter()     The built-in function used to obtain an iterator from an iterable.

An iterator is an object with a __next__ method that returns the next element
of an iterable.

For more on iterable and iterator see
https://www.programiz.com/python-programming/iterator

Every iterator is also an iterable, but not every iterable is an iterator.
For example, a list is iterable but a list is not an iterator.
"""
