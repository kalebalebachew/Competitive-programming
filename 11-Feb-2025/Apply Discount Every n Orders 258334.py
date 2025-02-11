# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.a = n
        self.b = 0
        self.p = [0] * 201

        for i in range(len(products)):
            self.p[products[i]] = prices[i]

        self.dis = discount

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.b += 1

        bill = 0.0

        for i in range(len(product)):
            bill += (amount[i] * self.p[product[i]])

        if self.b != self.a:
            return bill

        bill = (bill) * ((100-self.dis)/100)  
        self.b = 0   
        return bill   
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)