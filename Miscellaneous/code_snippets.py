# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Code_snippets

class ScriptWorkbench (Workbench): 
    MenuText = "Scripts"
    def Initialize(self):
        import Scripts # assuming Scripts.py is your module
        list = ["Script_Cmd"] # That list must contain command names, that can be defined in Scripts.py
        self.appendToolbar("My Scripts",list) 
        
Gui.addWorkbench(ScriptWorkbench())

import FreeCAD, FreeCADGui 
 
class ScriptCmd: 
   def Activated(self): 
       # Here your write what your ScriptCmd does...
       FreeCAD.Console.PrintMessage('Hello, World!')
   def GetResources(self): 
       return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'More detailed text'} 
       
FreeCADGui.addCommand('Script_Cmd', ScriptCmd())

# Assumes Import_Ext.py is the file that has the code for opening and reading .ext files
FreeCAD.addImportType("Your new File Type (*.ext)","Import_Ext")

def open(filename): 
   doc=App.newDocument()
   # here you do all what is needed with filename, read, classify data, create corresponding FreeCAD objects
   doc.recompute()

FreeCAD.addExportType("Your new File Type (*.ext)","Export_Ext")

import Part,PartGui 
doc=App.activeDocument() 
# add a line element to the document and set its points 
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute()

import Part, PartGui 
doc = App.activeDocument()
n = list() 

# create a 3D vector, set its coordinates and add it to the list 
v = App.Vector(0,0,0) 
n.append(v) 
v = App.Vector(10,0,0) 
n.append(v) 
#... repeat for all nodes 

# Create a polygon object and set its nodes 
p = doc.addObject("Part::Polygon","Polygon") 
p.Nodes = n 
doc.recompute()

doc=App.activeDocument() 
grp=doc.addObject("App::DocumentObjectGroup", "Group") 
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp

import Mesh
doc=App.activeDocument()
# create a new empty mesh
m = Mesh.Mesh()
# build up box out of 12 facets
m.addFacet(0.0,0.0,0.0, 0.0,0.0,1.0, 0.0,1.0,1.0)
m.addFacet(0.0,0.0,0.0, 0.0,1.0,1.0, 0.0,1.0,0.0)
m.addFacet(0.0,0.0,0.0, 1.0,0.0,0.0, 1.0,0.0,1.0)
m.addFacet(0.0,0.0,0.0, 1.0,0.0,1.0, 0.0,0.0,1.0)
m.addFacet(0.0,0.0,0.0, 0.0,1.0,0.0, 1.0,1.0,0.0)
m.addFacet(0.0,0.0,0.0, 1.0,1.0,0.0, 1.0,0.0,0.0)
m.addFacet(0.0,1.0,0.0, 0.0,1.0,1.0, 1.0,1.0,1.0)
m.addFacet(0.0,1.0,0.0, 1.0,1.0,1.0, 1.0,1.0,0.0)
m.addFacet(0.0,1.0,1.0, 0.0,0.0,1.0, 1.0,0.0,1.0)
m.addFacet(0.0,1.0,1.0, 1.0,0.0,1.0, 1.0,1.0,1.0)
m.addFacet(1.0,1.0,0.0, 1.0,1.0,1.0, 1.0,0.0,1.0)
m.addFacet(1.0,1.0,0.0, 1.0,0.0,1.0, 1.0,0.0,0.0)
# scale to a edge langth of 100
m.scale(100.0)
# add the mesh to the active document
me=doc.addObject("Mesh::Feature","Cube")
me.Mesh=m

import Part
doc = App.activeDocument()
c = Part.Circle() 
c.Radius=10.0  
f = doc.addObject("Part::Feature", "Circle") # create a document with a circle feature 
f.Shape = c.toShape() # Assign the circle shape to the shape property 
doc.recompute()

gad = Gui.activeDocument() # access the active document containing all 
                           # view representations of the features in the
                           # corresponding App document 

