l1=[32,124,32,124,32]
l2=[32,124,32,124,32]
l3=[32,124,32,124,32]
l=[l1,l2,l3]
d1=[32,124,32,124,32]
d2=[32,124,32,124,32]
d3=[32,124,32,124,32]
D=[l1,l2,l3]
D[1][2]=chr(88)
def check(row,col,turn):
    if(turn==1):
        win1=True
        if((row-1+col-1)!=4 and (row-1+col-1)!=2 and (row-1+col-1)!=0):
            for i in range(0,5,2):
                if(l[row-1][i]!=chr(88)):
                    win1=False
            if(win1==True):
                return True
            for i in range(3):
                if(l[i][col-1]!=chr(88)):
                    win1=False
            if(win1==True):
                return True
            else:
                return False
        else:
            for i in range(0,5,2):
                if(l[row-1][i]!=chr(88)):
                    win1=False
            if(win1==True):
                return True
            for i in range(3):
                if(l[i][col-1]!=chr(88)):
                    win1=False
            if(win1==True):
                return True
            if((l[0][0]==chr(88)and l[1][2]==chr(88) and l[2][4]==chr(88)) or (l[0][4]==chr(88) and l[1][2]==chr(88) and l[2][0]==chr(88))):
                return True
            else:
                return False
    if(turn==2):
        win2=True
        if((row-1+col-1)!=4 and (row-1+col-1)!=2 and (row-1+col-1)!=0):
            for i in range(0,5,2):
                if(l[row-1][i]!=chr(79)):
                    win2=False
            if(win2==True):
                return True
            for i in range(3):
                if(l[i][col-1]!=chr(79)):
                    win2=False
            if(win2==True):
                return True
            else:
                return False
        else:
            for i in range(0,5,2):
                if(l[row-1][i]!=chr(79)):
                    win2=False
            if(win2==True):
                return True
            for i in range(3):
                if(l[i][col-1]!=chr(79)):
                    win2=False
            if(win2==True):
                return True
            if((l[0][0]==chr(79)and l[1][2]==chr(79) and l[2][4]==chr(79)) or (l[0][4]==chr(79) and l[1][2]==chr(79) and l[2][0]==chr(79))):
                return True
            else:
                return False
    
    
        
                
            
           
def display(d):
    for i in range(3):
        for j in range(5):
            if(type(d[i][j])==int):
                print(chr(d[i][j]),format(' ','>2'),end='')
            else:
                print(d[i][j],format(' ','>2'),end='')
        if i==0 or i==1:
            print("\n-------------------")
        
print("#############    HELLO!!! Welcome to the TIC-TAC-TOE   ###################")
print("\n#############    THIS IS A TWO PLAYER GAME             ###################")
print("\n#############    PLAYER ONE PLAYS 'X'                  ###################")
print("\n#############    PLAYER TWO PLAYS 'O'                  ###################")
print("\n#############    TO PLAY YOUR TURN 'ENTER THE NUMBER OF ROW AND COLUMN seperated by space  ")
print("\nFor example , if you played 2 2 ,that means you played like this:-" )
display(D)
print("\nLet's start the game###############")
t=1
draw=False
choice='Y'
while(choice=='y'or choice=='Y'):
    l1=[32,124,32,124,32]
    l2=[32,124,32,124,32]
    l3=[32,124,32,124,32]
    l=[l1,l2,l3]
    while(t<10):
        print("\nPlayer 1 ,play your turn")
        r1,c1=map(int,input().split())
        l[r1-1][(2*c1-1)-1]=chr(88)
        display(l)
        if(check(r1,c1,1)==True):
            draw=True
            print("\nCongo!!! you won ")
            break



        print("\nPlayer 2,play your turn")
        r2,c2=map(int,input().split())
        l[r2-1][(2*c2-1)-1]=chr(79)
        display(l)
        if(check(r2,c2,2)==True):
            draw=True
            print("\nCongo!!! you won")
            break
        t=t+1
    
    if(draw==False):
        print("\nGame result in draw")
    print("\nDo you want to play again!! press 'Y' for yes and 'N' for no")
    choice=input()
