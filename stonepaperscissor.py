import random
list=["r","p","s"]
comp_win=0
me_win=0
chance=1
name=input("please enter your name\n")
print("welcome to my game",name,"\n")
r=int(input("how many rounds you would like to play\n"))

while chance<=r:
    print(f"ROUND:{chance}")
    me=input("enter your choice\nr for rock  p for paper  s for scissor\n")
    if me!= "r" and me!="p" and me!="s":
        print("oops wrong input")
        continue
    comp = random.choice(list)
    if comp=="r":
        if me=="p":
            me_win+=1
        elif me=="s":
            comp_win+=1
    if comp=="p":
        if me=="r":
            comp_win+=1
        elif me=="s":
            me_win+=1

    if comp=="s":
        if me=="r":
            me_win+=1
        elif me=="p":
            comp_win+=1

    if me_win>comp_win:
        print("congrats you win this round",name,"\n")
    elif me_win<comp_win:
        print("sorry you lost this round",name,"\n")
    else:

        print("round drawn!!\n")
    chance+=1
if me_win>comp_win:
        print("congrats you win the game",name,"\n")
elif me_win<comp_win:
        print("sorry you lost the game",name,"\n")
else:
        print("game drawn!!\n")
print("your score:",me_win,"\n")
print("computer score:",comp_win,"\n")