v = gad.getObject("Cube")  # access the view representation to the Mesh feature 'Cube' 
v.ShapeColor               # prints the color to the console 
v.ShapeColor=(1.0,1.0,1.0) # sets the shape color to white

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QColor, QPixmap, QImage, QPainter, QCursor
from PySide2.QtCore import Qt

myImage = QtGui.QPixmap("Complete_Path_to_image.bmp")
cursor = QtGui.QCursor(myImage)
QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(cursor))

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QColor, QPixmap, QImage, QPainter, QCursor
from PySide2.QtCore import Qt

cross32x32Icon = [
"32 32 2 1",
" 	c None",
".	c #FF0000",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                                ",
"............... . ..............",
"                                ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               ",
"                .               "
]

myImage = QtGui.QPixmap(cross32x32Icon)
cursor = QtGui.QCursor(myImage)
QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(cursor))

App.newDocument()
v=Gui.activeDocument().activeView()
 
#This class logs any mouse button events. As the registered callback function fires twice for 'down' and
#'up' events we need a boolean flag to handle this.
class ViewObserver:
   def logPosition(self, info):
       down = (info["State"] == "DOWN")
       pos = info["Position"]
       if (down):
           FreeCAD.Console.PrintMessage("Clicked on position: ("+str(pos[0])+", "+str(pos[1])+")\n")
       
o = ViewObserver()
c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)

v.removeEventCallback("SoMouseButtonEvent",c)

App.newDocument()
v=Gui.activeDocument().activeView()
class ViewObserver:
   def logPosition(self, info):
       try:
           down = (info["Key"])
           FreeCAD.Console.PrintMessage(str(down)+"\n") # here the character pressed
           FreeCAD.Console.PrintMessage(str(info)+"\n") # list all events command
           FreeCAD.Console.PrintMessage("_______________________________________"+"\n")
       except Exception:
           None
 
o = ViewObserver()
c = v.addEventCallback("SoEvent",o.logPosition)

#v.removeEventCallback("SoEvent",c) # remove ViewObserver

from pivy.coin import *                # load the pivy module
view = Gui.ActiveDocument.ActiveView   # get the active viewer
root = view.getSceneGraph()            # the root is an SoSeparator node
root.addChild(SoCube())
view.fitAll()

type = SoType.fromName("SoFCSelection")
node = type.createInstance()

from pivy import coin
sg = Gui.ActiveDocument.ActiveView.getSceneGraph()
co = coin.SoCoordinate3()
pts = [[0,0,0],[10,0,0]]
co.point.setValues(0,len(pts),pts)
ma = coin.SoBaseColor()
ma.rgb = (1,0,0)
li = coin.SoLineSet()
li.numVertices.setValue(2)
no = coin.SoSeparator()
no.addChild(co)
no.addChild(ma)
no.addChild(li)
sg.addChild(no)

sg.removeChild(no)

class myWidget_Ui(object):
    def setupUi(self, myWidget):
        myWidget.setObjectName("my Nice New Widget")
        myWidget.resize(QtCore.QSize(QtCore.QRect(0,0,300,100).size()).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget
 
        self.label = QtGui.QLabel(myWidget) # creates a label
        self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
        self.label.setObjectName("label") # sets its name, so it can be found by name

    def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
        myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))

app = QtGui.qApp
FCmw = app.activeWindow() # the active qt window, = the freecad window since we are inside it
# FCmw = FreeCADGui.getMainWindow() # use this line if the 'addDockWidget' error is declared
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window

# create new Tab in ComboView
from PySide import QtGui,QtCore
#from PySide import uic

def getMainWindow():
   "returns the main window"
   # using QtGui.qApp.activeWindow() isn't very reliable because if another
   # widget than the mainwindow is active (e.g. a dialog) the wrong widget is
   # returned
   toplevel = QtGui.qApp.topLevelWidgets()
   for i in toplevel:
       if i.metaObject().className() == "Gui::MainWindow":
           return i
   raise Exception("No main window found")

def getComboView(mw):
   dw=mw.findChildren(QtGui.QDockWidget)
   for i in dw:
       if str(i.objectName()) == "Combo View":
           return i.findChild(QtGui.QTabWidget)
       elif str(i.objectName()) == "Python Console":
           return i.findChild(QtGui.QTabWidget)
   raise Exception ("No tab widget found")

