function risky(): void {}
function doWork(): void {}

function EmptyCatch() {
  try {
    risky();
  } catch (e) {}
  return null;
}

function LogOnlyCatch() {
  try {
    doWork();
  } catch (err) {
    console.error(err);
  }
  return null;
}
