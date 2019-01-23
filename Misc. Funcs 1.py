#!/bin/python3

import sys
import os


def longest_string(in_val):
    '''
    (List[str]) -> str
    Returns the largest string in a list of given strings
    '''
    # Call max function to retrieve max item in list, where key is length
    # (since dealing with string chars instead of ints)
    return max(in_val, key = len)

def list_comp(in_val):
    '''
    (List[obj]) -> List[int]
    Returns a copy of the given list, with only integer values retained (all
    els deleted).
    '''
    # define new list, use list comprehension to extract all ints from input
    new_list = [x for x in in_val if type(x) == int]
    # return new list
    return new_list

def wrongresort(in_val):
    '''
    (List[int]) -> List[int]
    Takes a list of ints, sorts them in decreasing order, and returns that list.
    '''
    # Use the sort method, trigger reverse parameter for decreasing order.
    in_val.sort(reverse = True)
    # return the now sorted list
    return in_val

def resort(in_val):
    '''
    (List[int]) -> List[int]
    Takes a list of ints, sorts them in increase order, regardless of sign.
    '''
    # Use the sort method, trigger abs value pattern key for decreasing order.
    # Return the resorted list
    return sorted(in_val, key = abs)

def domain_check(domain):
    '''
    (str) -> bool
    Returns whether or not a given string is a domain or not
    '''
    # NOTE: This is very easy using regex, but re is not imported, so assuming
    # solution without regex is desired... (?)
    is_domain = True
    # ^ assume domain is valid in start
    if (not domain.contains('.')) or (len(domain[domain.rfind('.'):]) > 3):
        is_domain = False
    # return whether or not it is a domain
    return is_domain