def knapsack_optimized(W, weights, values):
    """
    Solves the 0/1 Knapsack problem using space-optimized Dynamic Programming.
    Time Complexity: O(N * W)
    Space Complexity: O(W)
    """
    n = len(values)
    # Initialize a DP array of size (W + 1) filled with zeros
    dp = [0] * (W + 1)
    
    # Process each item one by one
    for i in range(n):
        # Traverse backward to ensure we use values from the previous iteration
        for w in range(W, weights[i] - 1, -1):
            # Max of: excluding the item vs. including the item
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[W]

# Example usage:
if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    max_value = knapsack_optimized(capacity, weights, values)
    print(f"Maximum value in Knapsack = {max_value}")  # Output: 220
