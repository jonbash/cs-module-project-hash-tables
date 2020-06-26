"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
q = set(range(1, 50))

f_lookup = {}
d_lookup = {}


def f(x):
    output = f_lookup.get(x)
    if output is None:
        output = x * 4 + 6
        f_lookup[x] = output
    return output


def get_d(a, b, c):
    output = d_lookup.get((a, b, c))
    if output is None:
        output = c - a - b - 3
        f_lookup[(a, b, c)] = output
        f_lookup[(b, a, c)] = output
    return output


def sumdiff(q):
    # output = []
    for a in q:
        for b in q:
            for c in q:
                d = get_d(a, b, c)
                if d in q:
                    s = f"f({a}) + f({b}) = f({c}) - f({d})\t{f(a)} + {f(b)} = {f(c)} - {f(d)}"
                    print(s)
                    # output.append(s)
    # return output


# sumdiff(q)
'''test = semdiff(q) '''
sumdiff(q)
# for thing in test:
#     print(thing)
