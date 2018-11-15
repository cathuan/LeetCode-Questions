package main

// MyQueue is a Queue constructed with stacks
type MyQueue struct {
	inStack  []int
	outStack []int
}

// Constructor Initialize your data structure here.
func Constructor() MyQueue {
	myQueue := new(MyQueue)
	return *myQueue
}

// Push element x to the back of queue. */
func (myQueue *MyQueue) Push(x int) {
	myQueue.inStack = append(myQueue.inStack, x)
}

// Pop Removes the element from in front of queue and returns that element.
func (myQueue *MyQueue) Pop() int {
	if len(myQueue.outStack) == 0 {
		for i := len(myQueue.inStack) - 1; i >= 0; i = i - 1 {
			myQueue.outStack = append(myQueue.outStack, myQueue.inStack[i])
		}
		myQueue.inStack = []int{}
	}

	popedValue := myQueue.outStack[len(myQueue.outStack)-1]
	myQueue.outStack = myQueue.outStack[:len(myQueue.outStack)-1]
	return popedValue
}

// Peek Get the front element.
func (myQueue *MyQueue) Peek() int {
	if len(myQueue.outStack) == 0 {
		for i := len(myQueue.inStack) - 1; i >= 0; i = i - 1 {
			myQueue.outStack = append(myQueue.outStack, myQueue.inStack[i])
		}
		myQueue.inStack = []int{}
	}

	return myQueue.outStack[len(myQueue.outStack)-1]
}

// Empty Returns whether the queue is empty.
func (myQueue *MyQueue) Empty() bool {
	return len(myQueue.inStack)+len(myQueue.outStack) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
