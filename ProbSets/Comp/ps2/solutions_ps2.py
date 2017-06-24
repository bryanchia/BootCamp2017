import box
import sys
import random

if __name__ =="__main__":
 
    
    #Use name if he provides one right after command line argument
    
    if len(sys.argv) == 2:
        
        name = sys.argv[1]
    #Prompt user for name otherwise
    
    else:
        
        name = input("Player name:")

    #Start game

    remaining = [1,2,3,4,5,6,7,8,9]
    valid = True

    while valid == True:
        
        print("\n")
        print("Numbers left:", remaining)

        #Roll a valid number
        if max(remaining) > 6:
            roll = random.randint(2,12)
        else:
            roll = random.randint(1,6)
        print("Roll:",roll)

        #Check if roll is valid
        valid = box.isvalid (roll,remaining)

        if valid == True:

            eliminate_sum = 0

            while eliminate_sum != roll:

                #Prompt for numbers to eliminate
                eliminate = input("Numbers to eliminate:")
                eliminate_int = box.parse_input(eliminate,remaining )

                #Check to see if the sum of numbers chosen is correct
                eliminate_sum = sum(eliminate_int)

                if eliminate_sum != roll:

                	print("Invalid input")

            #Remove the numbers from the list 

            toremove = []

            for i in range(0,len(eliminate_int)):

            	toremove = eliminate_int[i]
            	remaining.remove(toremove)

    print("Game over!")
    final_score = sum(remaining)
    print("\n")
    print("Score for player",name,":",final_score,"points")

    if final_score !=0:
        print("Congratulations!! You shut the box!")









