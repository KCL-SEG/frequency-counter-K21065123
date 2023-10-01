"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for i in items:
        str_items = [str(i) for i in items]

    
    for i in str_items:
        c = str_items.count(i)
        frequencies[i]= c

    return frequencies 
