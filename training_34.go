package main

import (
	"fmt"
	"strings"
)

func multiply(num1 string, num2 string) string {
	// Handle edge case: if either number is "0", result is "0"
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	m, n := len(num1), len(num2)
	// Result can have at most m + n digits
	result := make([]int, m+n)

	// Multiply each digit and add to result
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			// Convert chars to integers
			digit1 := int(num1[i] - '0')
			fmt.Println(digit1)
			digit2 := int(num2[j] - '0')
			fmt.Println(digit2)

			// Multiply and add to current position
			product := digit1 * digit2
			pos1, pos2 := i+j, i+j+1

			// Add to existing value and handle carry
			sum := product + result[pos2]
			result[pos2] = sum % 10
			result[pos1] += sum / 10
		}
	}

	// Convert result to string, skipping leading zeros
	var sb strings.Builder
	for i := 0; i < len(result); i++ {
		// Skip leading zeros
		if sb.Len() == 0 && result[i] == 0 {
			continue
		}
		sb.WriteByte(byte(result[i] + '0'))
	}

	// If result is empty, return "0" (shouldn't happen due to edge case check)
	if sb.Len() == 0 {
		return "0"
	}

	return sb.String()
}
