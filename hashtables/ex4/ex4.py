def has_negatives(a):
    myHash = {}
    result = []

    for number in a:
        myHash[number] = True

    for key in myHash:
        if key > 0:
            if -(key) in myHash:
                if key not in result:
                    result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
