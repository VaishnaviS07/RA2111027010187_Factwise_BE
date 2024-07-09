def maxScore(cardPoints, k):
    n = len(cardPoints)
    
    # Calculate the total sum of all elements
    total_sum = sum(cardPoints)
    
    # Calculate the sum of the first n-k elements
    window_sum = sum(cardPoints[:n-k])
    
    # Initialize the minimum sum of the sliding window
    min_window_sum = window_sum
    
    # Slide the window across the array
    for i in range(n - k, n):
        window_sum = window_sum - cardPoints[i - (n - k)] + cardPoints[i]
        min_window_sum = min(min_window_sum, window_sum)
    
    # Maximum score is total sum minus the minimum window sum
    return total_sum - min_window_sum
