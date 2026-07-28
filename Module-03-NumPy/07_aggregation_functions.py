import numpy as np

# ==========================================
# Aggregation on 1D Array
# ==========================================

marks = np.array([50, 60, 70, 80, 90])

print("Marks:", marks)

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))


# ==========================================
# Aggregation on 2D Array
# ==========================================

marks = np.array([
    [80, 70, 90],
    [60, 75, 85]
])

print("\n2D Marks:")
print(marks)

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))