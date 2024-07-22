def sum_of_first_k_natural_numbers(K):
    return K * (K + 1) // 2

# Reading input
K = int(input().strip())

# Calculate sum of first K natural numbers
result = sum_of_first_k_natural_numbers(K)

# Output the result
print(result)
