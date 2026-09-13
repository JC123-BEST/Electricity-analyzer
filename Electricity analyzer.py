days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while True:
    readings = input("Enter the readings for 7 days: ")
    readings_list = readings.split()
    if len(readings_list) != 7:
       continue
    integer_readings = []
    valid = True
    for reading in readings_list:
        try:
            new_value = int(reading)
            if new_value < 0:
                valid = False
            else:
                integer_readings.append(new_value)
        except ValueError:
            valid = False
    if not valid:
        continue
    total = 0
    for reading in integer_readings:
        total += reading
    average = total / len(integer_readings)
    highest_value = 0
    highest_index = 0
    for index, reading in enumerate(integer_readings):
        if reading > highest_value:
            highest_value = reading
            highest_index =  index
    highest_day = days[highest_index]
    lowest_value = integer_readings[0]
    lowest_index = 0
    for index, reading in enumerate(integer_readings):
        if reading < lowest_value:
            lowest_value = reading
            lowest_index =  index
    lowest_day = days[lowest_index]
    above_average_days = []
    for index, reading in enumerate(integer_readings):
        if reading > average:
            above_average_days.append(days[index])
    print(f"total consumption: {total}")
    print(f"Average: {average}")
    print(f"highest_day: {highest_day}")
    print(f"highest consumption: {highest_value}")
    print(f"Lowest day: {lowest_day}")
    print(f"lowest consumption: {lowest_value}")
    print(f"Above average days: {above_average_days}")
    break

