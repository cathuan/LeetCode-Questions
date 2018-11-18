package main

// StockSpanner is a struct
type StockSpanner struct {
	count   int
	prices  []int
	indices []int
}

//func Constructor() StockSpanner {
//	span := new(StockSpanner)
//	span.count = 1
//	return *span
//}

// Next get next
func (span *StockSpanner) Next(price int) int {
	for len(span.prices) > 0 {
		prevPrice := span.prices[len(span.prices)-1]
		if prevPrice <= price {
			span.prices = span.prices[:len(span.prices)-1]
			span.indices = span.indices[:len(span.indices)-1]
		} else {
			break
		}
	}

	var days int
	var preCount int
	if len(span.prices) == 0 {
		days = span.count
	} else {
		preCount = span.indices[len(span.indices)-1]
		days = span.count - preCount
	}

	span.prices = append(span.prices, price)
	span.indices = append(span.indices, span.count)
	span.count++
	return days
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
