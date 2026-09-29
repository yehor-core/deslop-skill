function risky(): void {}
function doWork(): void {}

function emptyCatch() {
  try {
    risky();
  } catch (e) {}
}

function logOnlyCatch() {
  try {
    doWork();
  } catch (err) {
    console.log(err);
  }
}

function commentOnlyCatch() {
  try {
    doWork();
  } catch (e) {
    // left blank
  }
}

function multiConsoleCatch() {
  try {
    doWork();
  } catch (e) {
    console.warn(e);
    console.error(e);
  }
}
