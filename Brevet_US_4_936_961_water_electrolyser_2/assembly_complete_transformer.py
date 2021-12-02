import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_complete_transformer"

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

# EPS = tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# part_core_ferrite
part_core_ferrite = Part.makeBox(93, 76, 16)

# box_1
box_1 = Part.makeBox(37, 48, 16)
box_1_vector = FreeCAD.Vector(28, 0, 0)
box_1.translate(box_1_vector)

# part_core_ferrite cut by box_1
part_core_ferrite = part_core_ferrite.cut(box_1)

Part.show(part_core_ferrite)

DOC.recompute()

# insert transformer
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_transformer.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_transformer").Placement = App.Placement(App.Vector(-18.7, 48, -17.4), App.Rotation(App.Vector(1,0,0), 90))

# insert transformer
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_transformer.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_transformer001").Placement = App.Placement(App.Vector(18.7 + 28, 48, -17.4), App.Rotation(App.Vector(1,0,0), 90))

# insert part_core_ferrite
Mesh.insert(u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_core_ferrite.stl", "assembly_complete_transformer")

FreeCAD.getDocument("assembly_complete_transformer").getObject("part_core_ferrite").Placement = App.Placement(App.Vector(0, 0, 17.3), App.Rotation(App.Vector(1,0,0), 180))

setview()
        