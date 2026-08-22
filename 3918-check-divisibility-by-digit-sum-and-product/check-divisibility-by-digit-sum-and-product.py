class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n 
        total = 0 
        product = 1

        while n > 0:
            digit = n % 10
            n //= 10
            total += digit
            product *= digit
            

        return temp %(total + product) == 0
        

        