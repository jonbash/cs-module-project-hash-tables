from hashtable import HashTable


lookup = HashTable(8)


def expensive_seq(x, y, z):
    # Your code here

    key = f"{x},{y},{z}"

    result = lookup.get(key)
    if result is not None:
        return result

    if x <= 0:
        result = y + z
    else:
        result = expensive_seq(x-1, y+1, z) \
                + expensive_seq(x-2, y+2, z*2) \
                + expensive_seq(x-3, y+3, z*3)
    lookup.put(key, result)

    return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
