/**
 * @return {number}
 */
var argumentsLength = function (...args) {
  let counter = 0;

  while (args[counter] !== undefined) counter += 1;

  return counter;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
console.log(argumentsLength(1, 2, 3));
