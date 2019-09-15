#HW02. Prepared by Nachiket Dani

def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    maxHR = 207 - (0.7 * age)
    reserve = maxHR - restHR

    #Following program calculates the heart zones which corelate to stress levels during exercise 
    # Zone 1 (50-60%): This zone should feel super easy -- almost like you didn't work out at all.
    # Zone 2 (60-70%): This is the "average effort" level where it is still possible to hold a conversation.
    # Zone 3 (70-80%): This is the "above average effort" level where you can only talk in one- or two- word answers.
    # Zone 4 (80-93%): This is the "hard effort" level. Your breathing is labored, your arms and legs feel heavy, and you can't sustain the pace for much more than an hour (at best).
    # Zone 5 (93-100%): This is the "all out" level. You can sustain this pace for a few seconds to maybe five minutes
    # The print statements calculate the upper and lower range limits without storing them in any variable for future reference 
    # since the problem is fairly simple.

    print("Zone1:",round(restHR + (reserve * 0.500),2),"to",round(restHR + (reserve * 0.600),2),"bpm")
    print("Zone2:",round(restHR + (reserve * 0.601),2),"to",round(restHR + (reserve * 0.700),2),"bpm")
    print("Zone3:",round(restHR + (reserve * 0.701),2),"to",round(restHR + (reserve * 0.800),2),"bpm")
    print("Zone4:",round(restHR + (reserve * 0.801),2),"to",round(restHR + (reserve * 0.930),2),"bpm")
    print("Zone5:",round(restHR + (reserve * 0.931),2),"to",round(restHR + (reserve),2),"bpm")
    print("=======================================")

main()