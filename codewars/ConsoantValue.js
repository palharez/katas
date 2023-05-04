const ALPHABET = {
  b: 2,
  c: 3,
  d: 4,
  f: 6,
  g: 7,
  h: 8,
  j: 10,
  k: 11,
  l: 12,
  m: 13,
  n: 14,
  p: 16,
  q: 17,
  r: 18,
  s: 19,
  t: 20,
  v: 22,
  w: 23,
  x: 24,
  y: 25,
  z: 26,
};

const IGNORE = {
  a: 0,
  e: 0,
  i: 0,
  o: 0,
  u: 0,
};

function solve(str) {
  let value = 0;

  let sub = [];

  for (let i = 0; i <= str.length; i++) {
    const s = str[i];

    if (s in IGNORE || i == str.length) {
      const newValue = calculateValue(sub);
      value = newValue > value ? newValue : value;
      sub = [];
    } else {
      sub.push(s);
    }
  }

  return value;
}

const calculateValue = (sub) => {
  let value = 0;

  for (const s of sub) {
    if (s in ALPHABET) {
      value += ALPHABET[s];
    }
  }

  return value;
};
