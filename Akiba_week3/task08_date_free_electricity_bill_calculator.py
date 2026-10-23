def validate_the_unit_consumed(unit):
  if unit < 0:

    return "invalid because consumption cannot be negative"
  
  if not unit.replace(".", "", 1).isdigit():

    return "invalid because it is not numerical quantity"
  
  return "valid"

def calculate_the_charge_for_each_tier(unit):
  charge=0
  for i in range(1,unit+1):
    if i<=50:
      charge += 0.50
    if 50 < i<=150:
      charge += 0.75
    if i >150:
      charge += 1.20
  return charge
def calculate_the_total_bill(unit):
  electricitycharge=calculate_the_charge_for_each_tier(unit)
  servicefee=10
  total_bill=electricitycharge + servicefee
  return total_bill

def generate_billing_summary(unit):
    electricity_charge = calculate_the_charge_for_each_tier(unit)
    total_bill = calculate_the_total_bill(unit)

    print("===== ELECTRICITY BILL =====")
    print(f"Units consumed: {unit}")
    print(f"Electricity charge: {electricity_charge:.2f} Birr")
    print(f"Service fee: 10.00 Birr")
    print(f"Total bill: {total_bill:.2f} Birr")
generate_billing_summary(200)
