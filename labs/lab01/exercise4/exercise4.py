# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        price = 2.0
    elif vehicle_type == "Hybrid":
        if hour <= 6 or hour >= 22:
            price = 2.0
        else:
            price = 5.0
    else:
        price = 5.0
    return price