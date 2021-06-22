class Solution {

/**
 * @param Integer[] $nums
 * @param Integer $k
 * @return Integer
 */
function findKthLargest($nums, $k) {
    sort($nums);
    return $nums[count($nums) - $k];
}
}