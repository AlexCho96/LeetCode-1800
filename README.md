# LeetCode - 1800. Maximum Ascending Subarray Sum

## Statement
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [ nums_{l}, nums_{l+1}, ..., nums_{r-1}, nums_{r} ] is ascending if for all i where l <= i < r, nums_{i}  < nums_{i+1}. Note that a subarray of size 1 is ascending.


### Example 1
> **Input**: nums = [10,20,30,5,10,50] <br>
**Output**: 65 <br>
**Explanation**: [5,10,50] is the ascending subarray with the maximum sum of 65.

### Example 2
> **Input**: nums = [10,20,30,40,50] <br>
**Output**: 150 <br>
**Explanation**: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

### Example 3
> **Input**: nums = [12,17,15,13,10,11,12] <br>
**Output**: 33 <br>
**Explanation**: [10,11,12] is the ascending subarray with the maximum sum of 33.