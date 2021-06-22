/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var findKthLargest = function(nums, k) {
    var nums = new Float64Array(nums)
    // console.log(nums)
    nums.sort()
    // nums.sort((a, b) => a - b)
    return nums[nums.length - k]
};
