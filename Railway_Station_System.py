import csv

# to check if user already exist or not
def check_user_name(a): 
    with open("user_data.csv","r") as csv_file:
        read=csv.reader(csv_file)
        for rows,i in read:
            if rows == a:
                return 1 

# to create user
def create_user(info,a):  
    with open("user_data.csv","a", newline='') as csv_file:
        write=csv.writer(csv_file)
        write.writerow(info)
        print("***********************************************")
        print("You have signup successfully!")


# to login user
def user_exist(a,b):
    with open("user_data.csv","r") as csv_file:
        read=csv.reader(csv_file)
        for rows,i in read:
            if rows == a and rows == b:
                return 1 


# write login user data
def write_data(info,a):
    with open("{}.csv".format(a),"a", newline='') as csv_file:
        write=csv.writer(csv_file)
        write.writerow(info)

# read login user data
def read_data(a):
    with open("{}.csv".format(a),"r") as csv_file:
        read=csv.reader(csv_file)
        for rows in read:
            print(rows)

# city enter input
def city_enter():
  try:
     x=int(input("Select the city you want to visit from Rawalpindi :"))
     return x
  except ValueError:
    print("***********************************************")
    print("Invalid input. Please enter a valid integer.")
    return city_enter()   


# bogie number input
def bogie_enter():
  try:
    print("***********************************************")
    y=int(input("Select the Bogie please :"))
    return y
  except ValueError:
    print("***********************************************")
    print("Invalid input. Please enter a valid integer.")
    return bogie_enter()

