package main

// TreeNode Definition for a binary tree node.

func inorderTraversal(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode

	curNode := root
	for (curNode != nil) || (len(stack) > 0) {
		for curNode != nil {
			stack = append(stack, curNode)
			curNode = curNode.Left
		}

		curNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, curNode.Val)
		curNode = curNode.Right
	}
	return res
}
