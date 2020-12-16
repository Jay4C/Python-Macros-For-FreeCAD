# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Mesh_to_Part
import FreeCAD, Part, Drawing, time
import Mesh

DOC = FreeCAD.activeDocument()
DOC_NAME = "Pippo"

def clear_doc():
    """
    Clear the active document deleting all the objects
    """
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)

def setview():
    """Rearrange View"""
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

def convert_part_objects_to_meshes():
    import Part
    doc = FreeCAD.newDocument("Box_5")
    box = doc.addObject("Part::Box", "myBox")
    box.Height = 5
    box.Length = 5
    box.Width = 5
    doc.recompute()

    import Mesh

    obj = box # a Part object must be preselected
    shp = obj.Shape
    faces = []

    triangles = shp.tessellate(1) # the number represents the precision of the tessellation
    for tri in triangles[1]:
        face = []
        for i in tri:
            face.append(triangles[0][i])
        faces.append(face)

    m = Mesh.Mesh(faces)
    Mesh.show(m)

    time.sleep(5)

    import MeshPart

    obj = box # a Part object must be preselected
    shp = obj.Shape

    mesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
    mesh.Mesh = MeshPart.meshFromShape(
            Shape=shp,
            LinearDeflection=0.01,
            AngularDeflection=0.025,
            Relative=False)

    setview()

# convert_part_objects_to_meshes()

def convert_meshes_to_part_objects_1():
    import Part
    doc = FreeCAD.newDocument("Box_5")
    box = doc.addObject("Part::Box", "myBox")
    box.Height = 5
    box.Length = 5
    box.Width = 5
    doc.recompute()

    import Mesh
    import Part

    mesh = Mesh.createTorus()
    shape = Part.Shape()
    shape.makeShapeFromMesh(mesh.Topology, 0.05) # the second arg is the tolerance for sewing
    solid = Part.makeSolid(shape)
    Part.show(solid)

    setview()

# convert_meshes_to_part_objects_1()

def convert_meshes_to_part_objects_2():
    import Part
    doc = FreeCAD.newDocument("Box_5")
    box = doc.addObject("Part::Box", "myBox")
    box.Height = 5
    box.Length = 5
    box.Width = 5
    doc.recompute()

    import Mesh
    import Part
    import MeshPart

    obj = box # a Mesh object must be preselected
    mesh = obj.Mesh
    segments = mesh.getPlanarSegments(0.00001) # use rather strict tolerance here
    faces = []

    for i in segments:
        if len(i) > 0:
            # a segment can have inner holes
            wires = MeshPart.wireFromSegment(mesh, i)
            # we assume that the exterior boundary is that one with the biggest bounding box
            if len(wires) > 0:
                ext = None
                max_length=0
                for i in wires:
                    if i.BoundBox.DiagonalLength > max_length:
                        max_length = i.BoundBox.DiagonalLength
                        ext = i

                wires.remove(ext)
                # all interior wires mark a hole and must reverse their orientation, otherwise Part.Face fails
                for i in wires:
                    i.reverse()

                # make sure that the exterior wires comes as first in the list
                wires.insert(0, ext)
                faces.append(Part.Face(wires))

    solid = Part.Solid(Part.Shell(faces))
    Part.show(solid)

    setview()

convert_meshes_to_part_objects_2()
