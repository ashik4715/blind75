// leetcode 238
// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
// The problem can be solved in O(n) time complexity and O(1) space complexity.
// We can use two arrays to keep track of the product of all elements to the left and right of each element.
// Then we can multiply the two arrays together to get the final result.
// The time complexity is O(n) because we are iterating through the array twice, and the space complexity is O(1) because we are using a fixed amount of space for the two arrays.
// We can also solve this problem in O(n) time complexity and O(1) space complexity by using a single array to keep track of the product of all elements to the left of each element.
// Then we can iterate through the array again to get the product of all elements to the right of each element and multiply it with the product of all elements to the left of each element.
// The time complexity is O(n) because we are iterating through the array twice, and the space complexity is O(1) because we are using a fixed amount of space for the single array.
// The final result will be stored in the same array.

pub fn product_except_self(nums: Vec<i32>) -> Vec<i32>{
    let n = nums.len();
    let mut result = vec![1; n];
    let mut left_product = 1;
    let mut right_product = 1;

    for i in 0..n {
        result[i] *= left_product;
        left_product *= nums[i];
    }

    for i in (0..n).rev() {
        result[i] *= right_product;
        right_product *= nums[i];
    }

    result
}

// Test cases
fn main() {
    println!("{:?}", product_except_self(vec![1, 2, 3, 4])); // [24, 12, 8, 6]
    println!("{:?}", product_except_self(vec![-1, 1, 0, 3, -3])); // [0, 0, 0, 0, 0]
    println!("{:?}", product_except_self(vec![0, 0])); // [0, 0]
    println!("{:?}", product_except_self(vec![1, 2, 3, 4, 5])); // [120, 60, 40, 30, 24]
    println!("{:?}", product_except_self(vec![1, 1, 1, 1])); // [1, 1, 1, 1]
}
