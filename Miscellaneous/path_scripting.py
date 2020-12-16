# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Path_scripting

import Path
c1 = Path.Command("g1x1")
c2 = Path.Command("g1y4")
c3 = Path.Command("g1 x2 y2") # spaces end newlines are not considered
p = Path.Path([c1,c2,c3])
o = App.ActiveDocument.addObject("Path::Feature","mypath")
o.Path = p
print(p.toGCode())

import Path
c=Path.Command()
c

c.Name = "G1"
c
c.Parameters= {"X":1,"Y":0}
c
c.Parameters
c.Parameters= {"X":1,"Y":0.5}
c
c.toGCode()
c2=Path.Command("G2")
c2
c3=Path.Command("G1",{"X":34,"Y":1.2})
c3
c3.Placement
c3.toGCode()
c3.setFromGCode("G1X1Y0")
c3
c4 = Path.Command("G1X4Y5")
c4

p1 = App.Placement()

p1.Base = App.Vector(3,2,1)

p1

c5=Path.Command("g1",p1)

c5

p2=App.Placement()

p2.Base = App.Vector(5,0,0)

c5

c5.Placement=p2

c5

c5.x

c5.x=10

c5

c5.y=2

c5

import Path

c1=Path.Command("g1",{"x":1,"y":0})

c2=Path.Command("g1",{"x":0,"y":2})

p=Path.Path([c1,c2])

p

p.Commands

p.Length

p.addCommands(c1)

p.toGCode()

lines = """
G0X-0.5905Y-0.3937S3000M03
G0Z0.125
G1Z-0.004F3
G1X0.9842Y-0.3937F14.17
G1X0.9842Y0.433
G1X-0.5905Y0.433
G1X-0.5905Y-0.3937
G0Z0.5
"""

slines = lines.split('\n')
p = Path.Path()
for line in slines:
    p.addCommands(Path.Command(line))

o = App.ActiveDocument.addObject("Path::Feature","mypath")
o.Path = p

# but you can also create a path directly form a piece of gcode.
# The commands will be created automatically:

p = Path.Path()
p.setFromGCode(lines)

p = Path.Path("G0 X2 Y2 G1 X0 Y2")

p

pf = App.ActiveDocument.addObject("Path::Feature","mypath")

pf

pf.Path = p

pf.Path

import Path

t1=Path.Tool()

t1

t1.Name = "12.7mm Drill Bit"

t1

t1.ToolType

t1.ToolType = "Drill"

t1.Diameter= 12.7

t1.LengthOffset = 127
t1.CuttingEdgeAngle = 59
t1.CuttingEdgeHeight = 50.8
t2 = Path.Tool("my other tool",tooltype="EndMill",diameter=10)
t2
t2.Diameter
table = Path.Tooltable()
table
table.addTools(t1)
table.addTools(t2)
table.Tools

import Path
p1 = Path.Path("G1X1")
o1 = App.ActiveDocument.addObject("Path::Feature","path1")
o1.Path=p1
p2 = Path.Path("G1Y1")
o2 = App.ActiveDocument.addObject("Path::Feature","path2")
o2.Path=p2
o3 = App.ActiveDocument.addObject("Path::FeatureCompound","compound")
o3.Group=[o1,o2]

from PathScripts import PathProject
o4 = App.ActiveDocument.addObject("Path::FeatureCompoundPython","prj")
PathProject.ObjectPathProject(o4)
o4.Group = [o3]
o4.Tooltable

from PathScripts import TooltableEditor
TooltableEditor.edit(o4)

import Part
import Path
v1 = FreeCAD.Vector(0,0,0)
v2 = FreeCAD.Vector(0,2,0)
v3 = FreeCAD.Vector(2,2,0)
v4 = FreeCAD.Vector(3,3,0)
wire = Part.makePolygon([v1,v2,v3,v4])
o = FreeCAD.ActiveDocument.addObject("Path::Feature","myPath2")
o.Path = Path.fromShape(wire)
FreeCAD.ActiveDocument.recompute()
p =  o.Path
print(p.toGCode())


import Path
f = open("/path/to/boomerangv4.ncc")
s = f.read()
p = Path.Path(s)
o = App.ActiveDocument.addObject("Path::Feature","boomerang")
o.Path = p

text = o.Path.toGCode()
print(text)
myfile = open("/path/to/newfile.ngc")
myfile.write(text)
myfile.close()

import example_pre
example_pre.insert("/path/to/myfile.ncc","DocumentName")

import example_post
example_post.export (myObjectName,"/path/to/outputFile.ncc")

def open(filename):
    gfile = __builtins__.open(filename)
    inputstring = gfile.read()
    # the whole gcode program will come in as one string,
    # for example: "G0 X1 Y1\nG1 X2 Y2"
    output = ""
    # we add a comment
    output += "(This is my first parsed output!)\n"
    # we split the input string by lines
    lines = inputstring.split("\n")
    for line in lines:
        output += line
        # we must insert the "end of line" character again
        # because the split removed it
        output += "\n"
    # another comment
    output += "(End of program)"
    import Path
    p = Path.Path(output)
    myPath = FreeCAD.ActiveDocument.addObject("Path::Feature","Import")
    myPath.Path = p
    FreeCAD.ActiveDocument.recompute()

doc = App.ActiveDocument

list_of_all_element_faces = []

for i, face in enumerate(doc.ShapeString.Shape.Faces):
    list_of_all_element_faces.append('Face' + str(i + 1))

doc.Profile_Faces.Base = [(doc.ShapeString, tuple(list_of_all_element_faces))]

doc.recompute()
