
print('Welcome to tip calculator!')
bill_total = float(input('What was the total of the bill? $'))
tip_amount = float(input('How percent would you like to tip? %'))
bill_split = float(input('How many ways to split the bill? '))

after_split = bill_total / bill_split
after_tip = tip_amount / 100
new_total = after_split + (after_split * after_tip)
print(f'you will share the pay of ${round(new_total, 21)}')

