import time, sys, traceback
print("SCHOOL SIMULATOR 1997")
time.sleep(2)
n = input("Please enter your name ")
print("APRIL 15, 1997")
time.sleep(2)
print("Teacher: Quiet down now, class.")
time.sleep(2.5)
print("Teacher: Thank you.")
time.sleep(1)
x = input("Teacher: Alright, please hand in your essays now. ")
if x == "Waluigi":
    print("https://www.youtube.com/watch?v=EOy6-AxbSE8")
    time.sleep(1)
    print("You Win!")
elif x == "https://www.namecheap.com/cart/cart.aspx?isupdate=true&itemid=170723048&type=d&durationdetails=1%20YEAR&":
    time.sleep(1)
    print("Teacher: I recognize that! Hey, you plagarized your essay!")
    time.sleep(1.5)
    kill1 = input("Kill the teacher? [Yes/No] ")
    if kill1 == "Yes":
        print("Teacher: ... *You hear sirens in the distance*")
        time.sleep(.5)
        print("GAME OVER.")
    else: print("GAME OVER.")
else:
    essay = x.split()
    print("The teacher places your essay in a stack, to be graded tommorow")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("APRIL 16, 1997")
    time.sleep(3)

    count = 0

    print("Teacher: You will now be called up one by one to learn your grade.")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("6 names later")
    time.sleep(2)
    print(n+", please come up here")
    time.sleep(1.75)
    for x in essay:
        if len(x) >10:
            count = count + 1
    if count < 5:
        print("Teacher: F!")
        time.sleep(1)
        kill2 = input("Kill the teacher? [Yes/No] ")
        if kill2 == "Yes":
            print("Teacher: ... *You hear sirens in the distance*")
            time.sleep(1)
            print("GAME OVER.")
        else:
            print("GAME OVER.")
    if count > 5:
        print("Teacher: A+!")
        time.sleep(1)
        print("YOU WIN!")
