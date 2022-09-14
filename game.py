def rules():
    print(" Welcome to Virtual Cricket") 
    print('\n')
    print(" Let us start with the rules of the game:")
    print("\t 1.)Use smallcase letters for every input required")
    print("\t 2.)For the game and toss you can use numbers in the range of 1-10(both included)")
    print("\t 3.)Both you and the Computer choose random numbers at the same time")
    print("\t 4.)If the numbers are different the person who is batting adds his number to his score")    
    print("\t 5.)If the numbers are same the batsman is out")
    print("\t 6.)If you are bowling and you choose the same number as the computer, the computer loses a wicket")
    print("\t 7.)You and the computer get 3 wickets each")
    print("\t 8.)A scorecard will display the details of the match after every wicket")
    print("\t 9.)The team which scores the highest at the end of the game WINS")
    print("\t 10.)You have the option to name the teams and players.")
    print("\t 11.)Incase of a tie, the match results do not get recorded.")
    print('\n')
    print("\t have fun :)")
    print("\n")
 
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",password="...",database="project")
if mycon.is_connected():
    print("DATABASE CONNECTED :)")
    print("\n")
cursor=mycon.cursor()
def default():
    sql="update scorecard set RUNS=%s "
    num=(0,)
    cursor.execute(sql,num)
    sql="update scorecard set balls=%s "
    num=(0,)
    cursor.execute(sql,num)
    sql="update scorecard set strike_rate=%s "
    num=(0,)
    cursor.execute(sql,num)
default()
 
def matchdetails(t1,r1,t2,r2,p1,pr1):
    #Match no
    sql="select MAX(MATCH_NO) from matchdetails"
    cursor.execute(sql)
    data=cursor.fetchall()
    a=data[0]
    b=a[0]
    c=b+1
    val=(c,t1,r1,t2,r2,p1,pr1)
    sql1="INSERT INTO matchdetails (MATCH_NO,WINNING_TEAM,RUNS_SCORED1,LOSING_TEAM,RUNS_SCORED2,BEST_BATSMAN,RUNS) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql1,val)
    mycon.commit()
    
 
def teamname():
    x=input("Do you want to enter your team's name ? \n ")
    if x=="no":
        tname="Chennai"
    elif x=="yes":
        print("the team name should be within 12 characters")
        tname=input("enter your team name")
    else :
        print("ERROR,Default team name has been applied :| \n")
        tname="Chennai"
               
    return tname
 
def compteamname():
    x=input("Do you want to enter computer's team name ? \n ")
    if x=="no":
        tname="Mumbai"
    elif x=="yes":
        print("the team name should be within 12 characters")
        tname=input("enter computer's team name")
    else:
        print("ERROR,Default team name has been applied :| \n")
        tname="Mumbai"
        
    return tname
    
 
