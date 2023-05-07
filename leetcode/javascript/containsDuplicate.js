/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const contains = {};

  for (const num of nums) {
    if (num in contains) {
      return true;
    }

    contains[num] = true;
  }

  return false;
};

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), true);
