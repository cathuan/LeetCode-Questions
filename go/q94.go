package main

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	var res []int
	return expand(root, res)
}

func expand(node *TreeNode, res []int) []int {
	if node != nil {
		res = expand(node.Left, res)
		res = append(res, node.Val)
		res = expand(node.Right, res)
	}
	return res
}
