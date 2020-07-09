#!/usr/bin/env python3

class BitReverser:
    """
    Reverses the bits of 8-bit numbers
    (e.g., `0b01001011` becomes `0b11010010`)
    """
    def __init__(self):
        self.componentizers = {}
        for i in range(8):
            self.componentizers[i] = 1 << i

    def bit_reverse(self, n):
        result = 0
        for i in range(8):
            component = n & self.componentizers[i]
            if i < 4:
                rev_component = component << (7 - (2 * i))
            else:
                rev_component = component >> ((2 * i) - 7)
            result |= rev_component
        return result


rev = BitReverser()
for x in range(256):
    print(f"x: {x}")
    print(f"bin: {format(x, '#010b')}")
    print(f"rev: {format(rev.bit_reverse(x), '#010b')}")
