import sys

def main():
    input = sys.stdin.readline
    N, X, K = map(int, input().split())
    pos = X
    for _ in range(K):
        A, B = map(int, input().split())
        if pos == A:
            pos = B
        elif pos == B:
            pos = A
    print(pos)

if __name__ == "__main__":
    main()