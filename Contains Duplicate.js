/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let kaleb = new Set();
    for(let i=0;i<nums.length;i++){
        if(kaleb.has(nums[i])){
            return true;
        }
       kaleb.add(nums[i]) ;
    } 
     return false;
    /*console.log(containsDuplicate([1,2,3,1])) 
    console.log(containsDuplicate([1,2,3,4])) 
    console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) */
     
};
