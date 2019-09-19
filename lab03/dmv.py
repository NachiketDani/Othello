import random
def main():

    print ("Welcome to the DMV (estimated wait time is 3 hours)")
    driver_name = input ("Please enter your first, middle, and last name: \n")
    birthdate = input ("Enter date of birth (MM/DD/YY): \n")
    
    ##Generate 7 digit Drivers license number
    dl_num = random.randint (1,9999999)
    dl_str = str(dl_num).zfill(7)

    ##Create Name format
    splitname_index = driver_name.rfind (" ")
    first_name = driver_name [0:splitname_index]
    last_name = driver_name [splitname_index+1:]

    ##Create Expiry Date
    exp_index = birthdate.rfind ("/")
    exp_date = birthdate [0:exp_index+1]+"21"

    ##Print Driver's License
    print ("-------------------------------------")
    print ("Washington Driver License")
    print ("DL", dl_str)
    print ("LN", last_name)
    print ("FN", first_name)
    print ("DOB", birthdate)
    print ("EXP", exp_date)
    print ("-------------------------------------")

main()

