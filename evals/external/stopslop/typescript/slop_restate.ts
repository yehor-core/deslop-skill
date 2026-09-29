class HitCounter {
  count = 0;

  recordHit(): void {
    // increment the count
    this.count += 1;
  }

  recordBatch(n: number): void {
    this.count += n; // increment the count
  }
}
