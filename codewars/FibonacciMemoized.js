function fibonacci(n, memo = {}) {
  if (n in memo) {
    return memo[n];
  }

  if (n < 2) return n;

  const result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);

  memo[n] = result;

  return result;
}
