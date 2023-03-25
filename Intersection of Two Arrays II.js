/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
function intersect(nums1, nums2) {
  const map = new Map();
  for (const num of nums1) {
    map.set(num, (map.get(num) || 0) + 1);
  }
  const result = [];
  for (const num of nums2) {
    if (map.get(num) > 0) {
      result.push(num);
      map.set(num, map.get(num) - 1);
    }
  }
  return result;
}
