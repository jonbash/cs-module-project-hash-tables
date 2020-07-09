"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
# q = set(range(1, 50))

f_lookup = {}
sum_lookup = {}
diff_lookup = {}


def f(x):
    output = f_lookup.get(x)
    if output is None:
        output = x * 4 + 6
        f_lookup[x] = output
    return output


def get_d(a, b, c):  # lookup never used; made it slower
    return c - a - b - 3


def get_sum(a, b):
    if (a, b) in sum_lookup:
        return sum_lookup[(a, b)]
    output = f(a) + f(b)
    sum_lookup[(a, b)] = output
    sum_lookup[(b, a)] = output
    return output


def get_diff(c, d):
    if (c, d) in diff_lookup:
        return diff_lookup[(c, d)]
    output = f(c) - f(d)
    diff_lookup[(c, d)] = output
    return output


def sumdiff_string(a, b, c, d):
    return f"f({a}) + f({b}) = f({c}) - f({d})\t" \
        + f"{f(a)} + {f(b)} = {f(c)} - {f(d)}"


def sumdiff(q):
    # output = []
    for a in q:
        for b in q:
            for c in q:
                d = get_d(a, b, c)
                if d in q:
                    print(sumdiff_string(a, b, c, d))
                    # output.append(s)
    # return output


def alt_sumdiff(q):
    sum_lookup = {}
    diff_lookup = {}

    for a in q:
        for b in q:
            ab_sum = f(a) + f(b)
            cd_diff = f(a) - f(b)
            sum_lookup[(a, b)] = ab_sum
            diff_lookup[cd_diff] = (a, b)
    for a in q:
        for b in q:
            ab_sum = sum_lookup[(a, b)]
            cd = diff_lookup.get(ab_sum)
            if cd is not None:
                (c, d) = cd
                print(sumdiff_string(a, b, c, d))





# sumdiff(q)
# test = semdiff(q)
# sumdiff(q)
alt_sumdiff(q)
# for thing in test:
#     print(thing)
