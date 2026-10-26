def time_string(hours, minutes, time_format):
    if minutes < 10:
        minutes = "0" + str(minutes)

    if time_format == 24:
        string = str(hours) + ":" + str(minutes)
    elif time_format == 12:
        hours = abs(hours - 12)

        if hours == 0:
            hours = 00
            print("t")
        
        string = str(hours) + ":" + str(minutes)

    return string

hours = int(input("Input hours: "))
minutes = int(input("Input minutes: "))
time_format = int(input("Input time format (24/12): "))

print(time_string(hours, minutes, time_format))