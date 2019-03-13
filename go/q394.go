package main

import (
	"fmt"
	"strconv"
)

// IsNumeric is a method used to determine whether a string is numeric
func IsNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func decodeString(s string) string {
	var stack []string
	cur := ""
	for i, c := range s {
		char := string(c)
		if char == "[" {
			stack = append(stack, cur)
			cur = "["
		} else if char == "]" {
			cur = cur + "]"
			stack = append(stack, cur)
			cur = ""
		} else {
			cur = cur + char
		}

		if i == len(s)-1 {
			stack = append(stack, cur)
		}
	}

	return s
}

func main() {
	s := "2[abc]3[cd]ef"
	ret := decodeString(s)
	fmt.Println(ret)
}
