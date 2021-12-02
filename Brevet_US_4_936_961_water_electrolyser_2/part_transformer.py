import FreeCAD, Part, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_transformer"

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

# transformer
transformer = Part.makeBox(65.4, 50.8, 87.4776)

# ferroxcube_1
ferroxcube_1 = Part.makeBox(28, 16, 87.4776)
ferroxcube_1_vector = FreeCAD.Vector(18.7, 17.4, 0)
ferroxcube_1.translate(ferroxcube_1_vector)

# cut transformer with ferroxcube_1
transformer = transformer.cut(ferroxcube_1)

# coil
coil = Part.makeBox(65.4, 50.8, 33.3248)

# ferroxcube_2
ferroxcube_2 = Part.makeBox(32, 20, 33.3248)
ferroxcube_2_vector = FreeCAD.Vector(16.7, 15.4, 0)
ferroxcube_2.translate(ferroxcube_2_vector)

# cut coil with ferroxcube_2
coil = coil.cut(ferroxcube_2)

# first cut for transformer with coil
coil_vector = FreeCAD.Vector(0, 0, 2.794)
coil.translate(coil_vector)
transformer = transformer.cut(coil)

# second cut for transformer with coil
coil_vector = FreeCAD.Vector(0, 0, 48.5648)
coil.translate(coil_vector)
transformer = transformer.cut(coil)

# pick_up_coil
pick_up_coil = Part.makeBox(65.4, 50.8, 9.652)

# cut pick_up_coil with ferroxcube_2
pick_up_coil = pick_up_coil.cut(ferroxcube_2)

# cut for transformer with pick_up_coil
pick_up_coil_vector = FreeCAD.Vector(0, 0, 38.9128)
pick_up_coil.translate(pick_up_coil_vector)
transformer = transformer.cut(pick_up_coil)

Part.show(transformer)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_transformer").getObject("Shape"))

stl_file = u"A:/1_Professionnel/1_Holomorphe/2_Archives/2_Outils_Numeriques/Python__Flask__Cristal_Ball/Test/Service/Archives/CAO/1_Holomorphe/Stanley_Meyer/Brevet_US_4_936_961_water_electrolyser_2/part_transformer.stl"

Mesh.export(__objs__, stl_file)

setview()
