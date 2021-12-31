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

number_of_steps = 20

# insertion part_electrode_laser_cutting
Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting").Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(App.Vector(0,0,1), 0))
FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting").ShapeColor = (0.10,0.20,0.30)

# insertion part_electrode_laser_cutting
for i in range(1, number_of_steps):
    if i < 10:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)).ShapeColor = (0.50,0.40,0.30)
    elif i >= 10 and i < 100:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)).ShapeColor = (0.50,0.40,0.30)
    else:
        Mesh.insert(u"part_electrode_laser_cutting.stl", "assembly")
        FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)).Placement = App.Placement(App.Vector(0, 0, i*3), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)).ShapeColor = (0.50,0.40,0.30)
    
setview()

__objs__ = []

__objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting"))

# append part_electrode_laser_cutting
for i in range(1, number_of_steps):
    if i < 10:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting00" + str(i)))
    elif i >= 10 and i < 100:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting0" + str(i)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly").getObject("part_electrode_laser_cutting" + str(i)))

stl_file = u"assembly.stl"

Mesh.export(__objs__, stl_file)

del __objs__
            