def playernames(z):
    x=input("Do you want to enter players' name ? \n ")
    if x=="no":
        l=["player1","player2","player3"]
    elif x=="yes":
        l=[]
        print("Player's Name should be within 12 characters \n")
        for i in range (1,4):
            print("enter the name for player",i)
            y=input()
            l.append(y)
    else:
        print("ERROR,Default player names have been applied :| \n")
        l=["player1","player2","player3"]
    t=tuple(l)
    a,b,c=t
    p1=(a,1)
    p2=(b,2)
    p3=(c,3)
    sql="update scorecard set P_NAME=%s where S_NO=%s"
    cursor.execute(sql,p1)
    cursor.execute(sql,p2)
    cursor.execute(sql,p3)
    print("PLAYERS NAMES UPDATED :) \n")
    #scorecard
    num=(4,)
    sql2="""select * from scorecard where S_NO<%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
    print("                     ","TEAM",z,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    for row in data:
        print("|",row[0]," "*(8-(len(str(row[0]))+3)),"|"
              ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
              ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
              ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
              ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
            
 
def compnames(z):
    x=input("Do you want to enter computer players' name ? \n ")
    if x=="no":
        l=["player4","player5","player6"]
    elif x=="yes":
        l=[]
        print("Computer Player's Name should be within 12 characters \n")
        for i in range (1,4):
            print("Enter the name for player",i)
            y=input()
            l.append(y)
    else:
        print("ERROR,Default player names have been applied :| \n")
        l=["player4","player5","player6"]
    t=tuple(l)
    a,b,c=t
    p1=(a,4)
    p2=(b,5)
    p3=(c,6)
    sql="update scorecard set P_NAME=%s where S_NO=%s"
    cursor.execute(sql,p1)
    cursor.execute(sql,p2)
    cursor.execute(sql,p3)
    print("COMPUTER PLAYER'S NAMES UPDATED :) \n")
    #SCORECARD
    num=(3,)
    sql2="""select * from scorecard where S_NO>%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
    print("                     ","TEAM",z,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    for row in data:
        print("|",row[0]-3," "*(8-(len(str(row[0]))+3)),"|"
              ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
              ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
              ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
              ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
    
 
        
def toss():
    import random
    call=input("odd or even : ")
    toss=int(input("Enter a number between 1 and 10 :"))
    x= random.randint(1,10)
    print("The computer chose :",x)
    tossdecider=(toss+x)%2
    if call=="even" and tossdecider==0 or call=="odd" and tossdecider==1:
        a=int(input(("You won the toss :) Do you  chose to bat or bowl? \n Press 1 to BAT and 2 to BOWL : ")))
        return a
         
    else:
        print("You lost the toss :(")
        y=random.randint(1,2)
        return y 
 
def batting(z,e):
    import random
    print("You are batting ! \n")
    score=0
    t=0
    sc=0
    nb=0
    while t<3:
        nb=nb+1
        runs=int(input("Enter your number :"))
        pcballs = random.randint(1,10)
        print("The Computer chose :",pcballs)
        if runs>0 and  runs<11 and runs != pcballs:
            score+=runs
            sc+=runs
        elif runs==pcballs:
            pcscore=0
            sr=(sc/nb)*100
            print("You are out")
            
            #sql
            sno=t+1
            sql="update scorecard set RUNS=%s where S_NO=%s"
            val=(sc,sno)
            cursor.execute(sql,val)
            sql="update scorecard set BALLS=%s where S_NO=%s"
            val=(nb,sno)
            cursor.execute(sql,val)
            sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
            val=(sr,sno)
            cursor.execute(sql,val)
            #SCORECARD
            num=(4,)
            sql2="""select * from scorecard where S_NO<%s"""
            cursor.execute(sql2,num)
            data=cursor.fetchall()
 
            print("                     ","TEAM",z,"                    "  )
            print("_____________________________________________________________")
            print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
            print("|________|_______________|________|_________|_______________|")
            for row in data:
                print("|",row[0]," "*(8-(len(str(row[0]))+3)),"|"
                      ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                      ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                      ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                      ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
            print("|________|_______________|________|_________|_______________| \n")
            
            nb,sc=0,0
            t=t+1
            if 3-t!=0:
                print("You have ",3-t,"more wickets \n Your total score is ",score,"\n")
    print("You are Bowling ! The Computer has to score ",score+1,"to WIN")
    pcscore1=0
    u=0
    nb2,sc2=0,0
    while u<3 :
        nb2+=1
        balls1=int(input("Enter your number :"))
        pcruns1 = random.randint(1,10)
        print("The Computer chose :",pcruns1)
        if balls1>0 and balls1<11 and balls1 != pcruns1:
            pcscore1+=pcruns1
            sc2+=pcruns1
            if pcscore1>score:
                sr2=(sc2/nb2)*100
                sno=u+4
                sql="update scorecard set RUNS=%s where S_NO=%s"
                val=(sc2,sno)
                cursor.execute(sql,val)
                sql="update scorecard set BALLS=%s where S_NO=%s"
                val=(nb2,sno)
                cursor.execute(sql,val)
                sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
                val=(sr2,sno)
                cursor.execute(sql,val)
                break
        elif balls1==pcruns1:
            sr2=(sc2/nb2)*100
            print("The Computer is out!")
            
            #sql
            sno=u+4
            sql="update scorecard set RUNS=%s where S_NO=%s"
            val=(sc2,sno)
            cursor.execute(sql,val)
            sql="update scorecard set BALLS=%s where S_NO=%s"
            val=(nb2,sno)
            cursor.execute(sql,val)
            sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
            val=(sr2,sno)
            cursor.execute(sql,val)
            #SCORECARD
            num=(3,)
            sql2="""select * from scorecard where S_NO>%s"""
            cursor.execute(sql2,num)
            data=cursor.fetchall()
            print("                     ","TEAM",e,"                    "  )
            print("_____________________________________________________________")
            print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
            print("|________|_______________|________|_________|_______________|")
            for row in data:
                print("|",row[0]-3," "*(8-(len(str(row[0]))+3)),"|"
                      ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                      ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                      ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                      ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
            print("|________|_______________|________|_________|_______________| \n")
    
            nb2,sc2=0,0
            u=u+1
            if 3-u!=0:
                print("The Computer has ",3-u,"more wickets \n Computer's Total Score is ",pcscore1,"\n the computer needs ",score+1-pcscore1,"to win\n")
 
    num=(4,)
    sql2="""select * from scorecard where S_NO<%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
 
    print("                     ","TEAM",z,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    max_runs1=0
    bb1=""
    srb1=0
    for row in data:
        if row[2]>max_runs1:
            max_runs1=row[2]
            bb1=row[1]
            srb1=row[4]
        print("|",row[0]," "*(8-(len(str(row[0]))+3)),"|"
                ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
    num=(3,)
    sql2="""select * from scorecard where S_NO>%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
    
    print("                     ","TEAM",e,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    max_runs2=0
    bb2=""
    srb2=0
    for row in data:
        if row[2]>max_runs2:
            max_runs2=row[2]
            bb2=row[1]
            srb2=row[4]
        print("|",row[0]-3," "*(8-(len(str(row[0]))+3)),"|"
                ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
        
    if pcscore1>score:
        
        max_runs=0
        bb=""
        if max_runs1>max_runs2:
            max_runs=max_runs1
            bb=bb1
        elif max_runs1==max_runs2:
            if srb1>srb2:
                max_runs=max_runs1
                bb=bb1
            else:
                max_runs=max_runs2
                bb=bb2
        else:
            max_runs=max_runs2
            bb=bb2
        matchdetails(e,pcscore1,z,score,bb,max_runs)
        return "You LOST :("
        
    elif pcscore1<score:
        max_runs=0
        bb=""
        if max_runs1>max_runs2:
            max_runs=max_runs1
            bb=bb1
        elif max_runs1==max_runs2:
            if srb1>srb2:
                max_runs=max_runs1
                bb=bb1
            else:
                max_runs=max_runs2
                bb=bb2
        else:
            max_runs=max_runs2
            bb=bb2
        matchdetails(z,score,e,pcscore1,bb,max_runs)
 
        return "You WON :)"
    else:
 
        return "It's a TIE :0"
 
def bowling(z,e):
    import random
    print("You are bowling ! \n")
    pcscore1=0
    t=0
    nb,sc=0,0
    while t<3:
        nb+=1
        balls1=int(input("Enter your number :"))
        pcruns1 = random.randint(1,10)
        print("The Computer chose :",pcruns1)
        if balls1>0 and balls1<11 and balls1 != pcruns1:
            pcscore1+=pcruns1
            sc+=pcruns1
        elif balls1==pcruns1:
            sr=(sc/nb)*100 
            print("The Computer is out")
            
            #sql
            sno=t+4
            sql="update scorecard set RUNS=%s where S_NO=%s"
            val=(sc,sno)
            cursor.execute(sql,val)
            sql="update scorecard set BALLS=%s where S_NO=%s"
            val=(nb,sno)
            cursor.execute(sql,val)
            sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
            val=(sr,sno)
            cursor.execute(sql,val)
            #SCORECARD
            num=(3,)
            sql2="""select * from scorecard where S_NO>%s"""
            cursor.execute(sql2,num)
            data=cursor.fetchall()
            print("                     ","TEAM",e,"                    "  )
            print("_____________________________________________________________")
            print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
            print("|________|_______________|________|_________|_______________|")
            for row in data:
                print("|",row[0]-3," "*(8-(len(str(row[0]))+3)),"|"
                      ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                      ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                      ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                      ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
            print("|________|_______________|________|_________|_______________| \n")
            
                
            nb,sc=0,0
            t=t+1
            if 3-t!=0:
                print("The Computer has ",3-t,"more wickets \n Computer's Total Score is ",pcscore1,"\n")
    print("You are batting! you have to score",pcscore1+1,"to win")
    score=0
    u=0
    nb2,sc2=0,0
    while u<3:
        nb2+=1
        runs=int(input("Enter your number :"))
        pcballs = random.randint(1,10)
        print("The Computer chose :",pcballs)
        if runs>0 and  runs<11 and runs != pcballs:
            score+=runs
            sc2+=runs
            if score>pcscore1:
                sr2=(sc2/nb2)*100
                sno=u+1
                sql="update scorecard set RUNS=%s where S_NO=%s"
                val=(sc2,sno)
                cursor.execute(sql,val)
                sql="update scorecard set BALLS=%s where S_NO=%s"
                val=(nb2,sno)
                cursor.execute(sql,val)
                sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
                val=(sr2,sno)
                cursor.execute(sql,val)
                break
        elif runs==pcballs:
            pcscore=0
            sr2=(sc2/nb2)*100
            print("You are out! ")
            
            #sql
            sno=u+1
            sql="update scorecard set RUNS=%s where S_NO=%s"
            val=(sc2,sno)
            cursor.execute(sql,val)
            sql="update scorecard set BALLS=%s where S_NO=%s"
            val=(nb2,sno)
            cursor.execute(sql,val)
            sql="update scorecard set STRIKE_RATE=%s where S_NO=%s"
            val=(sr2,sno)
            cursor.execute(sql,val)
            #SCORECARD
            num=(4,)
            sql2="""select * from scorecard where S_NO<%s"""
            cursor.execute(sql2,num)
            data=cursor.fetchall()
            print("                     ","TEAM",z,"                    "  )
            print("_____________________________________________________________")
            print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
            print("|________|_______________|________|_________|_______________|")
            for row in data:
                print("|",row[0]," "*(8-(len(str(row[0]))+3)),"|"
                      ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                      ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                      ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                      ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
            print("|________|_______________|________|_________|_______________| \n")
           
                
            nb2,sc2=0,0
            u=u+1
            if 3-u!=0:
                print("You have ",3-u,"more wickets \n Your total score is ",score,"\n you need",pcscore1+1-score,"to win \n")
 
    num=(4,)
    sql2="""select * from scorecard where S_NO<%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
 
    print("                     ","TEAM",z,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    max_runs1=0
    bb1=""
    srb1=0
    for row in data:
        if row[2]>max_runs1:
            max_runs1=row[2]
            bb1=row[1]
            srb1=row[4]
        print("|",row[0]," "*(8-(len(str(row[0]))+3)),"|"
                ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
    num=(3,)
    sql2="""select * from scorecard where S_NO>%s"""
    cursor.execute(sql2,num)
    data=cursor.fetchall()
    
    print("                     ","TEAM",e,"                    "  )
    print("_____________________________________________________________")
    print("|  S.NO  |  PLAYER NAME  |  RUNS  |  BALLS  |  STRIKE RATE  |")
    print("|________|_______________|________|_________|_______________|")
    max_runs2=0
    bb2=""
    srb2=0
    for row in data:
        if row[2]>max_runs2:
            max_runs2=row[2]
            bb2=row[1]
            srb2=row[4]
        print("|",row[0]-3," "*(8-(len(str(row[0]))+3)),"|"
                ,row[1]," "*(15-(len(str(row[1]))+3)),"|"
                ,row[2]," "*(8-(len(str(row[2]))+3)),"|"
                ,row[3]," "*(9-(len(str(row[3]))+3)),"|"
                ,row[4]," "*(15-(len(str(row[4]))+3)),"|")
    print("|________|_______________|________|_________|_______________| \n")
    
    if pcscore1>score:
        
        max_runs=0
        bb=""
        if max_runs1>max_runs2:
            max_runs=max_runs1
            bb=bb1
        elif max_runs1==max_runs2:
            if srb1>srb2:
                max_runs=max_runs1
                bb=bb1
            else:
                max_runs=max_runs2
                bb=bb2
        else:
            max_runs=max_runs2
            bb=bb2
        matchdetails(e,pcscore1,z,score,bb,max_runs)
 
        return "You LOST :("
    elif pcscore1<score:
 
        max_runs=0
        bb=""
        if max_runs1>max_runs2:
            max_runs=max_runs1
            bb=bb1
        elif max_runs1==max_runs2:
            if srb1>srb2:
                max_runs=max_runs1
                bb=bb1
            else:
                max_runs=max_runs2
                bb=bb2
        else:
            max_runs=max_runs2
            bb=bb2
        matchdetails(z,score,e,pcscore1,bb,max_runs)
    
 
        return "You WON :)"
    else:
        
 
        return "It's a TIE :0"
def default():
    sql="update scorecard set RUNS=%s "
    num=(0,)
    cursor.execute(sql,num)
    sql="update scorecard set balls=%s "
    num=(0,)
    cursor.execute(sql,num)
    sql="update scorecard set strike_rate=%s "
    num=(0,)
    cursor.execute(sql,num)
 
 
rules()
 
t=teamname()
r=compteamname()
 
p=playernames(t)
 
 
q=compnames(r)
 
 
 
z=toss()
if z==1:
    print(batting(t,r))
else:
    print(bowling(t,r))
 
rep=input("Do you want to view a report of all the matches played: ")
if rep=="yes":
    print("__________________________________________________________________________________________________________________")
    print("|  MATCH_NO:  |  WINNING TEAM  |  RUNS SCORED   |  LOSING TEAM  |  RUNS SCORED  |  BEST BATSMAN  |  RUNS SCORED  |")
    print("|_____________|________________|________________|_______________|_______________|________________|_______________|")
    
    cursor.execute("""select * from matchdetails""")
    data=cursor.fetchall()
    for row in data:
        print("|",row[0]," "*(13-(len(str(row[0]))+3)),"|"
              ,row[1]," "*(16-(len(str(row[1]))+3)),"|"
              ,row[2]," "*(16-(len(str(row[2]))+3)),"|"
              ,row[3]," "*(15-(len(str(row[3]))+3)),"|"
              ,row[4]," "*(15-(len(str(row[4]))+3)),"|"
              ,row[5]," "*(16-(len(str(row[5]))+3)),"|"
              ,row[6]," "*(15-(len(str(row[6]))+3)),"|")
    print("|_____________|________________|________________|_______________|_______________|________________|_______________|")
else:
    print("Have a nice day :)")
