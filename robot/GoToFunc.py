import math
import time
#oprional argument
#pointToGoal = true it will point to goal else it does nothing 
#
"""git add gotofunc.py
git commit -m "msg for users"
git push"""
def goTo(x, y, robot_pos, robot_angle, point_goal=True, point_angle=0, magicnum= 0.27):
    AngleNDistance = GetAngleToSpot(x,y,robot_pos, robot_angle) #0 angle to spot, 1 distance to spot
    
    MotorsSpeed = RotateToSpot(AngleNDistance[0], magicnum, AngleNDistance[1]) #0 right, 1 left 
    
    return [MotorsSpeed[0], MotorsSpeed[1]]

##################################################
##################################################
def GetAngleToSpot(x,y,robot_pos, robot_angle):
    YAxisToDest = (1-y)-(1-robot_pos["y"])
    XAxisToDest = x-robot_pos["x"]
    angle = math.atan2(YAxisToDest, XAxisToDest)
    #gets the hypo to know the distance between robot and desired location
    distanceToSpot = math.sqrt(math.pow(YAxisToDest, 2) + math.pow(XAxisToDest, 2))                   
    #print(angle) 
    #some math (copied xD) to convert the value we got into degrees so that our robot can get the direction to point at  
    if angle < 0:
        angle = 2 * math.pi + angle

    if robot_angle < 0:
        robot_angle = 2 * math.pi + robot_angle

    robotDestAngle = math.degrees(angle + robot_angle)
    robotDestAngle -= 90
    if robotDestAngle > 360:
        robotDestAngle -= 360
    #print("angle: ",  robotDestAngle, " distance: " , distanceToSpot )
    
    return [robotDestAngle, distanceToSpot]

#####################################################
#####################################################
def RotateToSpot (robotAngleFromSpot, magicnum, dst):
    #defualt values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    MagicNum = magicnum
    #67
    
    angleToTarget = 360-robotAngleFromSpot #actual rotation needed to face desires spot
    #print (angleToTarget)
    if(angleToTarget > 360): # for some reason the fieled is 360...its 400 somethin i think
        angleToTarget-=360
    #print(angleToTarget)

    right = -10
    left = -10   
    if((angleToTarget > 0 and angleToTarget <90) or (angleToTarget > 270 and angleToTarget <360)):
        if(angleToTarget >=0 and angleToTarget <180):#turn left
            left += (angleToTarget *MagicNum)
            right  +=(-angleToTarget)*MagicNum
        if(angleToTarget <= 360 and angleToTarget>=180):#turn right  
            angleToTarget = 360 - angleToTarget
            left += (-angleToTarget)*MagicNum 
            right +=  (angleToTarget*MagicNum)#*2
    else:
        right = 10
        left = 10  
        angleToTarget -= 180
        if angleToTarget < 0:
            angleToTarget+=360
        if(angleToTarget >=0 and angleToTarget <180):#turn left
            
            left -= (-angleToTarget *MagicNum)
            right  -=(angleToTarget)*MagicNum
        if(angleToTarget <= 360 and angleToTarget>=180):#turn right  
            angleToTarget = 360 - angleToTarget
            left -= (angleToTarget)*MagicNum 
            right -=  (-angleToTarget*MagicNum)#*2

    # if dst < 0.1:
    #     right = right*dst*20
    #     left = left*dst*20
    #if motors speed exceed the limit. cap em
    if(right >10):
        right= 10
    elif(right <-10):
        right= -10

    if(left >10):
        left= 10
    elif(left <-10):
        left= -10

    return [right, left]
