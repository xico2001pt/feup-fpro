"""
Write a Python function budgeting(budget, products, wishlist) that, given an integer budget, products and purchases that a buyer intends to do (wishlist), checks if the budget is not exceeded, making the appropriate adjustments, if needed. The argument products is a dictionary where each key is the product name and the value is the price (per unit); the wishlist is a dictionary where each key is the product name and the value the quantity desired.

Due to lack of attention, the buyer might have wanted more than he could afford. The function should uncover these cases and calculate what products should have their desired quantity lowered (or even be removed) in order to reduce the total amount to fit the budget. Examine products with lower price first. The function should return the updated wishlist.

"""

def budgeting(budget, products, wishlist):
    result = {}
    cost = 0
    def order(item):
        return products[item[0]]
    
    sorted_wishlist = sorted(list(wishlist.items()), key=order, reverse=True)
    for product, quant in sorted_wishlist:
        for _ in range(quant):
            cost += products[product]
            if cost <= budget:
                result[product] = result.get(product, 0) + 1
    return result