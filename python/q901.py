class StockSpanner(object):
    def __init__(self):
        self.prices = []
        self.count = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while self.prices:
            prevPrice, _ = self.prices[-1]
            if prevPrice <= price:
                self.prices.pop()
            else:
                break

        if not self.prices:
            days = self.count
        else:
            _, prevCount = self.prices[-1]
            days = self.count - prevCount
        self.prices.append((price, self.count))
        self.count += 1
        return days


if __name__ == "__main__":

    span = StockSpanner()
    for price in [100, 80, 60, 70, 60, 75, 85]:
        print span.next(price)