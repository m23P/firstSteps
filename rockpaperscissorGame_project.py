import random
c=["Rock", "Paper" ,"Scissor"]
while(True):
    ucount=0
    Ccount=0
    uc=int(input(''' 
GAME Star......
1.Yes
2.NO || EXIT                              
 '''))
    if (uc==1):
        for i in range(5):
            userinput=int(input(''' 
enter your choice:                                
1.Rock
2.Paper
3.Scissor
            ''') )
        
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor"
            Cchoice=random.choice(c)
            if(Cchoice==uchoice):
                print("Computer choice is :",Cchoice)
                print("User choice:",uchoice)
                ucount=ucount+1
                Ccount=Ccount+1
                print("GAME DRAW:")
            elif((uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice =="Paper")):
                print("Computer choice is:",Cchoice)
                print("User choice:",uchoice)
                print("you win ")
                ucount=ucount+1
            else:
                print("Computer choice is:",Cchoice)
                print("User choice:",uchoice)
                print("Computer Win:")
                Ccount=Ccount+1
        if(Ccount==ucount):
            print("Game Draw")
            print("User Score:",ucount)
            print("computer Score:",Ccount)
        elif(ucount>Ccount):
            print(" FINAL RESULT YOU WIN")
            print("User Score:",ucount)
            print("computer Score:",Ccount)
        else:
            print("FINAL RESULT COMPUTER WIN:")
            print("User Score:",ucount)
            print("computer Score:",Ccount)
    else:
        break        
                           
                
                
                
                        