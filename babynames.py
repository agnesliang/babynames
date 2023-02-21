#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A: organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> add_name({}, 2002, 30, 'Aggie')
    {'Aggie': {2002: 30}}
    >>> add_name({}, 2004, 23, 'Angus')
    {'Angus': {2004: 23}}
    """
    if name not in names:
        names[name] = {}
        names[name][year] = rank
        return names

    if year not in names[name]:
        names[name][year] = rank
        return names

    rank = names[name][year]
    names[name][year] = rank
    return names




def add_file(names, filename):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}
    >>> add_file({'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}, 'small-2010.txt')
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    with open(filename) as f:
        files = f.readlines()
        year = int(files[0].strip())

        for line in files[1:]:
            line = line.strip()
            s_line = line.split(',')
            rank = int(s_line[0])
            m = s_line[1]
            f = s_line[2]

            add_name(names, year, rank, m)
            add_name(names, year, rank, f)

    return names

def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    """
    n_dict = {}
    for file in filenames:
        add_file(n_dict, file)
    return n_dict


def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> search_names ({'Angus': {2002:1},'Justice': {2013:3}, 'Lara':{2005:6}}, 'us')
    ['Angus', 'Justice']
    >>> search_names ({'Chase': {2092:40}, 'Christian': {2015:28}, 'Charlotte':{2025:6}}, 'ch')
    ['Charlotte', 'Chase', 'Christian']
    >>> search_names ({'Jaden': {2002:18}, 'Pablo': {2011:13}, 'Mia':{2045:9}}, 'il')
    []
    """
    t_names = []
    l = target.lower()
    for name in names:
        name_lower = name.lower()
        if l in name_lower:
            t_names.append(name)
    return sorted(t_names)


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
