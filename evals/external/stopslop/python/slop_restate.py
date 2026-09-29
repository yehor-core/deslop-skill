class HitCounter:
    def __init__(self):
        self.count = 0

    def record_hit(self):
        # increment the count
        self.count += 1

    def record_batch(self, n):
        self.count += n  # increment the count