mw = getMainWindow()
tab = getComboView(getMainWindow())
tab2=QtGui.QDialog()
tab.addTab(tab2,"A Special Tab")

#uic.loadUi("/myTaskPanelforTabs.ui",tab2)
tab2.show()
#tab.removeTab(2)

from PySide import QtGui
mw = FreeCADGui.getMainWindow()
dws = mw.findChildren(QtGui.QDockWidget)

# objectName may be :
# "Report view"
# "Tree view"
# "Property view"
# "Selection view"
# "Combo View"
# "Python console"
# "draftToolbar"

for i in dws:
  if i.objectName() == "Report view":
    dw = i
    break

va = dw.toggleViewAction()
va.setChecked(True)        # True or False
dw.setVisible(True)        # True or False

import WebGui
WebGui.openBrowser("http://www.example.com")

from PySide import QtGui,QtWebKit
a = QtGui.qApp
mw = a.activeWindow()
v = mw.findChild(QtWebKit.QWebFrame)
html = unicode(v.toHtml())
print( html)

# -*- coding: utf-8 -*-
# the line above to put the accentuated in the remarks
# If this line is missing, an error will be returned
# extract and use the coordinates of 3 objects selected
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base, Console
sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
if len(sel)!=3 :
  # If there are no 3 objects selected, an error is displayed in the report view
  # The \r and \n at the end of line mean return and the newline CR + LF.
  Console.PrintError("Select 3 points exactly\r\n")
else :
  points=[]
  for obj in sel:
    points.append(obj.Shape.BoundBox.Center)

  for pt in points:
    # display of the coordinates in the report view
    Console.PrintMessage(str(pt.x)+"\r\n")
    Console.PrintMessage(str(pt.y)+"\r\n")
    Console.PrintMessage(str(pt.z)+"\r\n")

  Console.PrintMessage(str(pt[1]) + "\r\n")

# -*- coding: utf-8 -*-
import FreeCAD,Draft
# List all objects of the document
doc = FreeCAD.ActiveDocument
objs = FreeCAD.ActiveDocument.Objects
#App.Console.PrintMessage(str(objs) + "\n")
#App.Console.PrintMessage(str(len(FreeCAD.ActiveDocument.Objects)) + " Objects"  + "\n")

for obj in objs:
    a = obj.Name                                             # list the Name  of the object  (not modifiable)
    b = obj.Label                                            # list the Label of the object  (modifiable)
    try:
        c = obj.LabelText                                    # list the LabeText of the text (modifiable)
        App.Console.PrintMessage(str(a) +" "+ str(b) +" "+ str(c) + "\n") # Displays the Name the Label and the text
    except:
        App.Console.PrintMessage(str(a) +" "+ str(b) + "\n") # Displays the Name and the Label of the object

#doc.removeObject("Box") # Clears the designated object

for edge in FreeCAD.ActiveDocument.MyObjectName.Shape.Edges: # replace "MyObjectName" for list
    print( edge.Length)

# -*- coding: utf-8 -*-
# causes an action to the mouse click on an object
# This function remains resident (in memory) with the function "addObserver(s)"
# "removeObserver(s) # Uninstalls the resident function
class SelObserver:
    def setPreselection(self,doc,obj,sub):                # Preselection object
        App.Console.PrintMessage(str(sub)+ "\n")          # The part of the object name

    def addSelection(self,doc,obj,sub,pnt):               # Selection object
        App.Console.PrintMessage("addSelection"+ "\n")
        App.Console.PrintMessage(str(doc)+ "\n")          # Name of the document
        App.Console.PrintMessage(str(obj)+ "\n")          # Name of the object
        App.Console.PrintMessage(str(sub)+ "\n")          # The part of the object name
        App.Console.PrintMessage(str(pnt)+ "\n")          # Coordinates of the object
        App.Console.PrintMessage("______"+ "\n")

    def removeSelection(self,doc,obj,sub):                # Delete the selected object
        App.Console.PrintMessage("removeSelection"+ "\n")

    def setSelection(self,doc):                           # Selection in ComboView
        App.Console.PrintMessage("setSelection"+ "\n")

    def clearSelection(self,doc):                         # If click on the screen, clear the selection
        App.Console.PrintMessage("clearSelection"+ "\n")  # If click on another object, clear the previous object
