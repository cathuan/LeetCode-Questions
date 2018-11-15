package main

func nextGreaterElement(findNums []int, nums []int) []int {
	var stack []int
	buf := make(map[int]int)

	for _, num := range nums {
		// empty stack
		if len(stack) == 0 {
			stack = append(stack, num)
		} else {
			// pop extra numbers out of stack
			for (len(stack) > 0) && (stack[len(stack)-1] < num) {
				// pop the last element from the stack
				key := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				buf[key] = num
			}
			stack = append(stack, num)
		}
	}

	for len(stack) > 0 {
		key := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		buf[key] = -1
	}

	var ret []int
	for _, num := range findNums {
		ret = append(ret, buf[num])
	}

	return ret
}
