function toUnderscore(string) {
  if (!string.length) {
    return String(string);
  }

  const result = [string[0].toLowerCase()];

  for (let i = 1; i < string.length; i++) {
    const s = string[i];

    if (s == s.toUpperCase() && isNaN(s)) {
      result.push("_");
      result.push(s.toLowerCase());
    } else {
      result.push(s);
    }
  }

  return result.join("");
}

console.log(toUnderscore("TestController"));
