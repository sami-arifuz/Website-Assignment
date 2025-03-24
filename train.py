
#1. Length Check

id = input("Enter your 12 digit ID: ")

if len(id) == 12:
    print("Correct ID! ")
    
else: 
    print("Your id is not 12 digit. try again!")
    


#2. Operator Check

if id[0:3] == "NRL" or id[0:3] == "SRT" or id[0:3] =="MLN":
    print("Correct")
    
    

#3. Station Code

if id[3:7] == "LDBR":
    print("London Bridge Station")
    
elif id [3:7] == "ESLD":
    print("East London Station")
    


#4. Date and Time Check

day = id[7:9]
time = id [9:11]

if not (1 <= day <= 31):
    print("Incorrect date; enter a correct date." )
    
elif not (00 <= time <= 23):
    print("Incorrect time; enter a correct time. ")
    


#5. Status Check

