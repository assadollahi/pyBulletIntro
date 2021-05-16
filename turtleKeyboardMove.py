
import pybullet as p
import time

# open the GUI
p.connect(p.GUI)

# load files and place them at the offsets
turtle = p.loadURDF("urdf/most_simple_turtle.urdf",[0,0,0])
plane = p.loadURDF("urdf/plane_box.urdf")
box1 = p.loadURDF("urdf/box.urdf", [1,0,0])
box2 = p.loadURDF("urdf/box.urdf", [1,1,0])

# enable real time simulation
p.setRealTimeSimulation(1)

# define gravity
p.setGravity(0,0,-10)

# for debug print out the joints of the turtle
for j in range (p.getNumJoints(turtle)):
	print(p.getJointInfo(turtle,j))
	
forward=0
turn=0
while (1):

	time.sleep(1./240.)
	keys = p.getKeyboardEvents()
	
	leftWheelVelocity=0
	rightWheelVelocity=0
	speed=10
	
	for k,v in keys.items():

                if (k == p.B3G_RIGHT_ARROW and (v&p.KEY_WAS_TRIGGERED)):
                        turn = -0.5
                if (k == p.B3G_RIGHT_ARROW and (v&p.KEY_WAS_RELEASED)):
                        turn = 0
                if (k == p.B3G_LEFT_ARROW and (v&p.KEY_WAS_TRIGGERED)):
                        turn = 0.5
                if (k == p.B3G_LEFT_ARROW and (v&p.KEY_WAS_RELEASED)):
                        turn = 0

                if (k == p.B3G_UP_ARROW and (v&p.KEY_WAS_TRIGGERED)):
                        forward=1
                if (k == p.B3G_UP_ARROW and (v&p.KEY_WAS_RELEASED)):
                        forward=0
                if (k == p.B3G_DOWN_ARROW and (v&p.KEY_WAS_TRIGGERED)):
                        forward=-1
                if (k == p.B3G_DOWN_ARROW and (v&p.KEY_WAS_RELEASED)):
                        forward=0

	rightWheelVelocity+= (forward+turn)*speed
	leftWheelVelocity += (forward-turn)*speed
	
	p.setJointMotorControl2(turtle,0,p.VELOCITY_CONTROL,targetVelocity=leftWheelVelocity,force=1000)
	p.setJointMotorControl2(turtle,1,p.VELOCITY_CONTROL,targetVelocity=rightWheelVelocity,force=1000)
