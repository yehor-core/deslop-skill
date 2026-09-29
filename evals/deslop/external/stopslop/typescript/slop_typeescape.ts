interface Config {
  endpoint: string;
}

function loadRaw(): unknown {
  return {};
}

const data = loadRaw();
const x = data as any;

const raw = loadRaw();
const config = raw as unknown as Config;

function unsafeOp(): number {
  return 1;
}

// @ts-ignore
const result = unsafeOp();

function someFunc(n: number): number {
  return n;
}

// @ts-nocheck
const cfg = someFunc(1);
