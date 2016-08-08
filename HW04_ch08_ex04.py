#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """It is only checking if the whole string is lowercase, 
    not if there are any lowercase letters in the whole string. 
    gives boolean output if all lower = true
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """It is only checking if the string 'c' is lowercase, not the string input var s
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Evaluating based on the entire string?
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Should work? flag = false doesn't matter because even if it is false 
    and one is true then it is true
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """ even if c.islower() is true, the 'if not' won't run if c.lower() (if all of c) is false,
    so incorrectly labels camel case as false
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():
    a = 'howdy'
    b = 'HoWdY'
    c = 'HOWDY'
    print(any_lowercase1(a))
    print(any_lowercase1(b))
    print(any_lowercase1(c))

    print(any_lowercase2(a))
    print(any_lowercase2(b))
    print(any_lowercase2(c))

    print(any_lowercase3(a))
    print(any_lowercase3(b))
    print(any_lowercase3(c))

    print(any_lowercase4(a))
    print(any_lowercase4(b))
    print(any_lowercase4(c))

    print(any_lowercase5(a))
    print(any_lowercase5(b))
    print(any_lowercase5(c))

if __name__ == '__main__':
    main()
