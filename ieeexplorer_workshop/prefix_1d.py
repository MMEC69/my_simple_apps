import sys


def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    # 1. Build 1-indexed Prefix Sum array in O(n)
    # pref[0] = 0 prevents out-of-bounds checks when L = 1!
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + arr[i - 1]

    # 2. Answer each query in O(1)
    out = []
    for _ in range(q):
        L, R = map(int, input().split())  # 1-based indices
        out.append(str(pref[R] - pref[L - 1]))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    main()