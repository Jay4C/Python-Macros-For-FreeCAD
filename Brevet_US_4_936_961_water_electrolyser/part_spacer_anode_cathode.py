import FreeCAD, Part, Drawing

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_spacer_anode_cathode"


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

cylinder_1 = Part.makeCylinder(11, 20)

cylinder_2 = Part.makeCylinder(6.35, 20)

cylinder_3 = cylinder_1.cut(cylinder_2)

cylinder_4 = Part.makeCylinder(11, 18)

cylinder_5 = Part.makeCylinder(6.35 + (8.525 - 6.35), 18)

cylinder_6 = cylinder_4.cut(cylinder_5)

spacer = cylinder_3.cut(cylinder_6)

Part.show(spacer)

DOC.recompute()

step_file = "C:\\part_spacer_anode_cathode.stp"

Part.export([spacer], step_file) 

setview()
