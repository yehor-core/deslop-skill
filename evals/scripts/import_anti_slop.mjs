// Import valid/invalid TS snippets from dmmulroy/anti-slop (MIT) rule tests.
//
// Only rules that match a deslop pattern are taken. anti-slop is one author's
// opinionated ruleset, so "invalid" means "that author flags it"; deslop may
// reasonably disagree, and the eval runner treats these as soft expectations.
//
// Usage: node evals/scripts/import_anti_slop.mjs   (needs the gh CLI)

import { execFileSync } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const REPO = "dmmulroy/anti-slop";
const OUT = join(dirname(fileURLToPath(import.meta.url)), "..", "external", "anti-slop");

// anti-slop rule -> deslop pattern id
const RULES = {
  "no-chained-type-assertions": "T1",
  "no-widen-then-assert": "T1",
  "require-safety-comment-for-type-assertion": "T1",
  "no-reduce-accumulator-copy": "V3",
  "no-array-filter-map": "V3",
  "no-conditional-empty-object-spread": "V4",
  "no-module-mocking": "S1",
};

const gh = (...args) => execFileSync("gh", args, { encoding: "utf8" });

function extract(source) {
  const runs = [];
  // The test files are plain JS apart from their imports.
  const code = source.replace(/^import .*$/gm, "");
  const sandbox = {
    RuleTester: class {
      run(name, _rule, cases) {
        runs.push({ name, cases });
      }
    },
  };
  // Rule objects are imported identifiers; give every unknown name a harmless stub.
  const context = vm.createContext(new Proxy(sandbox, {
    has: () => true,
    get: (target, key) => (key in target ? target[key] : key in globalThis ? globalThis[key] : { meta: {} }),
  }));
  vm.runInContext(code, context);
  return runs;
}

const normalize = (c) => (typeof c === "string" ? { code: c } : { code: c.code, name: c.name, options: c.options });

const sha = gh("api", `repos/${REPO}/commits/HEAD`, "--jq", ".sha").trim();
const cases = [];
for (const [rule, pattern] of Object.entries(RULES)) {
  const source = Buffer.from(gh("api", `repos/${REPO}/contents/src/rules/${rule}.test.ts?ref=${sha}`, "--jq", ".content"), "base64").toString();
  for (const run of extract(source)) {
    for (const c of run.cases.valid ?? []) cases.push({ rule, pattern, kind: "clean", ...normalize(c) });
    for (const c of run.cases.invalid ?? []) cases.push({ rule, pattern, kind: "slop", ...normalize(c) });
  }
}

mkdirSync(OUT, { recursive: true });
const license = Buffer.from(gh("api", `repos/${REPO}/contents/LICENSE?ref=${sha}`, "--jq", ".content"), "base64").toString();
writeFileSync(join(OUT, "LICENSE"), license);
writeFileSync(
  join(OUT, "snippets.json"),
  JSON.stringify({ source: `https://github.com/${REPO}`, commit: sha, license: "MIT", note: "Opinionated upstream rules; treat kind as a soft expectation.", cases }, null, 2) + "\n",
);
console.log(`${cases.length} snippets -> ${OUT}`);
