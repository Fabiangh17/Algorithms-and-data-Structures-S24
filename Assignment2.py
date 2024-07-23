import time
import winsound
import random


# Merge, this is a complement function for merge sort algorithm.
# merge two arrays ( a and b) into one (ab_Merged) in a sorted way (first lower, then higher)
def merge(a, b, ab_merged):
    i = j = 0
    print("+++++> [", end=" ")
    time.sleep(0.8)
    while i+j < len(ab_merged):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            ab_merged[i + j] = a[i]
            print(ab_merged[i + j], end=", ")
            i += 1
            time.sleep(1.5)

        else:
            # If elements swap, then play a sound
            if i != len(a):
                # play sound here
                winsound.MessageBeep(winsound.MB_OK)
                time.sleep(0.5)

            ab_merged[i + j] = b[j]
            print(ab_merged[i + j], end=", ")
            j += 1
            time.sleep(1.5)

    print("]\n")
    time.sleep(1)


# Merge Sort Algorithm
# Sort an array (data) of n elements
def merge_sort(data):
    n = len(data)

    if n < 2:                   # If only one element, then the array is already sorted
        return

    mid = n//2                  # Find the middle of the array
    A = data[0:mid]               # Move the first half of the array to a new Array A[]
    B = data[mid:n]               # Move the second half of the array to a new Array B[]

    print(f"Split {data}: \n/////> {A}  {B}\n")
    time.sleep(1)
    # Recursively split each new array
    merge_sort(A)
    merge_sort(B)

    # Recursively merge each split array.
    print(f"Merge {A} with {B}:")
    merge(A, B, data)


# Array of data to be sorted:
# Create a new array of random numbers between 1 and 100 and size (Size =20)
Size = 20
S = [random.randint(1, 100,) for _ in range(Size)]

print(f"Initial array:\n {S}")              # Print the initial array

merge_sort(S)

print(f"\n\nThe sorted data is: {S}")       # Print the sorted array
