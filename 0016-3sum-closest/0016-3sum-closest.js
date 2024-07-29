/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b);  // sort the input array in ascending order
    let closestSum = Infinity;   // initialize closestSum to be maximum integer value
    const n = nums.length;       // store the length of the input array
    
    for (let i = 0; i < n - 2; i++) {
        let j = i + 1, k = n - 1;
        
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            
            if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
                closestSum = sum;
            }
            
            if (sum < target) {
                j++;
            } else if (sum > target) {
                k--;
            } else {
                return target;
            }
        }
    }
    
    return closestSum;
};
