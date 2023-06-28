var ArrayWrapper = function(nums) {
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((acc, curr) => acc + curr, 0);
}

ArrayWrapper.prototype.toString = function() {
    return JSON.stringify(this.nums);
}
