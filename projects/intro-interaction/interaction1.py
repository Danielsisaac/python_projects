loop = True

while loop: #normally, the while loop uses the component that, if a condition is true, it should run, and if false, it shouldn't. So the code can be written as while loop == true:, but this method kind of gives a shorter and cleaner vesion.
    password = input("Input your password: ")
    if password == "stop":
        break
#In this line of code, the variable used in the condition of the loop has to first be set to a particular condition. After that, the while loop can be used, and if the while loop keeps being true, the loop keeps running and that break function remains until the loop condition is met, and the loop becomes true, then the break function kicks in and drags the code outside the while loop.