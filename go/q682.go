package main

import (
	"strconv"
)

func calPoints(ops []string) int {
	var scores []int

	for _, op := range ops {
		if op == "C" {
			scores = scores[:len(scores)-1]
		} else if op == "D" {
			prevValidScore := scores[len(scores)-1]
			scores = append(scores, 2*prevValidScore)
		} else if op == "+" {
			prevValidScore1 := scores[len(scores)-1]
			prevValidScore2 := scores[len(scores)-2]
			scores = append(scores, prevValidScore1+prevValidScore2)
		} else {
			i, _ := strconv.Atoi(op)
			scores = append(scores, i)
		}
	}

	score := 0
	for _, s := range scores {
		score = score + s
	}

	return score
}
