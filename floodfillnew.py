from queue import Queue
import API
import sys

x=0
y=0
orient=0
cell = 0

def log(string):
    sys.stderr.write("{}\n".format(string))

cells = [[0] * 16 for _ in range(16)]    

flood2 = [[0] * 16 for _ in range(16)]

flood=[[14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14],
        [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
        [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
        [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
        [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
        [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
        [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
        [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
        [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
        [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
        [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
        [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
        [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
        [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
        [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
        [14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14]]

def orientation(orient,turn):
    if (turn== 'L'):
        orient-=1
        if (orient==-1):
            orient=3
    elif(turn== 'R'):
        orient+=1
        if (orient==4):
            orient=0
    elif(turn== 'B'):
        if (orient==0):
            orient=2
        elif (orient==1):
            orient=3
        elif (orient==2):
            orient=0
        elif (orient==3):
            orient=1

    return(orient)

def updateCoordinates(x,y,orient):

    if (orient==0):
        y+=1
    if (orient==1):
        x+=1
    if (orient==2):
        y-=1
    if (orient==3):
        x-=1

    return(x,y)

def updateWalls(x, y, orient, L, R, F):
    if L and R and F:
        walls = {0: 13, 1: 12, 2: 11, 3: 14}
    elif L and R and not F:
        walls = {0: 9, 1: 10, 2: 9, 3: 10}
    elif L and F and not R:
        walls = {0: 8, 1: 7, 2: 6, 3: 5}
    elif R and F and not L:
        walls = {0: 7, 1: 6, 2: 5, 3: 8}
    elif F:
        walls = {0: 2, 1: 3, 2: 4, 3: 1}
    elif L:
        walls = {0: 1, 1: 2, 2: 3, 3: 4}
    elif R:
        walls = {0: 3, 1: 4, 2: 1, 3: 2}
    else:
        walls = {0: 15, 1: 15, 2: 15, 3: 15}

    cells[y][x] = walls[orient]

def isAccessible(x, y, x1, y1):
   
      horizontal_wall = {
        "down": [4, 5, 6, 10, 11, 12, 14],
        "up": [2, 7, 8, 10, 12, 13, 14]
    }
    
      vertical_wall = {
        "left": [1, 5, 8, 9, 11, 13, 14],
        "right": [3, 6, 7, 9, 11, 12, 13]
    }

      if x == x1:
          if y > y1:
           
              if cells[y][x] in horizontal_wall["down"] or cells[y1][x1] in horizontal_wall["up"]:
                 return False
          else:
            
            if cells[y][x] in horizontal_wall["up"] or cells[y1][x1] in horizontal_wall["down"]:
                return False
      elif y == y1:
         if x > x1:
           
            if cells[y][x] in vertical_wall["left"] or cells[y1][x1] in vertical_wall["right"]:
                return False
         else:
           
            if cells[y][x] in vertical_wall["right"] or cells[y1][x1] in vertical_wall["left"]:
                return False

         return True

def getSurrounds(x,y):
    x3= x-1
    y3=y
    x0=x
    y0=y+1
    x1=x+1
    y1=y
    x2=x
    y2=y-1
    if(x1>=16):
        x1=-1
    if(y0>=16):
        y0=-1
    return (x0,y0,x1,y1,x2,y2,x3,y3)

def changeDestination(maze,destinationx, destinationy):
    for j in range(16):
        for i in range(16):
            flood[i][j]=255

    queue=[]
    maze[destinationy][destinationx]=0

    queue.append(destinationy)
    queue.append(destinationx)

    
    while (len(queue)!=0):
        yrun=queue.pop(0)
        xrun=queue.pop(0)

        x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(xrun,yrun)
        if(x0>=0 and y0>=0 ):
            if (maze[y0][x0]==255):
                maze[y0][x0]=maze[yrun][xrun]+1
                queue.append(y0)
                queue.append(x0)
        if(x1>=0 and y1>=0 ):
            if (maze[y1][x1]==255):
                maze[y1][x1]=maze[yrun][xrun]+1
                queue.append(y1)
                queue.append(x1)
        if(x2>=0 and y2>=0 ):
            if (maze[y2][x2]==255):
                maze[y2][x2]=maze[yrun][xrun]+1
                queue.append(y2)
                queue.append(x2)
        if(x3>=0 and y3>=0 ):
            if (maze[y3][x3]==255):
                maze[y3][x3]=maze[yrun][xrun]+1
                queue.append(y3)
                queue.append(x3)

def floodFill2(maze):
    for i in range(16):
        for j in range(16):
            maze[i][j]=0

    queue=[]
    flood2[7][7]=1
    flood2[8][7]=1
    flood2[7][8]=1
    flood2[8][8]=1

    queue.append(7,7,8,7,7,8,8,8)
    
    while (len(queue)!=0):
        yrun=queue.pop(0)
        xrun=queue.pop(0)

        x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(xrun,yrun)
        if(x0>=0 and y0>=0 and cells[y0][x0]!=0):
            if (maze[y0][x0]==0):
                if (isAccessible(xrun,yrun,x0,y0)):
                    maze[y0][x0]=maze[yrun][xrun]+1
                    queue.append(y0)
                    queue.append(x0)
        if(x1>=0 and y1>=0 and cells[y1][x1]!=0):
            if (maze[y1][x1]==0):
                if (isAccessible(xrun,yrun,x1,y1)):
                    maze[y1][x1]=maze[yrun][xrun]+1
                    queue.append(y1)
                    queue.append(x1)
        if(x2>=0 and y2>=0 and cells[y2][x2]!=0):
            if (maze[y2][x2]==0):
                if (isAccessible(xrun,yrun,x2,y2)):
                    maze[y2][x2]=maze[yrun][xrun]+1
                    queue.append(y2)
                    queue.append(x2)
        if(x3>=0 and y3>=0 and cells[y3][x3]!=0):
            if (maze[y3][x3]==0):
                if (isAccessible(xrun,yrun,x3,y3)):
                    maze[y3][x3]=maze[yrun][xrun]+1
                    queue.append(y3)
                    queue.append(x3)

def floodFill3(maze,queue):

    while (len(queue)!=0):
        yrun=queue.pop(0)
        xrun=queue.pop(0)

        x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(xrun,yrun)
        if(x0>=0 and y0>=0 ):
            if (maze[y0][x0]==255):
                if (isAccessible(xrun,yrun,x0,y0)):
                    maze[y0][x0]=maze[yrun][xrun]+1
                    queue.append(y0)
                    queue.append(x0)
        if(x1>=0 and y1>=0):
            if (maze[y1][x1]==255):
                if (isAccessible(xrun,yrun,x1,y1)):
                    maze[y1][x1]=maze[yrun][xrun]+1
                    queue.append(y1)
                    queue.append(x1)
        if(x2>=0 and y2>=0 ):
            if (maze[y2][x2]==255):
                if (isAccessible(xrun,yrun,x2,y2)):
                    maze[y2][x2]=maze[yrun][xrun]+1
                    queue.append(y2)
                    queue.append(x2)
        if(x3>=0 and y3>=0 ):
            if (maze[y3][x3]==255):
                if (isAccessible(xrun,yrun,x3,y3)):
                    maze[y3][x3]=maze[yrun][xrun]+1
                    queue.append(y3)
                    queue.append(x3)

def toMove(maze,x,y,xprev,yprev,orient):

    x0,y0,x1,y1,x2,y2,x3,y3 = getSurrounds(x,y)
    val= maze[y][x]
    prev=0
    minVals=[1000,1000,1000,1000]

    if (isAccessible(x,y,x0,y0)):
        if (x0==xprev and y0==yprev):
            prev=0
        minVals[0]= maze[y0][x0]

    if (isAccessible(x,y,x1,y1)):
        if (x1==xprev and y1==yprev):
            prev=1
        minVals[1]= maze[y1][x1]

    if (isAccessible(x,y,x2,y2)):
        if (x2==xprev and y2==yprev):
            prev=2
        minVals[2]= maze[y2][x2]

    if (isAccessible(x,y,x3,y3)):
        if (x3==xprev and y3==yprev):
            prev=3
        minVals[3]= maze[y3][x3]

    minVal=minVals[0]
    minCell=0
    noMovements=0
    for i in minVals:
        if (i!=1000):
            noMovements+=1

    for i in range(4):
        if (minVals[i]<minVal):
            if (noMovements==1):
                minVal= minVals[i]
                minCell= i
            else:
                if(i==prev):
                    pass
                else:
                    minVal= minVals[i]
                    minCell= i

    if (minCell==orient):
        return ('F')
    elif((minCell==orient-1) or (minCell== orient+3)):
        return('L')
    elif ((minCell==orient+1) or (minCell== orient-3)):
        return('R')
    else:
        return('B')

def toMove2(maze,x,y,xprev,yprev,orient):

    x0,y0,x1,y1,x2,y2,x3,y3 = getSurrounds(x,y)
    val= maze[y][x]
    minCell=0
    if (isAccessible(x,y,x0,y0)):
        if (maze[y0][x0]==val-1):
            minCell=0

    if (isAccessible(x,y,x1,y1)):
        if (maze[y1][x1]==val-1):
            minCell=1

    if (isAccessible(x,y,x2,y2)):
        if (maze[y2][x2]==val-1):
            minCell=2

    if (isAccessible(x,y,x3,y3)):
        if (maze[y3][x3]==val-1):
            minCell=3


    if (minCell==orient):
        return ('F')
    elif((minCell==orient-1) or (minCell== orient+3)):
        return('L')
    elif ((minCell==orient+1) or (minCell== orient-3)):
        return('R')
    else:
        return('B')

def show(flood,variable):
    for x in range(16):
        for y in range(16):
            x0,y0,x1,y1,x2,y2,x3,y3= getSurrounds(x,y)
            a=''
            if isAccessible(x,y,x0,y0):
                a+=str(x0)
                a+=str(y0)
            if isAccessible(x,y,x1,y1):
                a+=str(x1)
                a+=str(y1)
            if isAccessible(x,y,x2,y2):
                a+=str(x2)
                a+=str(y2)
            if isAccessible(x,y,x3,y3):
                a+=str(x3)
                a+=str(y3)
                    
            API.setText(x,y,str(flood2[y][x]))

def center(x,y,orient):
    L= API.wallLeft()
    R= API.wallRight()
    F= API.wallFront()

    if (L):
        updateWalls(x,y,orient,L,R,F)

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnRight()
        orient = orientation(orient,'R')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)
        
        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnRight()
        orient = orientation(orient,'R')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnRight()
        orient = orientation(orient,'R')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)
        
        return (x,y,xprev,yprev,orient)

    else:
        updateWalls(x,y,orient,L,R,F)

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnLeft()
        orient = orientation(orient,'L')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)
        
        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnLeft()
        orient = orientation(orient,'L')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        API.turnLeft()
        orient = orientation(orient,'L')

        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)

        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        return (x,y,xprev,yprev,orient)
#done
def appendZero():

    for i in range(16):
        for j in range(16):
            flood[i][j]=255

    flood[7][7]=0
    flood[8][7]=0
    flood[7][8]=0
    flood[8][8]=0
    queue=[] 
    
    queue.append(7)
    queue.append(7)
    queue.append(8)
    queue.append(7)
    queue.append(7)
    queue.append(8)
    queue.append(8)
    queue.append(8)

def appendDestination(x,y):
    for i in range(16):
        for j in range(16):
            flood[i][j]=255

    flood[y][x]=0
    queue=[]

    queue.append(y)
    queue.append(x)

def main():
    x=0
    y=0
    xprev=0
    yprev=0
    orient=0
    state=0
    short= False
    queue=[]

    while True:
        API.setColor(x, y, 'red')
        L= API.wallLeft()
        R= API.wallRight()
        F= API.wallFront()
        updateWalls(x,y,orient,L,R,F)

        if (flood[y][x]!=0):
            
            if (state==0):
                appendZero()
            elif(state==1):
                appendDestination(15,0)
                short=False
            elif(state==2):
                appendDestination(0,0)
                short=False
            elif(state==3):
                appendZero()
                floodFill2(flood2)
                short=True
            elif(state==4):
                appendDestination(0,15)
                short=False
            elif(state==5):
                appendDestination(0,0)
                short=False
            elif(state==6):
                appendZero()
                floodFill2(flood2)
                short=True

            floodFill3(flood,queue)

        else:
            if state==5:
                appendZero()
                floodFill3(flood,queue)
                state+=1
            elif state==4:
                changeDestination(flood,0,0)
                state+=1
            elif state==3:
                changeDestination(flood,0,15)
                state+=1
            elif state==2:
                appendZero()
                floodFill3(flood,queue)
                state+=1
            elif state==1:
                changeDestination(flood,0,0)
                state+=1
            elif state==0:
                x,y,xprev,yprev,orient= center(x,y,orient)
                changeDestination(flood,15,0)
                state+=1

            floodFill2(flood2)

            
        if short:
            direction= toMove2(flood2,x,y,xprev,yprev,orient)
        else:
            direction= toMove(flood,x,y,xprev,yprev,orient)
        
        if (direction=='L'):
            API.turnLeft()
            orient = orientation(orient,'L')

        elif (direction=='R'):
            API.turnRight()
            orient = orientation(orient,'R')

        elif (direction=='B'):
            API.turnLeft()
            orient = orientation(orient,'L')
            API.turnLeft()
            orient = orientation(orient,'L')


        show(flood,state)
        API.moveForward()
        xprev=x
        yprev=y
        x,y = updateCoordinates(x,y,orient)



if __name__ == "__main__":
    main()





