from collections import Counter

# Input
x = int(input())  # Number of shoes
shoe_sizes = list(map(int, input().split()))
shoe_inventory = Counter(shoe_sizes)

n = int(input())  # Number of customers

earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        earnings += price
        shoe_inventory[size] -= 1  # One shoe of this size sold

print(earnings)
