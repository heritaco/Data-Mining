"""
This module counts the number of operations in a for loop and a list comprehension.
"""

# Bucle for
count_for = 0
result_for = []
for i in range(1000000):
    result_for.append(i**2)
    count_for += 1
print("Bucle for operations:", count_for)

# Comprensión de lista
count_comp = 0
result_comp = [i**2 for i in range(1000000)]
count_comp = len(result_comp)
print("Comprensión de lista operations:", count_comp)

# ratio
print("Ratio:", count_for / count_comp)
