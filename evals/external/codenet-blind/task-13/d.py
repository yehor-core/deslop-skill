from typing import List

def is_valid_bracket_sequence(s: str) -> bool:
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0

def solve(strings: List[str]) -> bool:
    open_count = sum(s.count('(') for s in strings)
    close_count = sum(s.count(')') for s in strings)
    
    if open_count != close_count:
        return False
    
    used = [False] * len(strings)
    open_surplus = 0
    
    def backtrack():
        nonlocal open_surplus
        
        if all(used):
            return open_surplus == 0
        
        for i in range(len(strings)):
            if not used[i]:
                used[i] = True
                current_open = strings[i].count('(') - strings[i].count(')')
                
                if open_surplus + current_open >= 0:
                    if backtrack():
                        return True
                
                used[i] = False
                open_surplus -= current_open
        
        return False
    
    return backtrack()

def main():
    N = int(input())
    strings = [input() for _ in range(N)]
    
    print('Yes' if solve(strings) else 'No')

if __name__ == '__main__':
    main()
