package main

func scoreOfParentheses(S string) int {
	var bracketStack []string
	var scoreStack []int
	total := 0
	for _, c := range S {
		char := string(c)
		//fmt.Println(char, scoreStack, bracketStack)
		if char == "(" {
			bracketStack = append(bracketStack, string(c))
			for len(scoreStack) < len(bracketStack) {
				scoreStack = append(scoreStack, 0)
			}
		} else {
			// get ()
			if (len(bracketStack) > 0) && (bracketStack[len(bracketStack)-1] == "(") {
				if len(scoreStack) > len(bracketStack) {
					lastScore := scoreStack[len(scoreStack)-1]
					scoreStack = scoreStack[:len(scoreStack)-1]
					scoreStack[len(scoreStack)-1] = scoreStack[len(scoreStack)-1] + lastScore*2
				} else {
					scoreStack[len(scoreStack)-1] = scoreStack[len(scoreStack)-1] + 1
				}
				bracketStack = bracketStack[:len(bracketStack)-1]
			}
		}

		if (len(scoreStack) == 1) && (len(bracketStack) == 0) {
			total = total + scoreStack[0]
			scoreStack = []int{}
		}
	}
	for i := 0; i < len(scoreStack); i = i + 1 {
		total = total + scoreStack[i]
	}
	return total
}
