function twoSum(nums, target) {
  const seen = {};

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;

    if (seen.hasOwnProperty(diff)) {
      return [seen[diff], i];
    }

    seen[num] = i;
  }
}
console.log(twoSum([3, 7, 4], 10)); 
