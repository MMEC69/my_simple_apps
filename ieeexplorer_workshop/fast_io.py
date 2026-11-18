import sys

# Override built-in input() with sys.stdin.readline
# .rstrip('\r\n') safely removes trailing newline characters
input = lambda: sys.stdin.readline().rstrip('\r\n')

n = int(input())
arr = list(map(int, input().split()))

print(n)

print(arr)