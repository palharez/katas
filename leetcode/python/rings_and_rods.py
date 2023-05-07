
def rings_and_rods(rings):
    """
    O(N)
    """
    def add_to_array(arr, item):
        if item not in arr:
            arr.append(item)

        return arr

    stacks = {}

    for i in range(0, len(rings), 2):
        ring = rings[i]
        rod = rings[i+1]
        arr = stacks.get(rod, [])
        stacks[rod] = add_to_array(arr, ring)

    count = 0

    for rod, rings in stacks.items():
        if len(rings) >= 3:
            count += 1

    return count

if __name__ == '__main__':
    print(rings_and_rods(rings = "B0B6G0R6R0R6G9"), 1)
    print(rings_and_rods(rings = "B0R0G0R9R0B0G0"), 1)
    print(rings_and_rods(rings = "G4"), 0)

