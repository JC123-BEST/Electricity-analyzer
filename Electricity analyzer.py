while True:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    readings = input("Enter the readings for 7 days: ")
    readings_list = readings.split()
    if len(readings_list) != 7:
       continue
    else:
        valid = True
        integer_readings = []
        for reading in readings_list:
            try:
                new_value = int(reading)
                if new_value < 0:
                    valid = False
                else:
                    integer_readings.append(new_value)
            except ValueError:
                valid = False
        if valid == False:
            continue
        else:

            print(integer_readings)
        break