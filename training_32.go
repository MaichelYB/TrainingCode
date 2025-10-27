package main

// https://leetcode.com/problems/combination-sum/
func combinationSum(candidates []int, target int) [][]int {
	var result [][]int

	var backtrack func(int, []int, int)
	backtrack = func(start int, currentCombination []int, currentSum int) {
		if currentSum == target {
			combination := make([]int, len(currentCombination))
			copy(combination, currentCombination)
			result = append(result, combination)
			return
		}

		for i := start; i < len(candidates); i++ {
			if currentSum+candidates[i] > target {
				continue
			}

			currentCombination = append(currentCombination, candidates[i])
			backtrack(i, currentCombination, currentSum+candidates[i])
			currentCombination = currentCombination[:len(currentCombination)-1]
		}
	}

	backtrack(0, []int{}, 0)
	return result
}
