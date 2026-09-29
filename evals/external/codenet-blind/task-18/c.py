import sys

def solve():
    n = int(sys.stdin.readline())

    # Binary search for an empty seat.
    # We leverage the property that adjacent seats have different sexes.
    # If we query seat `mid`, and it's occupied, we know the sex.
    # Based on the sex of `mid`, we can deduce the expected sex of `mid + 1`.
    # If `mid + 1` has the same sex as `mid`, it means there must be an empty seat
    # between `mid` and `mid + 1` (circularly).
    # Otherwise, if `mid + 1` has the opposite sex, the pattern continues.

    low = 0
    high = n - 1

    while True:
        mid = (low + high) // 2

        sys.stdout.write(str(mid) + "\n")
        sys.stdout.flush()
        response = sys.stdin.readline().strip()

        if response == "Vacant":
            return

        sex_mid = response

        # Determine the expected sex of the next seat
        if sex_mid == "Male":
            expected_sex_next = "Female"
        else: # sex_mid == "Female"
            expected_sex_next = "Male"

        # Query the next seat to check the pattern
        next_seat = (mid + 1) % n
        sys.stdout.write(str(next_seat) + "\n")
        sys.stdout.flush()
        response_next = sys.stdin.readline().strip()

        if response_next == "Vacant":
            return

        sex_next = response_next

        if sex_next == expected_sex_next:
            # Pattern holds, an empty seat must be in the other half
            if mid < n // 2: # If mid is in the first half
                low = mid + 1
            else: # If mid is in the second half
                high = mid - 1
        else:
            # Pattern broken, empty seat is between mid and next_seat
            # If sex_next is same as sex_mid, then the empty seat is at next_seat.
            # If sex_next is not as expected, the empty seat is at mid.
            # Since we already checked mid, if the pattern breaks, it must be at mid+1
            # (or rather, the next seat we query will reveal it).
            # Specifically, if sex_next is the same as sex_mid, the empty seat
            # must be at next_seat if it exists or somewhere before mid.
            # If sex_next is different but not the expected opposite, it implies
            # the break is between mid and next_seat.
            # Since N is odd, this implies the empty seat must be at `next_seat`.
            # Consider the parity of the difference.
            # If sex_mid == sex_next, the number of steps to get back to the same sex is 2.
            # The number of people between mid and next_seat (circularly) is odd.
            # If we query `mid` and `mid+1`, and `sex_mid == sex_next`, it implies that
            # the number of people between `mid` and `next_seat` is odd.
            # The state of seats `mid+2`, `mid+3`, ..., `next_seat-1` must alternate
            # such that an odd number of people are between `mid` and `next_seat`.
            # If `sex_mid` and `sex_next` are the same, it means the parity of occupied seats
            # between `mid` and `next_seat` is even (0 or 2).
            # Since the difference in indices `next_seat - mid = 1`, and we have an odd number of seats in total,
            # if `sex_mid == sex_next`, it implies an empty seat is in the range `mid+1` to `mid` (circularly).
            # The key is the difference in indices and the parity.
            # If `sex_mid` and `sex_next` are the same, and `next_seat = mid + 1`, then the effective
            # difference in indices is `mid - next_seat = -1` (modulo N).
            # Consider the segments:
            # If `sex_mid == sex_next`, it means the pattern `Male, Female, Male, Female...` or
            # `Female, Male, Female, Male...` is broken if `sex_mid` and `sex_next` are the same.
            # This means an empty seat must be at `next_seat`.
            if mid < n // 2:
                high = mid
            else:
                low = mid

        if low == high:
            sys.stdout.write(str(low) + "\n")
            sys.stdout.flush()
            response = sys.stdin.readline().strip()
            if response == "Vacant":
                return

solve()
```
