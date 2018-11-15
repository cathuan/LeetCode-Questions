package main

// MyStack is a stack implemented by Queue
type MyStack struct {
	queue []int
}

// Constructor Initialize your data structure here.
func Constructor() MyStack {
	stack := new(MyStack)
	return *stack
}

// Push element x onto stack.
func (stack *MyStack) Push(x int) {
	originalLength := len(stack.queue)
	stack.queue = append(stack.queue, x)
	for i := 0; i < originalLength; i = i + 1 {
		var x int
		x, stack.queue = stack.queue[0], stack.queue[1:]
		stack.queue = append(stack.queue, x)
	}
}

// Pop Removes the element on top of the stack and returns that element.
func (stack *MyStack) Pop() int {
	var x int
	x, stack.queue = stack.queue[0], stack.queue[1:]
	return x
}

// Top Get the top element.
func (stack *MyStack) Top() int {
	return stack.queue[0]
}

// Empty Returns whether the stack is empty.
func (stack *MyStack) Empty() bool {
	return len(stack.queue) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
