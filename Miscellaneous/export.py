import Part

doc = FreeCAD.newDocument("Box_5")

box = doc.addObject("Part::Box", "myBox")
box.Height = 5
box.Length = 5
box.Width = 5

doc.recompute()

Part.export([box], "box.stp")

Gui.activeDocument().activeView().viewIsometric()
Gui.SendMsgToActiveView("ViewFit")

