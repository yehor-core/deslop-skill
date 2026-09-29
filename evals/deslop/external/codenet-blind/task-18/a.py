import sys

def solve(N):
    # A simple strategy to query seats in a way that guarantees finding a vacant seat
    for i in range(N):
        print(i)
        sys.stdout.flush()
        response = input().strip()
        
        if response == "Vacant":
            return
    
    # If we reach here, something went wrong
    sys.exit(1)

def main():
    N = int(input())
    solve(N)

if __name__ == "__main__":
    main()
