class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        new_prices = prices[:]

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                new_prices[idx] -= price
            stack.append(i)

        return new_prices
    

sol = Solution()

inp = [
    [8,4,6,2,3],
    [1,2,3,4,5],
    [10,1,1,6]
]

for arr in inp:
    print(f"Final prices of the items will be {arr} : ", sol.finalPrices(arr))