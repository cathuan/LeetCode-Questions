package main

func parseTernary(expression string) string {
	var value string
	var opIndices []int
	var stack []string

	cur := ""
	for i, c := range expression {
		char := string(c)
		if char == "?" {
			stack = append(stack, cur)
			cur = ""
			opIndices = append(opIndices, len(stack)-1)
		} else if char == ":" {
			stack = append(stack, cur)
			cur = ""
		} else {
			cur = cur + char
		}

		if i == len(expression)-1 {
			stack = append(stack, cur)
		}

		if len(opIndices) == 0 {
			continue
		}

		for opIndex := opIndices[len(opIndices)-1]; opIndex+3 == len(stack); opIndex = opIndices[len(opIndices)-1] {
			if stack[opIndex] == "T" {
				value = stack[opIndex+1]
			} else {
				value = stack[opIndex+2]
			}
			stack = stack[:opIndex]
			stack = append(stack, value)

			opIndices = opIndices[:len(opIndices)-1]
			if len(opIndices) == 0 {
				break
			}
			opIndex = opIndices[len(opIndices)-1]
		}
	}
	return stack[0]
}

func process(stack []string, opIndices []int) {}

//func main() {
//	expression := "T?T?13:54:3"
//	fmt.Println(parseTernary(expression))
//}
