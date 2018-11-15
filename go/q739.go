package main

func dailyTemperatures(T []int) []int {
	var stack []int
	var ret []int
	for i := 0; i < len(T); i = i + 1 {
		ret = append(ret, 0)
	}

	for i := 0; i < len(T); i = i + 1 {
		var j int
		for (len(stack) > 0) && (T[stack[len(stack)-1]] < T[i]) {
			j = stack[len(stack)-1]
			ret[j] = i - j
			stack = stack[:len(stack)-1]
		}

		stack = append(stack, i)
	}

	return ret
}
