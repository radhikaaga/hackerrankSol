n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    if command[0] == "pop":
        # Remove the smallest element to mimic deterministic behavior
        if s:
            s.remove(min(s))
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))
