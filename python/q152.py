class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_products = []
        min_products = [Product()]
        max_products = [Product()]
        current_product = Product()

        for num in nums:
            current_product.multiply(num)
            current_products.append(current_product)

            if min_products[-1] > current_product:
                min_products.append(current_product)
            else:
                min_products.append(min_products[-1])

            if max_products[-1] < current_product:
                max_products.append(current_product)
            else:
                max_products.append(max_products[-1])

        min_products = min_products[:-1]
        max_products = max_products[:-1]

        print current_products
        print min_products
        print max_products

        max_value = None
        for i in range(len(nums)):

            current_max_value = max(current_products[i]/min_products[i], current_products[i]/max_products[i])
            if max_value is None:
                max_value = current_max_value
            else:
                max_value = max(current_max_value, max_value)
        return max_value


class Product(object):

    def __init__(self):

        self.value = 1
        self.contains_zero = False
        self.without_zero = 1

    def multiply(self, num):
        self.value *= num
        if num == 0:
            self.contains_zero = True
        else:
            self.without_zero *= num


if __name__ == "__main__":

    nums = [0, 2]
    solution = Solution()
    print solution.maxProduct(nums)