s =SelObserver()
FreeCADGui.Selection.addObserver(s)                       # install the function mode resident
#FreeCADGui.Selection.removeObserver(s)                   # Uninstall the resident function

App.newDocument()
v=Gui.activeDocument().activeView()
 
#This class logs any mouse button events. As the registered callback function fires twice for 'down' and
#'up' events we need a boolean flag to handle this.
class ViewObserver:
   def __init__(self, view):
       self.view = view
   
   def logPosition(self, info):
       down = (info["State"] == "DOWN")
       pos = info["Position"]
       if (down):
           FreeCAD.Console.PrintMessage("Clicked on position: ("+str(pos[0])+", "+str(pos[1])+")\n")
           pnt = self.view.getPoint(pos)
           FreeCAD.Console.PrintMessage("World coordinates: " + str(pnt) + "\n")
           info = self.view.getObjectInfo(pos)
           FreeCAD.Console.PrintMessage("Object info: " + str(info) + "\n")

o = ViewObserver(v)
c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)

from pivy import coin
import FreeCADGui

def mouse_over_cb( event_callback):
    event = event_callback.getEvent()
    pos = event.getPosition().getValue()
    listObjects = FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo((int(pos[0]),int(pos[1])))
    obj = []
    if listObjects:
        FreeCAD.Console.PrintMessage("\n *** Objects under mouse pointer ***")
        for o in listObjects:
            label = str(o["Object"])
            if not label in obj:
                obj.append(label)
        FreeCAD.Console.PrintMessage("\n"+str(obj))


view = FreeCADGui.ActiveDocument.ActiveView

mouse_over = view.addEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over_cb )

# to remove Callback :
#view.removeEventCallbackPivy( coin.SoLocation2Event.getClassTypeId(), mouse_over)

####
#The easy way is probably to use FreeCAD's selection.
#FreeCADGui.ActiveDocument.ActiveView.getObjectsInfo(mouse_coords)

####
#you get that kind of result :
#'Document': 'Unnamed', 'Object': 'Box', 'Component': 'Face2', 'y': 8.604081153869629, 'x': 21.0, 'z': 8.553047180175781

####
#You can use this data to add your element to FreeCAD's selection :
#FreeCADGui.Selection.addSelection(FreeCAD.ActiveDocument.Box,'Face2',21.0,8.604081153869629,8.553047180175781)

import FreeCADGui
from FreeCAD import Console
o = App.ActiveDocument.ActiveObject
op = o.PropertiesList
for p in op:
    Console.PrintMessage("Property: "+ str(p)+ " Value: " + str(o.getPropertyByName(p))+"\r\n")

import Draft
obj = FreeCADGui.Selection.getSelection()[0]
obj.addProperty("App::PropertyString","GComment","Draft","Font name").GComment = "Comment here"
App.activeDocument().recompute()

