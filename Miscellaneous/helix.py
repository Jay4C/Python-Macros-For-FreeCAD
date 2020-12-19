import FreeCAD, Part

DOC = FreeCAD.activeDocument()

DOC_NAME = "helix"


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

pitch_M3 = 0.5
height_M3 = 10
radius_M3 = 2.459

helix = Part.makeHelix(pitch_M3, height_M3, radius_M3)

Part.show(helix)

DOC.recompute()

setview()
