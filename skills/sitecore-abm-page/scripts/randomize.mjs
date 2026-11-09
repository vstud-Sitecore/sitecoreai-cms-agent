// Cross-platform naming draws using Node built-ins only.
import { randomInt } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const skillDirectory = path.dirname(fileURLToPath(import.meta.url));
function randomize(input) {
  const hasWords = Array.isArray(input.eligible);
  const hasNames = Array.isArray(input.candidates);
  if (hasWords === hasNames) throw new Error('Provide either eligible words or candidates');
  if (hasWords) {
    const bank = JSON.parse(fs.readFileSync(path.join(skillDirectory, '../references/word-bank.json'), 'utf8'));
    const allowed = new Set(Object.values(bank).flat());
    const eligible = [...new Set(input.eligible.map(word => word.toLowerCase()))];
    if (!eligible.every(word => allowed.has(word))) throw new Error('Eligible words must come from references/word-bank.json');
    const count = input.count === undefined ? 3 : input.count;
    if (!Number.isInteger(count) || count < 1 || count > eligible.length) throw new Error('Count must be between one and the number of distinct eligible words');
    const words = [];
    while (words.length < count) words.push(eligible.splice(randomInt(eligible.length), 1)[0]);
    return { words };
  }
  const candidates = [...new Set(input.candidates)];
  if (new Set(candidates.map(name => name.toLowerCase())).size < 2) throw new Error('Provide at least two distinct valid names');
  for (const name of candidates) {
    if (!/^[A-Za-z]+(?: [A-Za-z]+)*$/.test(name) || name.split(' ').length < 4 || name.split(' ').length > 8) throw new Error('Each candidate must contain four to eight words using letters and single spaces');
  }
  return { name: candidates[randomInt(candidates.length)] };
}
export { randomize };
export default { randomize };
if (typeof process !== "undefined" && process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url) {
  try {
    const args = process.argv.slice(2);
    const input = {};
    for (let i = 0; i < args.length;) {
      const flag = args[i++];
      if (flag === '--count') { input.count = Number(args[i++]); continue; }
      if (flag !== '--eligible' && flag !== '--candidates') throw new Error('Unknown option: ' + flag);
      const values = [];
      while (i < args.length && !args[i].startsWith('--')) values.push(args[i++]);
      input[flag.slice(2)] = values;
    }
    console.log(JSON.stringify(randomize(input)));
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
