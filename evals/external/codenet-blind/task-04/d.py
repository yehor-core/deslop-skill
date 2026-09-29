import sys

def solve(L):
    mod = 10**9 + 7
    ans = 0
    
    for k in range(L.bit_length()):
        # Count complete blocks
        block_size = 1 << (k + 1)
        complete_blocks = L // block_size
        ans += complete_blocks * (1 << k)
        
        # Handle remaining partial block
        remainder = L % block_size
        if remainder > (1 << k):
            ans += remainder - (1 << k)
    
    return ans % mod

def main():
    L = int(sys.stdin.readline().strip())
    print(solve(L))

if __name__ == "__main__":
    main()
