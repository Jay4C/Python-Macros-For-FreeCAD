import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly"


def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# Diametre maximal
diametre_maximal = 250

cylinder_1 = Part.makeCylinder(diametre_maximal/2, 6)

cylinder_2 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2 - 3, 3)

# cylinder_1 cut by cylinder_2
cylinder_2_vector = FreeCAD.Vector(0, 0, 3)
cylinder_2.translate(cylinder_2_vector)
cylinder_1 = cylinder_1.cut(cylinder_2)

cylinder_3 = Part.makeCylinder(diametre_maximal/2, 3)

cylinder_4 = Part.makeCylinder(diametre_maximal/2 - 3 - 5 - 3 - 2, 3)

# cylinder_3 cut by cylinder_4
cylinder_3 = cylinder_3.cut(cylinder_4)

# cylinder_1 cut by cylinder_3
cylinder_3_vector = FreeCAD.Vector(0, 0, 3)
cylinder_3.translate(cylinder_3_vector)
cylinder_1 = cylinder_1.cut(cylinder_3)

# holes for fixing the tank
degre = 10
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 2.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the anodes and the cathodes
degre = 60
for i in range(int(360/degre)):
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

# insertion part_rondelle_m10_17d - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d").ShapeColor = (1.00,1.00,0.00)

# For placing the part_rondelle_m10_17d
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -1)
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i1)).ShapeColor = (1.00,1.00,0.00)
    i1 += 1

# For placing the part_rondelle_m10_17d
for i in range(7, 14):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(7, 13):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 3)
    
    if i < 10:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d00" + str(i)).ShapeColor = (1.00,1.00,0.00)
    else:
        FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_vis_metal_m10_200l - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
Mesh.insert(u"part_vis_metal_m10_200l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l").ShapeColor = (0.00,1.00,1.00)

# For placing the part_vis_metal_m10_200l
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), -3)
    Mesh.insert(u"part_vis_metal_m10_200l.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_vis_metal_m10_200l00" + str(i1)).ShapeColor = (0.00,1.00,1.00)
    i1 += 1
    
# insertion part_ecrou_10m - 0
degre = 60
radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
alpha=(degre*math.pi)/180
vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 4)
Mesh.insert(u"part_ecrou_10m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_10m").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m").ShapeColor = (0.00,0.00,1.00)

# For placing the part_ecrou_10m
i1 = 1
degres = [120, 180, 240, 300, 360]
for degre in degres:
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    alpha=(degre*math.pi)/180
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 4)
    Mesh.insert(u"part_ecrou_10m.stl", "assembly")
    FreeCAD.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_ecrou_10m00" + str(i1)).ShapeColor = (0.00,0.00,1.00)
    i1 += 1

# For placing the part_rondelle_m10_17d
for i in range(15, 21):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(13, 19):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 8)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 0
vector = App.Vector(0, 0, 9)
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate").ShapeColor = (0.00,0.50,0.50)

# For placing the part_rondelle_m10_17d
for i in range(22, 28):
    Mesh.insert(u"part_rondelle_m10_17d.stl", "assembly")

for i in range(19, 25):
    alpha=(i*60*math.pi)/180
    radius = diametre_maximal/2 - 3 - 5 - 3 - 2 - 3 - 2 - 2 - 4 - 5
    vector = App.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 10)
    FreeCAD.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
    FreeCADGui.getDocument("assembly").getObject("part_rondelle_m10_17d0" + str(i)).ShapeColor = (1.00,1.00,0.00)

# insertion part_capacitor_plate - 1
vector = App.Vector(0, 0, 11)
Mesh.insert(u"part_capacitor_plate.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_capacitor_plate001").Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate001").ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(2, 10):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate00" + str(i)).ShapeColor = (0.00,0.50,0.50)

# For placing all the part_capacitor_plate
for i in range(10, 90):
    if i % 2 == 0:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)
    else:
        vector = App.Vector(0, 0, i*2 + 9)
        Mesh.insert(u"part_capacitor_plate.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).Placement = App.Placement(vector, App.Rotation(App.Vector(0,0,1), 60))
        FreeCADGui.getDocument("assembly").getObject("part_capacitor_plate0" + str(i)).ShapeColor = (0.00,0.50,0.50)

setview()
        