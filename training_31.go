package main

import "fmt"

// https://leetcode.com/problems/count-and-say/

// most efficient solution 0ms
// func countAndSay(n int) string {
// 	compressed := []byte{'1'}
// 	for range n - 1 {
// 		compressed = compress(compressed)
// 	}
// 	return string(compressed)
// }

// func compress(bytes []byte) []byte {
// 	count := byte(1)
// 	var ret []byte
// 	for i := range len(bytes) - 1 {
// 		if bytes[i] == bytes[i+1] {
// 			count++
// 		} else {
// 			ret = append(ret, '0'+count, bytes[i])
// 			count = 1
// 		}
// 	}
// 	ret = append(ret, '0'+count, bytes[len(bytes)-1])
// 	return ret
// }

func checkValue(s string) string {
	result := ""
	temp := ""
	curr_val := ""
	count := 0
	for i := 0; i < len(s); i++ {
		// if result is empty means it's first letter
		if temp == "" {
			temp += string(s[i])
			curr_val = string(s[i])
			count += 1
			continue
		}

		if curr_val != string(s[i]) {
			result += fmt.Sprintf("%d%s", count, temp)
			temp = string(s[i])
			count = 1
			curr_val = string(s[i])
			continue
		}

		// temp += string(s[i])
		count += 1
	}

	result += fmt.Sprintf("%d%s", count, temp)

	return result
}

func countAndSay(n int) string {
	temp := ""
	for i := 0; i < n; i++ {
		if i == 0 {
			temp = "1"
			continue
		}
		temp = checkValue(temp)
		fmt.Println(temp)
	}
	return temp
}
