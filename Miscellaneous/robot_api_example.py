# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Robot_API_example

from Robot import *
from Part import *
from FreeCAD import *

rob = Robot6Axis()
print(rob)

Start = rob.Tcp
print Start
print rob.Axis1

rob.Axis1 = 5.0

print rob.Tcp

rob.Tcp = Start
print rob.Axis1

rob.Axis2 = 5.0
print rob.Tcp
rob.Tcp = Start
print rob.Axis2

w = Waypoint(Placement(),name="Pt",type="LIN")
print w.Name,w.Type,w.Pos,w.Cont,w.Velocity,w.Base,w.Tool

l = [w]
for i in range(5):
  l.append(Waypoint(Placement(Vector(0,0,i*100),Vector(1,0,0),0),"LIN","Pt"))

t = Trajectory(l)
print t
for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,0,i*100+500),Vector(1,0,0),0),"LIN","Pt"))

print t.Waypoints
 
del rob,Start,t,l,w

if(App.activeDocument() == None):App.newDocument()
 
App.activeDocument().addObject("Robot::RobotObject","Robot")

App.activeDocument().Robot.RobotVrmlFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.wrl"
App.activeDocument().Robot.RobotKinematicFile = App.getResourceDir()+"Mod/Robot/Lib/Kuka/kr500_1.csv"

App.activeDocument().Robot.Axis2 = -90
App.activeDocument().Robot.Axis3 = 90

pos = FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp

pos.move(App.Vector(-10,0,0))
FreeCAD.getDocument("Unnamed").getObject("Robot").Tcp = pos

App.activeDocument().addObject("Robot::TrajectoryObject","Trajectory")

t = App.activeDocument().Trajectory.Trajectory

StartTcp = App.activeDocument().Robot.Tcp
t.insertWaypoints(StartTcp)
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory

for i in range(7):
  t.insertWaypoints(Waypoint(Placement(Vector(0,1000,i*100+500),Vector(1,0,0),i),"LIN","Pt"))

t.insertWaypoints(StartTcp) # end point of the trajectory
App.activeDocument().Trajectory.Trajectory = t
print App.activeDocument().Trajectory.Trajectory

from KukaExporter import ExportCompactSub

ExportCompactSub(App.activeDocument().Robot,App.activeDocument().Trajectory,'D:/Temp/TestOut.src')

for w in App.activeDocument().Trajectory.Trajectory.Waypoints:
	(A,B,C) = (w.Pos.Rotation.toEuler())
	print ("LIN {X %.3f,Y %.3f,Z %.3f,A %.3f,B %.3f,C %.3f} ; %s"%(w.Pos.Base.x,w.Pos.Base.y,w.Pos.Base.z,A,B,C,w.Name))
