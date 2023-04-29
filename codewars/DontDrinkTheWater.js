function separateLiquids(glass) {
  
  const DENSITY = {
    'H': 1.36,
    'W': 1.00,
    'A': 0.87,
    'O': 0.80,
  };
  
  if (!glass.length) return [];
  
  const flattedGlass = flatGlass(glass);
  const sortedFlattedGlass = flattedGlass.sort((a, b) => DENSITY[a] - DENSITY[b]);
  const sortedGlass = madeGlass(sortedFlattedGlass, glass[0].length);
  
  return sortedGlass;
}

function madeGlass(sortedFlattedGlass, size) {
  const sortedGlass = [];
  
  let temp = [];
  let k = 0;

  for (let i = 0; i <= sortedFlattedGlass.length; i++) {
    if (k < size) {
      temp.push(sortedFlattedGlass[i]);
      k++;
    } else {
      sortedGlass.push(temp);
      temp = [sortedFlattedGlass[i]];
      k = 1
    }
  }
  
  return sortedGlass;
}

function flatGlass(glass) {
  const flatted = [];
  
  for (let i = 0; i < glass.length; i++) {
    for (let k = 0; k < glass[i].length; k++) {
      flatted.push(glass[i][k]);
    }
  }
  
  return flatted;
}
