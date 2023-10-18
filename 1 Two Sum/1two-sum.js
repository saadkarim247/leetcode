/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    var hashmap = {};
    for (var i = 0; i < nums.length; i++) {
        var result = (target - nums[i]).toString();
        if (result in hashmap) {
            return [parseInt(hashmap[result]), i]
        } else {
            hashmap[nums[i]] = i
        }
    }
};
