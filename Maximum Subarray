/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
    let max_sum = -Infinity;
    let current_sum = 0;
    for(let i=0;i<nums.length;i++){
        current_sum = Math.max(nums[i],current_sum+nums[i])
        max_sum = Math.max(current_sum,max_sum)

    }
    return max_sum
};
// we use kedane's algorithm here
