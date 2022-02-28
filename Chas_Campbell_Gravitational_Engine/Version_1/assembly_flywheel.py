import FreeCAD, Part, Drawing, math, Mesh

DOC = FreeCAD.activeDocument()

DOC_NAME = "assembly_flywheel"


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

# part_tige_filetee_m20_1000l
Mesh.insert(u"part_tige_filetee_m20_1000l.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").ShapeColor = (0.40,0.20,0.10)
FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l").Placement = App.Placement(App.Vector(600,35,-(1000-20)/2),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").ShapeColor = (0.10,0.20,0.40)
FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel").Placement = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
for i in range(1, 7):
    z = 70 * i
    
    Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
    FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).ShapeColor = (0.10,0.20,0.40)    
    FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))

# assembly_slice_flywheel
for i in range(7, 13):
    z = -70 * (i - 6)
    
    if i < 10:
        Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
        FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).ShapeColor = (0.10,0.20,0.40)    
        FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))
    else:
        Mesh.insert(u"assembly_slice_flywheel.stl","assembly_flywheel")
        FreeCADGui.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)).ShapeColor = (0.10,0.20,0.40)    
        FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)).Placement = App.Placement(App.Vector(0,0,z),App.Rotation(App.Vector(0,0,1),0))
        
setview()

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m").Placement = App.Placement(App.Vector(600,35,70*6 + 20),App.Rotation(App.Vector(0,0,1),0))

# part_rondelle_20m
Mesh.insert(u"part_rondelle_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").ShapeColor = (0.90,0.70,0.50)
FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001").Placement = App.Placement(App.Vector(600,35,-70*6 - 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m").Placement = App.Placement(App.Vector(600,35,70*6 + 20 + 3),App.Rotation(App.Vector(0,0,1),0))

# part_ecrou_20m
Mesh.insert(u"part_ecrou_20m.stl","assembly_flywheel")
FreeCADGui.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").ShapeColor = (0.30,0.60,0.90)
FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001").Placement = App.Placement(App.Vector(600,35,-70*6 - 3 - 20),App.Rotation(App.Vector(0,0,1),0))

# Export assembly_flywheel
__objs__=[]
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_tige_filetee_m20_1000l"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel"))

for i in range(1, 10):
    __objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel00" + str(i)))

for i in range(10, 13):
    __objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("assembly_slice_flywheel0" + str(i)))

__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_rondelle_20m001"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m"))
__objs__.append(FreeCAD.getDocument("assembly_flywheel").getObject("part_ecrou_20m001"))

Mesh.export(__objs__,u"assembly_flywheel.stl")

del __objs__
    