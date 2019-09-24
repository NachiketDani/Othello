# Diagnosis program by Nachiket Dani


def main():
    # Define diagnosis variables
    diagnosis1 = "Possibilities include pneumonia or infection of airways"
    diagnosis2 = "Possibilities include viral infection"
    diagnosis3 = "Possibilities include a throat infection"
    diagnosis4 = "Possibilities include kidney infection"
    diagnosis5 = "Possibilities include a urinary tract infection"
    diagnosis6 = "Possibilities sunstroke or heat exhaustion"
    diagnosis7 = "Possibilities include meningitis"
    diagnosis8 = "Possibilities include digestive tract infection"
    diagnosis9 = "Insufficient information to list possibilities"
    # Define symptom variables
    sym_check1 = "Are you coughing?"
    sym_check2 = "Are you short of breath or wheezing or coughing up phlegm?"
    sym_check3 = "Do you have a headache?"
    sym_check4 = "Do you have aching bones or aching joints?"
    sym_check5 = "Do you have a rash?"
    sym_check6 = "Do you have a sore throat?"
    sym_check7 = "Do you have back pain just above the waist with chills and fever?"
    sym_check8 = "Do you have pain urinating or urinating more often?"
    sym_check9 = "Have you spent the day in the sun or in hot conditions?"
    sym_check10 = "Are you experiencing any of the following: \n - pain when bending your head forward,\n - experience nausea or vomiting,\n - bright light hurts your eyes,\n - experiencing drowsiness or confusion?"
    sym_check11 = "Are you vomiting or had diarrhea?"

    # Define status variable to track diagnosis
    status = "check with patient"

    # Subroutine for diagnoses leading to sym_check4 questionnaire
    def routine_sym4():
        status = input(sym_check4).title()
        if status == "Yes":
            print(diagnosis2)
        elif status == "No":
            status = input(sym_check5).title()
            if status == "Yes":
                print(diagnosis9)
            elif status == "No":
                status = input(sym_check6).title()
                if status == "Yes":
                    print(diagnosis3)
                elif status == "No":
                    status = input(sym_check7).title()
                    if status == "Yes":
                        print(diagnosis4)
                    elif status == "No":
                        status = input(sym_check8).title()
                        if status == "Yes":
                            print(diagnosis5)
                        elif status == "No":
                            status = input(sym_check9).title()
                            if status == "Yes":
                                print(diagnosis6)
                            elif status == "No":
                                print(diagnosis9)

    # Subroutine sym_check4 triggered if symptom 3 and 11 fail
    def routine_sym311():
            routine_sym4()

    # Subroutine for diagnoses leading to symptom3 only if sym_check1 is Yes
    def routine_sym3A():
        status = input(sym_check3).title()
        if status == "Yes":
            print(diagnosis3)
        elif status == "No":
            routine_sym4()

    # Subroutine for diagnoses leading to symptom3 only if sym_check1 is No
    def routine_sym3B():
        status = input(sym_check3).title()
        if status == "Yes":
            status = input(sym_check10).title()
            if status == "Yes":
                print(diagnosis7)
            elif status == "No":
                status = input(sym_check11).title()
                if status == "Yes":
                    print(diagnosis8)
                elif status == "No":
                    routine_sym311()
        elif status == "No":
            routine_sym311()

    # Begin Diagnosis by sym_check1
    status = input(sym_check1).title()
    if status == "Yes":
        status = input(sym_check2).title()
        if status == "Yes":
            print(diagnosis1)
        elif status == "No":
            routine_sym3A()
    elif status == "No":
        routine_sym3B()

main()