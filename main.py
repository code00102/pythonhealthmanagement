# health management system
# 3 clients - Harry, Rohan and Hammad
"""
def getDate():
    import datetime
    return datetime.datetime.now()
"""


# function to create 6 new files of diet and exercise for 3 clients
# write into them.
# input should be printed in both file and the console.
# [date] input
# function to retrieve what we entered.
from asyncore import write


def getDate():
    import datetime
    return datetime.datetime.now()


def fileCreation():
    with open("HarryDiet.txt", "w") as fp:
        pass
    with open("HarryExercise.txt", "w") as fp:
        pass
    with open("RohanDiet.txt", "w") as fp:
        pass
    with open("RohanExercise.txt", "w") as fp:
        pass
    with open("HammadDiet.txt", "w") as fp:
        pass
    with open("HammadExercise.txt", "w") as fp:
        pass


def askFirst():
    while True:
        a = int(input("Enter 1 for data log and 2 for data retrieve: "))
        if a == 1:
            dataLog()
            break
        elif a == 2:
            dataReturn()
            break
        else:
            print("Only Logging and Retrieval is allowed. ")
            continue


def dataLog():
    global datey
    while True:
        names = int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad: "))
        if names == 1:
            while True:
                types = int(input("Press 1 for Diet and 2 for Exercise: "))
                if types == 1:
                    strs = input("What diet would you like to take? ")
                    print(datey, strs)
                    with open("HarryDiet.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to continue? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                elif types == 2:
                    strs = input("What exercise would you like to perform? ")
                    print(datey, strs)
                    with open("HarryExercise.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to continue? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                else:
                    print("Only Diet and Exercise are allowed. ")
                    continue

            again = input("Do you like to continue logging for Harry? Y|N ")
            if again == "Y":
                continue
            else:
                break

        elif names == 2:
            while True:
                types = int(input("Press 1 for Diet and 2 for Exercise: "))
                if types == 1:
                    strs = input("What diet would you like to take? ")
                    print(datey, strs)
                    with open("RohanDiet.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to write again? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                elif types == 2:
                    strs = input("What exercise would you like to perform? ")
                    print(datey, strs)
                    with open("RohanExercise.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to write again? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                else:
                    print("Only Diet and Exercise are allowed. ")
                    continue
            again = input("Do you like to continue logging for Rohan? Y|N ")
            if again == "Y":
                continue
            else:
                break

        elif names == 3:
            while True:
                types = int(input("Press 1 for Diet and 2 for Exercise: "))
                if types == 1:
                    strs = input("What diet would you like to take? ")
                    print(datey, strs)
                    with open("HammadDiet.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to write again? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                elif types == 2:
                    strs = input("What exercise would you like to perform? ")
                    print(datey, strs)
                    with open("HammadExercise.txt", "a") as fp:
                        fp.write(datey)
                        fp.write("\t")
                        fp.write(strs)
                    cont = input("Would you like to write again? Y|N ")
                    if cont == "Y":
                        continue
                    else:
                        break
                else:
                    print("Only Diet and Exercise are allowed. ")
                    continue

            again = input("Do you like to continue logging for Hammad? Y|N ")
            if again == "Y":
                continue
            else:
                break

        else:
            print("Only Harry, Rohan and Hammad are allowed. Sorry ! ")
            continue


def dataReturn():
    while True:
        ip = int(input("Whose data would you like to obtain?"
                       " 1 for Harry "
                       " 2 for Rohan "
                       " 3 for Hammad "))
        if ip == 1:
            while True:
                types = int(input("Press 1 to retrieve diet log and 2 to retrieve exercise log: "))
                if types == 1:
                    with open("HarryDiet.txt", "r") as fp:
                        print(fp.read())
                    break
                elif types == 2:
                    with open("HarryExercise.txt", "r") as fp:
                        print(fp.read())
                    break
                else:
                    print("Sorry! You can only retrieve diet and exercise. ")
                    continue
            break

        elif ip == 2:
            while True:
                types = int(input("Press 1 to retrieve diet log and 2 to retrieve exercise log: "))
                if types == 1:
                    with open("RohanDiet.txt", "r") as fp:
                        print(fp.read())
                    break
                elif types == 2:
                    with open("RohanExercise.txt", "r") as fp:
                        print(fp.read())
                    break
                else:
                    print("Sorry! You can only retrieve diet and exercise. ")
                    continue
            break

        elif ip == 3:
            while True:
                types = int(input("Press 1 to retrieve diet log and 2 to retrieve exercise log: "))
                if types == 1:
                    with open("HammadDiet.txt", "r") as fp:
                        print(fp.read())
                    break
                elif types == 2:
                    with open("HammadExercise.txt", "r") as fp:
                        print(fp.read())
                    break
                else:
                    print("Sorry! You can only retrieve diet and exercise. ")
                    continue
            break

        else:
            print("Sorry! You can only retrieve data for Harry, Rohan and Hammad. ")


getDate()
datey = str(getDate())
fileCreation()
askFirst()
