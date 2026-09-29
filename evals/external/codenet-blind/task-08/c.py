import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

def get_common_divisors(a, b):
    common_divs = []
    sqrt_gcd = int(math.sqrt(gcd(a, b)))
    
    for d in range(1, sqrt_gcd + 1):
        if gcd(a, b) % d == 0:
            common_divs.append(d)
            if d != gcd(a, b) // d:
                common_divs.append(gcd(a, b) // d)
    
    return sorted(common_divs)

def max_coprime_divisors(a, b):
    common_divs = get_common_divisors(a, b)
    max_divisors = []
    
    for div in common_divs:
        is_coprime = True
        for chosen_div in max_divisors:
            if not are_coprime(div, chosen_div):
                is_coprime = False
                break
        
        if is_coprime:
            max_divisors.append(div)
    
    return len(max_divisors)

def main():
    a, b = map(int, input().split())
    result = max_coprime_divisors(a, b)
    print(result)

if __name__ == "__main__":
    main()
