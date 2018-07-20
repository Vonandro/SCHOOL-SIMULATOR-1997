import time, sys, traceback
print("SCHOOL SIMULATOR 1997")
time.sleep(1)
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
elif x == "https://www.namecheap.com/cart/cart.aspx?isupdate=true&itemid=170723048&type=d&durationdetails=1%20YEAR&" or x == "After the World War I, the Czechs outnumbered Slovaks two to one in the new Czechoslovak state.[13] The Slovaks lived in the shadow of the more internationally recognized Czech leadership and the great capital of Prague.[13] The relationship between the Czechs and Slovaks was asymmetrical: Slovakia was considered an agrarian appendage to the highly industrial Czech nation,[13][14] and the Czechs viewed Slovak culture as lacking in maturity and refinement.[14] The languages of the two nations are closely related and mutually intelligible, many Czechs viewed Slovak as a caricature of Czech.[14] In his 1934 memoirs, the President of Czechoslovakia, Tomáš Garrigue Masaryk, writes he said in a 1924 interview to a French journalist of Le Petit Parisien: «There is no Slovak nation, it has been invented by Hungarian propaganda. The Czechs and Slovaks are brothers. They understand each other perfectly. All that separates them is the cultural level - the Czechs are more developed than the Slovaks, because the Magyars kept them in the dark. (...) In one generation there will be no difference between the two branches of our national family.»[15] However the interview is nowhere to be found in the scanned full archives of Le Petit Parisien.[16]":
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
