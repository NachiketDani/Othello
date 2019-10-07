import sys


def main():

    PUMPON_THRESHOLD = 800
    pump_on_min = 0
    data_count = 0
    water_vol = 0
    pump_poweruse = 0
    power_cost = 0
    gal5_min = -1
    gal100_min = -1

    # filename = input("Filename for pump power consumption data:")
    input_file = input("Please enter the file name: ")
    try:
        pump_data = open(input_file, "r")
    except:
        print("Unable to open", input_file)
        return

    for lines in pump_data:
        power_atmin = int(lines.rstrip())
        data_count += 1
        pump_poweruse += power_atmin
        if power_atmin >= PUMPON_THRESHOLD:
            pump_on_min += 1

        # Following code determines time needed to reach 5 and 100 gallons
        if pump_on_min == 3:
            gal5_min = data_count
        if pump_on_min == 50:
            gal100_min = data_count

    water_vol = pump_on_min * 2
    power_cost = pump_poweruse/60

    print("Data covers a total of", data_count/60, "hours")
    print("(That's", data_count/1440, "days)\n\n")

    print("Pump was running for", pump_on_min, "minutes, producing", water_vol, "gallons")
    print("(That's", (pump_on_min/1440), "gallons per day)\n\n")

    print("Pump required a total of", pump_poweruse, "watt minutes of power")
    print("That's", round(pump_poweruse/60000, data_count), "kWh\n\n")

    print("It took", gal5_min, "minutes of data to reach 5 gallons.")
    print("It took", gal100_min, "minutes of data to reach 100 gallons.")

# EXTRA CREDIT WORK
    softner_check = 0
    time_rec = 0
    softner_log = []


def softner_logic():
    """CODE IS REPEATED AND NEEDS TO BE DELETED FROM HERE TILL "!!!!!" """
    for lines in pump_data:
        power_atmin = int(lines.rstrip())
        data_count += 1
        pump_poweruse += power_atmin
        if power_atmin >= PUMPON_THRESHOLD:
            pump_on_min += 1
    """DEL CODE TILL HERE !!!!!"""
            softner_check = True
                



main()
