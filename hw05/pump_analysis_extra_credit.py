import sys


def main():
    # List of constants and variables in use
    COST_KWDOLLAR = 0.11        # Cost per 1 kW is 11 cents
    WATERPERKW = 2              # Water pumps @rate of 2gal/min if pump is on
    GALLON5_MIN = 3             # Pumps 5 gal in 3 min @rate of 2gal/min
    GALLON100_MIN = 50          # Pumps 100 gal in 50 min @rate of 2gal/min
    MININHOURS = 60             # 60 minutes in 1 hour
    MININDAY = 1440             # 1440 minutes in 1 day
    KWH_WMIN = 60000            # Watt-min to kWh conversion rate (1000*60)
    PUMPON_THRESHOLD = 500      # Minimum power value for pump to be ON
    SOFTNER_THRESHOLD = 120
    pump_onmin_total = 0
    totalmin_count = 0
    water_vol = 0
    pump_poweruse = 0
    power_cost = 0
    gal5_min = -1
    gal100_min = -1
    pump_on_softner = 0
    softner_pumpduration = []
    softner_runstart = []

    # Code for receiving filename from user; exception handling
    input_file = input("Please enter the file name: ")
    try:
        pump_data = open(input_file, "r")
    except:
        print("Unable to open", input_file)
        return

    # Code for each line of data, check for pump is on and softner recharge
    for lines in pump_data:
        power_atmin = int(lines.rstrip())
        totalmin_count += 1
        pump_poweruse += power_atmin
        if power_atmin >= PUMPON_THRESHOLD:
            pump_onmin_total += 1
            pump_on_softner += 1
            if pump_on_softner == 1:
                pumpon_timer = totalmin_count
        else:
            if pump_on_softner >= SOFTNER_THRESHOLD:
                softner_pumpduration.append(pump_on_softner)
                softner_runstart.append(pumpon_timer)
            pump_on_softner = 0

    # Following code determines time needed to reach 5 and 100 gallons
        if pump_onmin_total == GALLON5_MIN:
            gal5_min = totalmin_count
        if pump_onmin_total == GALLON100_MIN:
            gal100_min = totalmin_count

    # Calculate total water pumped
    water_vol = pump_onmin_total * WATERPERKW

    # Calculate cost in $ per kWh
    power_cost = (pump_poweruse/KWH_WMIN)*COST_KWDOLLAR

    # Print code for data summary
    print("Data covers a total of", totalmin_count/MININHOURS, "hours")
    print("(That's", totalmin_count/MININDAY, "days)\n")

    # Print code for Pump run time
    print("Pump was running for", pump_onmin_total, "minutes, producing",
          water_vol, "gallons")
    print("(That's", (MININDAY * water_vol)/totalmin_count,
          "gallons per day)\n")

    # Print cost for running the pump (EXTRA)
    print("The cost of running the pump for",
          round(pump_onmin_total/MININHOURS, 2),
          "hours is $", round(power_cost, 2), "\n")

    # Print code for power consumption
    print("Pump required a total of", pump_poweruse,
          "watt minutes of power")
    print("That's", round(pump_poweruse/KWH_WMIN, totalmin_count), "kWh\n")

    # Print code for filling 5 and 100 gallons
    print("It took", gal5_min, "minutes of data to reach 5 gallons.")
    print("It took", gal100_min, "minutes of data to reach 100 gallons.\n")

    # Print code for water softner recharges
    if len(softner_pumpduration) != 0:
        print("Information on water softner recharges:")
    for i in range(len(softner_pumpduration)):
        print(softner_pumpduration[i], "minute run started at",
              softner_runstart[i])


main()
