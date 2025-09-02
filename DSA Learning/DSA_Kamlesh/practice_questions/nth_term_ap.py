def nth_term_ap(a1, a2, n):
    d = a2 - a1  
    return a1 + (n - 1) * d  

# Example usage:
a1 = 1
a2 = 3
n = 10
print(f"{n}th_term_ap: ",nth_term_ap(a1, a2, n))  # Output: 19
