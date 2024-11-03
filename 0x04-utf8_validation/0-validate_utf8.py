#!/usr/bin/python3
""" UTF8 Validation"""


def validUTF8(data):
    """ will determine if a given data set represents a valid utf-8 encoding """

    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

         mask_byte = 1 << 7


         if number_bytes == 0:

             while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

             if number_bytes == 0:
                 continue

        else:

            if not (i & mask_1 and not (i & mask_2)):
                return False

            number_bytes -= 1

        return number_bytes == 0