# Extract the coordinate X,Y,Z and Angle giving the label (here "Cylindre")
App.Console.PrintMessage("Base.x       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.x)+"\n")
App.Console.PrintMessage("Base.y       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.y)+"\n")
App.Console.PrintMessage("Base.z       : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Base.z)+"\n")
App.Console.PrintMessage("Base.Angle   : "+str(FreeCAD.ActiveDocument.getObjectsByLabel("Cylindre")[0].Placement.Rotation.Angle)+"\n\n")
##################################################################################

numberOfPoints = 100                                                         # Decomposition number (or precision you can change)
selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy() # select one element
points  = selectedEdge.discretize(numberOfPoints)                            # discretize the element
i=0
for p in points:                                                             # list and display the coordinates
    i+=1
    print( i, " X", p.x, " Y", p.y, " Z", p.z)

import Part
from FreeCAD import Base

c=Part.makeCylinder(2,10)        # create the circle
Part.show(c)                     # display the shape

# slice accepts two arguments:
#+ the normal of the cross section plane
#+ the distance from the origin to the cross section plane. Here you have to find a value so that the plane intersects your object
s=c.slice(Base.Vector(0,1,0),0)  # 

# here the result is a single wire
# depending on the source object this can be several wires
s=s[0]

# if you only need the vertexes of the shape you can use
v=[]
for i in s.Vertexes:
    v.append(i.Point)

# but you can also sub-sample the section to have a certain number of points (int) ...
p1=s.discretize(20)
ii=0
for i in p1:
    ii+=1
    print( i )                                             # Vector()
    print( ii, ": X:", i.x, " Y:", i.y, " Z:", i.z )       # Vector decode
Draft.makeWire(p1,closed=False,face=False,support=None)    # to see the difference accuracy (20)

## uncomment to use
#import Draft
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # first transform the DWire in Wire         "downgrade"
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # second split the Wire in single objects   "downgrade"
#
##Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True) # to attach lines contiguous SELECTED use "upgrade"


# ... or define a sampling distance (float)
p2=s.discretize(0.5)
ii=0
for i in p2:
    ii+=1
    print( i )                                             # Vector()
    print( ii, ": X:", i.x, " Y:", i.y, " Z:", i.z )       # Vector decode 
Draft.makeWire(p2,closed=False,face=False,support=None)  # to see the difference accuracy (0.5)

## uncomment to use
#import Draft
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # first transform the DWire in Wire         "downgrade"
#Draft.downgrade(App.ActiveDocument.ActiveObject,delete=True)  # second split the Wire in single objects   "downgrade"
#
##Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True) # to attach lines contiguous SELECTED use "upgrade"

import FreeCAD
for obj in FreeCAD.ActiveDocument.Objects:
    print( obj.Name )                               # display the object Name
    objName = obj.Name
    obj = App.ActiveDocument.getObject(objName)
    Gui.Selection.addSelection(obj)                 # select the object

# select one face of the object
import FreeCAD, Draft
App=FreeCAD
nameObject = "Box"                             # objet
faceSelect = "Face3"                           # face to selection
loch=App.ActiveDocument.getObject(nameObject)  # objet
Gui.Selection.clearSelection()                 # clear all selection
Gui.Selection.addSelection(loch,faceSelect)    # select the face specified
s = Gui.Selection.getSelectionEx()
#Draft.makeFacebinder(s)                       #

## normal of a face by giving the number of the face and the name of the object (rotation Q with yL, uV) = (App.Vector (x, y, z), angle))
## normal d'une face en donnant le numero de la face et le nom de l'objet (rotation Q avec yL, uV) = (App.Vector(x, y, z),angle))
from FreeCAD import Vector

numero_Face = 2      # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"  # object name
yL = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].CenterOfMass
uv = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].Surface.parameter(yL)

nv = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(uv[0], uv[1])
direction = yL.sub(nv + yL)
print("Direction  : ",direction)

r = App.Rotation(App.Vector(0,0,1),direction)
print("Rotation   : ", r)
print("Rotation Q : ", r.Q)

numero_Face = 2       # number of the face searched (begin 0, 1, 2, 3 .....)
nomObjet    = "Box"   # object name
normal      = Gui.ActiveDocument.getObject(nomObjet).Object.Shape.Faces[numero_Face].normalAt(0,0)
print("Face"+str(numero_Face), " : ", normal)

## normal of a face by giving the number of the face of the selected object
selectionObjects = FreeCADGui.Selection.getSelection()     
numero_Face = 3    # numero de la face recherchee
normal = selectionObjects[0].Shape.Faces[numero_Face].normalAt(0,0)
print(normal)
# selectionne la face numerotee
Gui.Selection.clearSelection()
Gui.Selection.addSelection(selectionObjects[0],"Face"+str(numero_Face))

def normal(self):
   ss=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy()#SubObjects[0] is the edge list
   points  = ss.discretize(3.0)#points on the surface edge, 
             #this example just use points on the edge for example. 
             #However point is not necessary on the edge, it can be anywhere on the surface. 
   face=FreeCADGui.Selection.getSelectionEx()[0].SubObjects[1]
   for pp in points:
      pt=FreeCAD.Base.Vector(pp.x,pp.y,pp.z)#a point on the surface edge
      uv=face.Surface.parameter(pt)# find the surface u,v parameter of a point on the surface edge
      u=uv[0]
      v=uv[1]
      normal=face.normalAt(u,v)#use u,v to find normal vector
      print( normal)
      line=Part.makeLine((pp.x,pp.y,pp.z), (normal.x,normal.y,normal.z))
      Part.show(line)

def getNormal(cb):
    if cb.getEvent().getState() == coin.SoButtonEvent.UP:
        pp = cb.getPickedPoint()
        if pp:
            vec = pp.getNormal().getValue()
            index = coin.cast(pp.getDetail(), "SoFaceDetail").getFaceIndex()
            print("Normal: {}, Face index: {}".format(str(vec), index))

from pivy import coin
meth=Gui.ActiveDocument.ActiveView.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), getNormal)

