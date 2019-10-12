import math

print("We assume that the bullet is 7,62 x 39 mm ")
print("And from Wikipedia we know that the velocity of the bullet is 730.3 m/s")
angle= input("Input the angle of launch(in degrees) : ")
height=input("Input your height when shoot the bullet: ")


velocity = 730.3
g= 9.8
# vx= velocity* math.cos(angle)
# vy = velocity * math.sin(angle)
# time= 2*vy/g 
vy=-1
vx=-1
range_projectile=0
hmax=0
height=0
# x_hor_dist= velocity* time 
# y_ver_dist= height+vy*t
if(height==0):
    vx=int(velocity)*(math.cos(int(angle)))
    vy= int(velocity)*math.sin(int(angle))
    time=2*vy/g
    range_projectile=2*vx*vy/g
    hmax=((vy)**2)/(2*g)

elif(height>0):
    vx=velocity*math.cos(int(angle))
    vy= velocity*math.sin(int(angle))
    time=(vy+ sqrt((vy)**2)+2*g*height)/g
    range_projectile= vx*(vy+sqrt((vy)**2)+2*g*height)/g
    hmax=height+((vy)**2)/(2*g)


print("so the bullet projection will be: {} at {} height".format(range_projectile,hmax))