#!/usr/bin/env python3

def bit_reverse(n):
    """Reverse binary representation of 8-bit integer"""
    result = 0
    # loop through each bit
    for i in range(8):
        # isolate i'th bit of int
        component = n & (1 << i)  # 'bitwise and' and 'bit shift'
        # shift bit to new correct position
        if i < 4:
            rev_component = component << (7 - (2 * i))
        else:
            rev_component = component >> ((2 * i) - 7)
        # 'add' shifted bit back to result
        result |= rev_component  # 'bitwise or'
    return result


for x in range(256):
    print(f"x: {x}")
    print(f"bin: {format(x, '#010b')}")
    print(f"rev: {format(bit_reverse(x), '#010b')}")
