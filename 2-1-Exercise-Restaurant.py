'''
Exercise: Restaurant

    Create a dict, called menu, in which the keys are names of items sold at a restaurant, and the values are the prices.
    Define a variable total, which has a value of 0.
    Ask the user repeatedly what they want to order.
        If they enter an empty string, stop asking and print the total
        If they enter something on the menu (i.e., a key in menu), then print the item, its price, and the current total (after adding this item to the total)
        If they enter something not on the menu, then scold them
    Print the total

Example:

Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order
'''

#mycode
menu = {'sandwich':10, 'tea':7}
total = 0

while True:
    order = input('Order:').strip()
    if order in menu:
        total =+ menu[order]
        print(order + ' costs' + menu[order] + ' total is ')
        continue
    else:
        break
    
'''
SOLUTION:

menu = {'sandwich':10, 'tea':7, 'apple':3}
total = 0

while True:
    order = input('Order: ').strip()
    
    if not order:  # if I get an empty string, break from the loop
        break

    if order in menu:
        price = menu[order]
        total += price
        print(f'{order} costs {price}, total is now {total}.')
    else:
        print(f'We are out of {order} today!')
        
print(f'total = {total}')
'''