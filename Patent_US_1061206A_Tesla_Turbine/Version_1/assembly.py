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
EPS_C = EPS * (-0.5)

# insertion part_tige_filetee_m30_1000l
Mesh.insert(u"part_tige_filetee_m30_1000l.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_tige_filetee_m30_1000l").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_tige_filetee_m30_1000l").ShapeColor = (0.50,0.40,0.30)

# insertion part_ecrou_30m _ 1
Mesh.insert(u"part_ecrou_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_30m").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_30m").ShapeColor = (0.90,0.80,0.70)

# insertion part_ecrou_30m _ 2
Mesh.insert(u"part_ecrou_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_ecrou_30m001").Placement = App.Placement(App.Vector(0, 0, 1000 - 40.2 - 3 - 5 - 7), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_ecrou_30m001").ShapeColor = (0.90,0.80,0.70)

# insertion part_rondelle_30m
Mesh.insert(u"part_rondelle_30m.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_rondelle_30m").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5 + 30), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m").ShapeColor = (0.60,0.50,0.40)

# insertion part_blade
Mesh.insert(u"part_blade.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_blade").Placement = App.Placement(App.Vector(0, 0, 40.2 + 3 + 5 + 30 + 4), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_blade").ShapeColor = (0.30,0.20,0.10)

number_of_steps = 123

# insertion part_rondelle_30m
for i in range(0, number_of_steps):
    location = 40.2 + 3 + 5 + 30 + (i+1)*7
    
    if i < 9:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m00" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
    elif i < 99:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m0" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
    else:
        Mesh.insert(u"part_rondelle_30m.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_rondelle_30m" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_rondelle_30m" + str(i+1)).ShapeColor = (0.60,0.50,0.40)
        
# insertion part_blade
for i in range(0, number_of_steps):
    location = 40.2 + 3 + 5 + 30 + 4 + (i+1)*7
    
    if i < 9:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade00" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade00" + str(i+1)).ShapeColor = (0.30,0.20,0.10)
    elif i < 99:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade0" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade0" + str(i+1)).ShapeColor = (0.30,0.20,0.10)
    else:
        Mesh.insert(u"part_blade.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_blade" + str(i+1)).Placement = App.Placement(App.Vector(0, 0, location), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_blade" + str(i+1)).ShapeColor = (0.30,0.20,0.10)

setview()
            