def main():
    while True:
        with open("user_data.csv","a", newline='') as csv_file:
            write=csv.writer(csv_file)
        print("***********************************************")
        print("\tWelcome to our PLATFORM\n")
        print("1: For Signup\n2: For Login\n3: For Exit")
        try:
            value = int(input("choose : "))
        except:
            print("***********************************************")
            print("Invalid choice!")
            continue
        if value == 1:
            print("***********************************************")
            print("\t\tSignup\n")
            user_name = input("Enter your username: ")
            user_password = input("Choose password: ")
            return_val = check_user_name(user_name)
            if return_val == 1:
                print("***********************************************")
                print("User already exist! plz choose other username!")
            else :
                info = [user_name,user_password]
                create_user(info,user_name)               

        elif value == 2:
            print("***********************************************")
            print("\t\tLogin\n")
            user_name = input("Enter your username: ")
            user_password = input("Enter your password: ")
            return_val = user_exist(user_name,user_password)
            if return_val == 1:
                try:
                    with open("{}.csv".format(user_name),"a", newline='') as csv_file:
                        write=csv.writer(csv_file)
                    cities=["none","Lahore","Karachi","Quetta","Peshawar"]
                    bogies=["none","Executive Class","Lower A/C Bogie","Economy Class","First Class Sleeper","Economy Sleeper"]
                    while True:
                        print("***********************************************")
                        print("\t\tMain Menu")
                        print("1 For Booking tickets")
                        print("2 For Previous Records")
                        print("3 For Exit")
                        key=int(input("choose : ")) 
                        if (key==1):
                            print("***********************************************")
                            name=str(input("Enter your name : "))
                            print("1. Lahore")
                            print("2. Karachi")
                            print("3. Quetta")
                            print("4. Peshawar")
                            city=int(city_enter())
                            if (city==1):
                                print("***********************************************")
                                print("You have selected to visit Lahore")
                                print(" 1. Executive Class , price 1500 per person \n 2. Lower A/C Bogie , , price 800 per person \n 3. Economy Class Bogie , , price 1000 per person")       
                                #These prices are without government tax but in total bill government tax will also be included according to a number of tickets.
                                bogie_class=int(bogie_enter())
                                if (bogie_class==1):
                                    print("***********************************************")
                                    exec=1500
                                    print("You have selected an Executive Class Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((exec*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(exec*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==2):
                                    print("***********************************************")
                                    low=800
                                    print("You have selected a Lower A/C Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((low*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(low*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==3):
                                    print("***********************************************")
                                    econ=1000
                                    print("You have selected an Economy Class Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((econ*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(econ*tickets)+tax
                                    print("Your total bill is : ",bill)
                                else:
                                    print("***********************************************")
                                    ("Please select correct option.") 
                            elif (city==2):
                                print("***********************************************")
                                print("You have selected to visit Karachi.")
                                print(" 1. Executive Class , price 8000 per person \n 2. Lower A/C Bogie , price 2000 per person \n 3. Economy Class Bogie , price 3000 per person \n 4. First Class Sleeper bogie, 4500 per person \n 5. Economy Sleeper Bogie, price 6000 per person")       
                                #These prices are without government tax but in total bill government tax will also be included according to number of tickets
                                bogie_class=int(bogie_enter())
                                if (bogie_class==1):
                                    print("***********************************************")
                                    exec=8000
                                    print("You have selected an Executive Class Bogie.")
                                    tickets=input("Enter number of seats you want : ")
                                    tax=((exec*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(exec*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==2):
                                    print("***********************************************")
                                    low=2000
                                    print("You have selected a Lower A/C Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((low*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(low*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==3):
                                    print("***********************************************")
                                    econ=3000
                                    print("You have selected an Economy Class Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((econ*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(econ*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==4):
                                    print("***********************************************")
                                    f_class_sleeper=4500
                                    print("You have selected an First Class Sleeper Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((f_class_sleeper*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(f_class_sleeper*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==5):
                                    print("***********************************************")
                                    econ_sleeper=6000
                                    print("You have selected an Economy Sleeper Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((econ_sleeper*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(econ_sleeper*tickets)+tax
                                    print("Your total bill is : ",bill)  
                                else:
                                    print("***********************************************")
                                    ("Please select correct option.")
                            elif (city==3):
                                print("***********************************************")
                                print("You have selected to visit Quetta.")
                                print(" 1. First Class Sleeper bogie , price 2500 per person \n 2. Economy Sleeper Bogie , price is 4000 per person")       
                                #These prices are without government tax but in total bill government tax will also be included according to number of tickets
                                bogie_class=int(bogie_enter())
                                if (bogie_class==1):
                                    print("***********************************************")
                                    f_class_sleeper=2500
                                    print("You have selected an First Class Sleeper Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((f_class_sleeper*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(f_class_sleeper*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==2):
                                    print("***********************************************")
                                    econ_sleeper=4000
                                    print("You have selected an Economy Sleeper Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((econ_sleeper*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(econ_sleeper*tickets)+tax
                                    print("Your total bill is : ",bill)    
                                else:
                                    print("***********************************************")
                                    ("Please select correct option.")
                            elif (city==4):
                                print("***********************************************")
                                print("You have selected to visit Peshawar")
                                print(" 1. Executive Class Bogie , price 2500 per person \n 2. Lower A/C Bogie , price 1200 per person \n 3. Economy Class Bogie , price 2000 per person")       
                                #These prices are without government tax but in total bill government tax will also be included according to a number of tickets.
                                bogie_class=int(bogie_enter())
                                if (bogie_class==1):
                                    print("***********************************************")
                                    exec=2500
                                    print("You have selected an Executive Class Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((exec*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(exec*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==2):
                                    print("***********************************************")
                                    low=1200
                                    print("You have selected an Lower A/C Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((low*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(low*tickets)+tax
                                    print("Your total bill is : ",bill)
                                elif (bogie_class==3):
                                    print("***********************************************")
                                    econ=2000
                                    print("You have selected an Lower A/C Bogie.")
                                    tickets=int(input("Enter number of seats you want : "))
                                    tax=((econ*tickets)/100)*15
                                    print("Government tax is : ",tax)
                                    bill=(econ*tickets)+tax
                                    print("Your total bill is : ",bill)
                                else:
                                    print("***********************************************")
                                    ("Please select correct option.")  
                            else:
                                print("***********************************************")
                                ("Please enter the correct city.Thanks")  

                            info=[name,cities[city],bogies[bogie_class],tickets,bill]
                            write_data(info,user_name) 
                        elif (key==2):
                            print("***********************************************")
                            read_data(user_name)
                        elif (key==3):
                            print("***********************************************")
                            return main()
                        else:
                            print("***********************************************")
                            print("Plz choose valid option!")
                except ValueError:
                    print("***********************************************")
                    print('An error occurred:')
            else:
                print("***********************************************")
                print("Invalid Credentials!")
        elif value == 3:
            print("***********************************************")
            print("Exit Successfully")
            print("***********************************************")
            break
        else:
            print("***********************************************")
            print("Plz choose valid option!")
            return main()

if __name__ == "__main__":
    main()