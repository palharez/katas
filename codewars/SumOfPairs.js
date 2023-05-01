function sumPairs(ints, s) {
    const seen = {};

    for (const value of ints) {
        if (seen[s - value]) {
            return [s - value, value];
        }

        seen[value] = true;
    }

    return undefined;
}

function main() {
    console.dir(sumPairs([1, 2, 3, 4], 5)); // Must be [2,3]
}

main();
