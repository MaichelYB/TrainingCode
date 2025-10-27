package main

import "sort"

// https://leetcode.com/problems/combination-sum-ii/submissions/1809440862/
func combinationSum2(candidates []int, target int) [][]int {
	var result [][]int

	// Sort the array to handle duplicates efficiently
	sort.Ints(candidates)

	var backtrack func(int, []int, int)
	backtrack = func(start int, current []int, sum int) {
		// Base case: found a valid combination
		if sum == target {
			temp := make([]int, len(current))
			copy(temp, current)
			result = append(result, temp)
			return
		}

		// Explore candidates
		for i := start; i < len(candidates); i++ {
			// Skip duplicates at the same level
			if i > start && candidates[i] == candidates[i-1] {
				continue
			}

			// Prune if sum exceeds target
			if sum+candidates[i] > target {
				break // Since array is sorted, no need to check further
			}

			// Choose current candidate
			current = append(current, candidates[i])

			// Explore: move to next index (i+1) since we can't reuse same element
			backtrack(i+1, current, sum+candidates[i])

			// Unchoose
			current = current[:len(current)-1]
		}
	}

	backtrack(0, []int{}, 0)
	return result
}
