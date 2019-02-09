function OneHundred(n) { 
    console.log(n)
    if (n == 100) {
        return n
    }
    return OneHundred(n + 1)
}
