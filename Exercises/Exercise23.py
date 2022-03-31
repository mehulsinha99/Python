actor1 = "Sean Connery"
actor2 = "Roger Moore"
actor3 = "Pierce Brosnan"
actor4 = "Daniel Craig"
score = 0
for i in range(1,5):
    attempt1 = input("Attempt - Name an actor:")
    if(attempt1.lower()==actor1.lower()): # or attempt1==actor2 or attempt1==actor3 or attempt1==actor4):
        print("Well done:",actor1,"was Bond in From Russia with Love.")
        score+=1
    elif(attempt1.lower()==actor2.lower()):
        print("Well done:",actor2,"was Bond in From Live and Let Die.")
        score += 1
    elif(attempt1.lower()==actor3.lower()):
        print("Well done:",actor3,"was Bond in From Die Another Day")
        score += 1
    elif(attempt1.lower()==actor4.lower()):
        print("Well done:",actor4,"was Bond in From Skyfall")
        score += 1
    else:
        print("Sorry. ",attempt1, "hasn’t played Bond as far as I know.")
print("your score: ",score)