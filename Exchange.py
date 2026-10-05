amount=float(input("Amount of money in USD:  "))
USD=150
rate=float(input("what is the exchange rate ?: "))
converter1=amount*USD
converter2= amount*rate
print("="*45)
print("       CURRENCY EXCHANGE")
print("="*45)
print(f" USD Amount: {amount}")
print(f" Exchange Rate1: 1 USD ={USD} ETB")
print(f" Exchange Rate2: 1 USD ={rate}ETB")
print(f" ETB Amount1: {converter1}")
print(f" ETB Amount2: {converter2}")
print("="*45)