# create one object of the position to camera with "getCameraOrientation()"
# the object is still facing the screen
import Draft

plan = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
plan = str(plan)
###### extract data
a    = ""
for i in plan:
    if i in ("0123456789e.- "):
        a+=i
a = a.strip(" ")
a = a.split(" ")
####### extract data

#print( a)
#print( a[0])
#print( a[1])
#print( a[2])
#print( a[3])

xP = float(a[0])
yP = float(a[1])
zP = float(a[2])
qP = float(a[3])

pl = FreeCAD.Placement()
pl.Rotation.Q = (xP,yP,zP,qP)         # rotation of object
pl.Base = FreeCAD.Vector(0.0,0.0,0.0) # here coordinates XYZ of Object
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None) # create rectangle
#rec = Draft.makeCircle(radius=5,placement=pl,face=False,support=None)                   # create circle
print( rec.Name)

import Draft
pl = FreeCAD.Placement()
pl.Rotation = FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
pl.Base = FreeCAD.Vector(0.0,0.0,0.0)
rec = Draft.makeRectangle(length=10.0,height=10.0,placement=pl,face=False,support=None)

import Draft
doc = FreeCAD.ActiveDocument

pl=FreeCAD.Placement()
pl.Rotation.Q=(0.0,-0.0,-0.0,1.0)
pl.Base=FreeCAD.Vector(0.0,0.0,0.0)
obj = Draft.makeCircle(radius=1.0,placement=pl,face=False,support=None)    # create circle

print( obj.PropertiesList )                                                  # properties disponible in the obj

doc.getObject(obj.Name).setExpression('Radius', u'2mm')                    # modify the radius
doc.getObject(obj.Name).setExpression('Placement.Base.x', u'10mm')         # modify the placement 
doc.getObject(obj.Name).setExpression('FirstAngle', u'90')                 # modify the first angle
doc.recompute()

expressions = obj.ExpressionEngine                                         # read the expression list
print( expressions)

for i in expressions:                                                      # list and separate the data expression
    print( i[0]," = ",i[1])

Gui.ActiveDocument.ActiveView.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), meth)

body = Gui.ActiveDocument.ActiveView.getActiveObject('pdbody')
first_selection = Gui.Selection.getSelectionEx()[0]

feature = first_selection.Object
face_name = first_selection.SubElementNames[0]

sketch = App.ActiveDocument.addObject('Sketcher::SketchObject','MySketch')
body.addObject(sketch)
sketch.MapMode = 'FlatFace'
sketch.Support = (feature, face_name)

App.ActiveDocument.recompute()

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

mw = Gui.getMainWindow()
gl = mw.findChild(QtWidgets.QOpenGLWidget)
me = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, QtCore.QPoint(800,300), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)

app = QtWidgets.QApplication.instance()
app.sendEvent(gl, me)


