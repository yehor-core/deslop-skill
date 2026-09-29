import sys

def solve(N, A):
    # Sort the array in descending order
    A.sort(reverse=True)
    
    # Keep track of the maximum possible result and operations
    max_result = float('-inf')
    best_operations = []
    
    # Try different starting subtraction orders
    for start_idx in range(N):
        # Make a copy of the original array to modify
        B = A.copy()
        operations = []
        
        # Simulate the subtraction process starting with different initial elements
        current_idx = start_idx
        while len(B) > 1:
            # Find the next largest and next smallest elements to subtract
            max_val = max(B)
            min_val = min(B)
            
            max_pos = B.index(max_val)
            min_pos = B.index(min_val)
            
            # Remove both elements and add their difference
            B.pop(max_pos)
            B.pop(min_pos if min_pos < max_pos else min_pos - 1)
            B.append(max_val - min_val)
            
            # Record the operation
            operations.append((max_val, min_val))
        
        # Update max result if needed
        if B[0] > max_result:
            max_result = B[0]
            best_operations = operations
    
    return max_result, best_operations

def main():
    # Read input
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Solve problem
    result, operations = solve(N, A)
    
    # Print output
    print(result)
    for x, y in operations:
        print(f"{x} {y}")

if __name__ == "__main__":
    main()
