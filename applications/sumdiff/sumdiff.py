"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
f_lookup = {}
sum_f_lookup = {}
diff_f_lookup = {}
abcd_lookup = {}

def lookup(x, table, func):
    result = table.get(x)
    if result is None:
        result = func(x)
        table[x] = result
    return result


def f(x):
    return lookup(x, f_lookup, lambda x: x * 4 + 6)


def sum_f(x, y):
    return lookup((x, y),
                  sum_f_lookup,
                  lambda x: f(x[0]) + f(x[1]))


def diff_f(x, y):
    return lookup((x, y),
                  diff_f_lookup,
                  lambda x: f(x[0]) - f(x[1]))


def abcd_eq(a, b, c, d):
    return lookup((a, b, c, d),
                  abcd_lookup,
                  lambda x: sum_f(x[0], x[1]) == diff_f(x[2], x[3]))


def sumdiff(q):
    output = []
    for a in q:
        for b in q:
            for c in q:
                for d in q:
                    if abcd_eq(a, b, c, d):
                        output.append((a, b, c, d))
    return output


test = sumdiff(q)
for thing in test:
    print(thing)
