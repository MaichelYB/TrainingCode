package main

import (
	"fmt"
	"sort"
)

// other solution
func nextPermutation(nums []int) {
	/*
	   [0,4,7,6,3,2]
	   find the number from where asc sequence break from right to left
	   find the next highest from the number where asc sequqnce breaks
	   [0,(4),7,(6),3,2]
	   replace
	   [0,(6),7,(4),3,2]
	   sort the array from the next of left replaced number till the end
	   [0,6,2,3,4,7]
	*/
	var index_one int
	num_size := len(nums)
	next_big := 101
	min_index := num_size - 1
	for i := num_size - 2; i >= 0; i-- {

		if nums[i] < nums[i+1] {
			index_one = i
			break
		}
	}

	for i := num_size - 1; i > index_one; i-- {
		if nums[index_one] < nums[i] {
			if next_big > nums[i] {
				next_big = nums[i]
				min_index = i
			}
		}
	}
	temp := nums[index_one]
	nums[index_one] = nums[min_index]
	nums[min_index] = temp
	fmt.Println(nums)
	sort.Slice(nums[index_one+1:], func(i, j int) bool {
		return nums[index_one+1+i] < nums[index_one+1+j]
	})
	fmt.Println(nums)
}

// my solution
func nextPermutationMine(nums []int) {
	// Step 1: Find the first decreasing element from the end
	i := len(nums) - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}

	// Step 2: Find the smallest element larger than nums[i] to swap
	if i >= 0 {
		j := len(nums) - 1
		for j > i && nums[j] <= nums[i] {
			j--
		}
		nums[i], nums[j] = nums[j], nums[i]
	}

	// Step 3: Reverse the suffix
	left, right := i+1, len(nums)-1
	for left < right {
		nums[left], nums[right] = nums[right], nums[left]
		left++
		right--
	}
}
