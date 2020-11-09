def get_indices_of_item_weights(weights, length, limit):
    myHash = {}

    i = 0
    while i < len(weights):
        currentWeight = weights[i]
        if (limit - currentWeight) in myHash:
            return (i, myHash[limit - currentWeight])
        else:
            myHash[currentWeight] = i
        i += 1
