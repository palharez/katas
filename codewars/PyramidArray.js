function pyramid(n) {
    const response = [];

    for (let i = 1; i <= n; i++) {
        let temp = [];

        for (let k = 0; k < i; k++) {
            temp.push(1);
        }

        response.push(temp);
    }

    return response;
}

function main() {
    console.dir("Testing for 0", pyramid(0), { depth: null }); // []
    console.dir("Testing for 1", pyramid(1), { depth: null }); // [[1]]
    console.dir("Testing for 2", pyramid(2), { depth: null }); // [[1], [1, 1]]
    console.dir("Testing for 3", pyramid(3), { depth: null }); // [[1], [1, 1], [1, 1, 1]]
}

main();
