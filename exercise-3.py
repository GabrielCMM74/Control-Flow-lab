# exercise-03 Calculate Dog Years

dogage = int(input("Please enter a dog's age in human years "))

if (dogage == 1):
    print("The dog's age in dog years is 10 years")

elif (dogage == 2):
    print("The dog's age in dog years is 20 years")
    
elif (dogage > 2):
    y = ((dogage-2)*7) + 20
    print("The dog's age in dog years is " + str(y) + " years")