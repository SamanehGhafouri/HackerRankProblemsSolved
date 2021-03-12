# Electronics shop
# A person wants to determine the most expensive computer
# keyboard and USB drive that can be purchased with a give
# budget. Given price lists for keyboards and USB drives and
# a budget, find the cost to buy them. If it is not possible
# to buy both items, return .


# Time complexity is o(n^2)
def get_money_spent(keyboards, drives, b):

    sum_of_items = [sum([i, j]) for i in keyboards for j in drives]
    return max([i for i in sum_of_items if i <= b] + [-1])


# Time complexity is o(n log n)
def get_money_spent_2(keyboards: list, usb_drives: list, budget: int):

    keyboards = [price for price in keyboards if price <= budget]
    if len(keyboards) == 0: return -1
    min_keyboard_price = min(keyboards)
    usb_drives = [price for price in usb_drives if price + min_keyboard_price <= budget]
    if len(usb_drives) == 0: return -1
    usb_drives.sort()

    purchase = -1
    for keyboard_price in keyboards:

        lo, hi = 0, len(usb_drives) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            current_purchase = keyboard_price + usb_drives[m]
            if purchase < current_purchase <= budget:
                purchase = max(purchase, current_purchase)
            if current_purchase > budget:
                hi = m - 1
            else:
                lo = m + 1
    return -1 if purchase > budget else purchase


bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
money_spent = get_money_spent(keyboards, drives, b)
print(money_spent)

money_spent_2 = get_money_spent_2(keyboards, drives, b)
print(money_spent_2)
