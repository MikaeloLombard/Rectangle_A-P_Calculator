#Area and Perimeter Calculator for Rectangles
def calculate():
    
    print ('Welcome to Rectangle Area and Perimeter Calculator')
    width = input("What is the width? ")
    height = input("What is the height? ")

#Calculate area and perimeter

    area = float(width) * float(height)
    print ("The area is {0:.2f}" .format(area))

    perimeter = (float(width)*2 + float(height)*2)
    print ('The perimeter is {0:.2f}' .format(perimeter))

#restart

    again()

def again():
    calc_again = input(" Do you want to restart the Calculator? Type Y for Yes or N for No. ")

    if calc_again.upper() == 'Y':
            calculate()
    if calc_again.upper() == 'N':
            print("Good bye!")
    else:
        again()


calculate()
    
    
