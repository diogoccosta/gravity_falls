#!/usr/bin/env python
# # -*- coding: utf-8 -*-

__author__ = "Diogo Carvalho"
__copyright__ = "Copyright 2018"
__credits__ = ["Diogo Carvalho", "Teodoro Hideki", "Pérola Harumi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Diogo Carvalho"
__email__ = "diogoccosta@icloud.com"
__status__ = "Test"

def getMode():
    while True:
        mode = int(raw_input('\nEnter the Key Number or "99" to Brute Force the message: '))
        if mode == 99:
            return mode
        elif (mode >= -26 and mode <= 26):
            return mode


def getMessage():
    crypMessage = raw_input('Enter the message: ')
    return crypMessage


def translateMessage(message, mode):

    transMessage = ""
    for ch in message:
        if ch.isalpha():
            finalLetter = chr((ord(ch.lower()) - 97 + mode) % 26 + 97)
        else:
            finalLetter = ch.lower()
        transMessage += finalLetter

    return transMessage


def main():
    mode = getMode()
    crypMessage = getMessage()
    if mode == 99:
        print "\nThe translated message could be:"
        m = -26
        while True:
            if m <= 26:
                transMessage = translateMessage(crypMessage, m)
                print "mode: ", m, "message: ", transMessage
            else:
                return
            m += 1
    else:
        transMessage = translateMessage(crypMessage, mode)
        print "\nThe translated message is: ", transMessage


def again():
    while True:
        decision = raw_input('\nUse "/a" to enter a New Message or "/q" to Quit --> ')
        if decision == '/a':
            main()
        elif decision == '/q':
            print "\nSee you...\n\n"
            exit()


main()
again()
