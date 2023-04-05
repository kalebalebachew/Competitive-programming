/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);  // sort the input array in ascending order
    const result = [];           // initialize the result array
    const n = nums.length;       // store the length of the input array
    
    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue;  // skip over duplicate i
        
        let j = i + 1, k = n - 1;
        
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];
            
            if (sum === 0) {
                result.push([nums[i], nums[j], nums[k]]);
                while (j < k && nums[j] === nums[j+1]) j++;  // skip over duplicate j
                while (j < k && nums[k] === nums[k-1]) k--;  // skip over duplicate k
                j++;
                k--;
            } else if (sum < 0) {
                j++;
            } else {
                k--;
            }
        }
    }
    
    return result;
};
