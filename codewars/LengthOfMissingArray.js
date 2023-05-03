function getLengthOfMissingArray(arrayOfArrays) {
    if (!arrayOfArrays || !arrayOfArrays.length) {
        return 0;
    }

    for (let i = 0; i < arrayOfArrays.length; i++) {
        if (!arrayOfArrays[i] || arrayOfArrays[i].length == 0) {
            return 0;
        }
    }

    arrayOfArrays.sort((a, b) => a.length - b.length);

    let correctLength = arrayOfArrays[0].length;

    for (let i = 0; i < arrayOfArrays.length; i++) {
        if (arrayOfArrays[i].length != correctLength) {
            return correctLength;
        }

        correctLength++;
    }

    return 0;
}
