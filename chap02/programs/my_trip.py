"""Calculates time, electrical energy used, and cost of electricity
for a trip in an electric vehicle"""
# Get inputs
distance = 180.      # [miles]
mpk = 3.9            # [miles/kilowatt-h] car mileage
speed = 60.          # [miles/h] average speed
cost_per_kWh = 0.22  # [$/kW-h] price of electricity

# Calculate outputs
time = distance / speed       # [hours]
energy = distance / mpk       # [kW-h]
cost = energy * cost_per_kWh  # [$]
