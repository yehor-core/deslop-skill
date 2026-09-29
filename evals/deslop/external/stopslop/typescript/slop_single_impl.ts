interface Storage {
  get(key: string): string;
}

class MemoryStorage implements Storage {
  get(key: string): string {
    return key;
  }
}

abstract class Handler {
  abstract handle(): void;
}

class DefaultHandler extends Handler {
  handle(): void {}
}
