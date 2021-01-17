import FreeCAD, Part, Drawing

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_cylinder_first_inductor"


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

cylinder_1 = Part.makeCylinder(12.7, 60)

cylinder_2 = Part.makeCylinder(3.5, 60)

# Cut
cut = cylinder_1.cut(cylinder_2)

Part.show(cut)

DOC.recompute()

step_file = "C:\\part_cylinder_first_inductor.stp"

Part.export([cut], step_file) 

setview()
