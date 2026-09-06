product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class prod:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

prod1 = prod("codetree", 50)
prod2 = prod(product_name, product_code)

print("product", prod1.product_code, "is", prod1.product_name)
print("product", prod2.product_code, "is", prod2.product_name)