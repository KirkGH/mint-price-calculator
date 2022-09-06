mint_price = input("Enter mint price: ")
int_mint_price = int(mint_price)

max_priority_fee = input("Enter minimum priority fee: ")
int_max_priority_fee = int(max_priority_fee) * .000000001

max_gas_fee = input("Enter max gas fee: ")
int_max_gas_fee = int(max_gas_fee) * .000000001

gas_limit = input("Enter gas limit: ")
int_gas_limit = int(gas_limit)

min_pay = int_max_priority_fee * int_gas_limit + int_mint_price
max_pay = int_max_gas_fee * int_gas_limit + int_mint_price

print("Min: " + str(min_pay))
print("Max: " + str(max_pay))