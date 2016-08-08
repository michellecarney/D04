#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################


def count(stringinput, letterinput):
    count = 0
    for letter in stringinput:
        if letter == letterinput:
            count = count + 1
    print(count)



###############################################################################
def main():

    count('caaaaaaaaaaat','a')
    count('meWoW', 'W')
    count('coding is fun', 'i')


if __name__ == '__main__':
    main()
