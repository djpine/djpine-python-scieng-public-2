"""Calculates time, electrical energy used, and cost of electricity
for a trip in an electric vehicle"""

distance = float(input("Input trip distance (miles): "))

mpk = 3.9            # [miles/kilowatt-h] car mileage
speed = 60.          # [miles/h] average speed
cost_per_kWh = 0.22  # [$/kW-h] price of electricity

time = distance / speed       # [hours]
energy = distance / mpk       # [kW-h]
cost = energy * cost_per_kWh  # [$]

print("\nDuration of trip = {0:0.1f} hours".format(time))
print("Electricity used = {0:0.1f} kW-h (@ {1:0.2f} miles/kW-h)"
      .format(energy, mpk))
print("Cost of electricity = ${0:0.2f} (@ ${1:0.2f}/kW-h)"
      .format(cost, cost_per_kWh))
