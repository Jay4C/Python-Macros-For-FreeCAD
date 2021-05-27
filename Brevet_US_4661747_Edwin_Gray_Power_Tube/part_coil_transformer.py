import FreeCAD, Part, Drawing, math, ImportGui

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_coil_transformer"


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

# part_coil_transformer
part_coil_transformer = Part.makeCylinder(12, 50)

# cylinder_core_ferrite
cylinder_core_ferrite = Part.makeCylinder(5, 50)

# part_coil_transformer cut by cylinder_core_ferrite
part_coil_transformer = part_coil_transformer.cut(cylinder_core_ferrite)

# cylinder_1
cylinder_1 = Part.makeCylinder(12, 46)

# cylinder_2
cylinder_2 = Part.makeCylinder(7, 46)

# cylinder_1 cut by cylinder_2
cylinder_1 = cylinder_1.cut(cylinder_2)

# part_coil_transformer cut by cylinder_1
cylinder_1_vector = FreeCAD.Vector(0, 0, 2)
cylinder_1.translate(cylinder_1_vector)
part_coil_transformer = part_coil_transformer.cut(cylinder_1)

Part.show(part_coil_transformer)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_coil_transformer").getObject("Shape"))

step_file = u"path/to/part_coil_transformer.step"

ImportGui.export(__objs__, step_file)

setview()