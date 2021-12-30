import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_plant"


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

maximal_diameter = 100
ecart = 8

# insertion assembly
for i in range(0, 20):
    if i < 1:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly").Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly").ShapeColor = (0.10,0.10,0.10)
    elif i >= 1 and i < 10:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly00" + str(i)).Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly00" + str(i)).ShapeColor = (0.10,0.10,0.10)
    else:
        Mesh.insert(u"assembly.stl", "assembly_plant")
        FreeCAD.getDocument("assembly_plant").getObject("assembly0" + str(i)).Placement = App.Placement(App.Vector((i+1)*(maximal_diameter + ecart), 0, 0), App.Rotation(App.Vector(0,0,1), 0))
        FreeCADGui.getDocument("assembly_plant").getObject("assembly0" + str(i)).ShapeColor = (0.10,0.10,0.10)

setview()

__objs__ = []

for i in range(0, 20):
    if i < 1:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly"))
    elif i >= 1 and i < 10:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly00" + str(i)))
    else:
        __objs__.append(FreeCAD.getDocument("assembly_plant").getObject("assembly0" + str(i)))

stl_file = u"assembly_plant.stl"

Mesh.export(__objs__, stl_file)

del __objs__
        