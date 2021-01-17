import FreeCAD, Part, Drawing

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_torus"


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

torus = Part.makeTorus(19.05, 3.175)

Part.show(torus)

DOC.recompute()

step_file = "C:\\part_torus.stp"

Part.export([torus], step_file) 

setview()
