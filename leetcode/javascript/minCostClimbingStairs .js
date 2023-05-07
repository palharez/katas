const minCostClimbingStairs = (cost) => {
    const climb = (n, cost, memo = {}) => {
        if (n in memo) return memo[n];

        if (n > cost.length - 1) return 0;

        memo[n] = Math.min(
            cost[n] + climb(n + 1, cost, memo),
            cost[n] + climb(n + 2, cost, memo)
        );

        return memo[n];
    };

    return Math.min(climb(0, cost), climb(1, cost));
};
