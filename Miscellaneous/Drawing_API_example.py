# https://wiki.freecadweb.org/Drawing_API_example
import FreeCAD, Part, Drawing

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

def simple_example():
    Part.show(Part.makeBox(100,100,100).cut(Part.makeCylinder(80,100)).cut(Part.makeBox(90,40,100)).cut(Part.makeBox(20,85,100)))

    Shape = App.ActiveDocument.Shape.Shape
    [visibleG0, visibleG1, hiddenG0,hiddenG1] = Drawing.project(Shape)
    print("visible edges : ", len(visibleG0.Edges))
    print("hidden edges : ", len(hiddenG0.Edges))

    print("Bnd Box shape: X = ", Shape.BoundBox.XLength, " Y = ", Shape.BoundBox.YLength, " Z = ", Shape.BoundBox.ZLength)
    print("Bnd Box project: X = ", visibleG0.BoundBox.XLength," Y = ", visibleG0.BoundBox.YLength, " Z = ", visibleG0.BoundBox.ZLength)

    [visibleG0, visibleG1, hiddenG0, hiddenG1] = Drawing.project(Shape,App.Vector(1,1,1))

    resultSVG = Drawing.projectToSVG(Shape,App.Vector(1,1,1))
    print(resultSVG)

    DOC.recompute()

simple_example()

setview()

def parametric_example():
    import FreeCAD
    import Part
    import Drawing

    # Create three boxes and a cylinder
    App.ActiveDocument.addObject("Part::Box","Box")
    App.ActiveDocument.Box.Length=100.00
    App.ActiveDocument.Box.Width=100.00
    App.ActiveDocument.Box.Height=100.00

    App.ActiveDocument.addObject("Part::Box","Box1")
    App.ActiveDocument.Box1.Length=90.00
    App.ActiveDocument.Box1.Width=40.00
    App.ActiveDocument.Box1.Height=100.00

    App.ActiveDocument.addObject("Part::Box","Box2")
    App.ActiveDocument.Box2.Length=20.00
    App.ActiveDocument.Box2.Width=85.00
    App.ActiveDocument.Box2.Height=100.00

    App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
    App.ActiveDocument.Cylinder.Radius=80.00
    App.ActiveDocument.Cylinder.Height=100.00
    App.ActiveDocument.Cylinder.Angle=360.00
    # Fuse two boxes and the cylinder
    App.ActiveDocument.addObject("Part::Fuse","Fusion")
    App.ActiveDocument.Fusion.Base = App.ActiveDocument.Cylinder
    App.ActiveDocument.Fusion.Tool = App.ActiveDocument.Box1

    App.ActiveDocument.addObject("Part::Fuse","Fusion1")
    App.ActiveDocument.Fusion1.Base = App.ActiveDocument.Box2
    App.ActiveDocument.Fusion1.Tool = App.ActiveDocument.Fusion
    # Cut the fused shapes from the first box
    App.ActiveDocument.addObject("Part::Cut","Shape")
    App.ActiveDocument.Shape.Base = App.ActiveDocument.Box 
    App.ActiveDocument.Shape.Tool = App.ActiveDocument.Fusion1
    # Hide all the intermediate shapes 
    Gui.ActiveDocument.Box.Visibility=False
    Gui.ActiveDocument.Box1.Visibility=False
    Gui.ActiveDocument.Box2.Visibility=False
    Gui.ActiveDocument.Cylinder.Visibility=False
    Gui.ActiveDocument.Fusion.Visibility=False
    Gui.ActiveDocument.Fusion1.Visibility=False
    App.ActiveDocument.addObject('Drawing::FeaturePage','Page')
    App.ActiveDocument.Page.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'
    App.ActiveDocument.addObject('Drawing::FeatureViewPart','View')
    App.ActiveDocument.View.Source = App.ActiveDocument.Shape
    App.ActiveDocument.View.Direction = (0.0,0.0,1.0)
    App.ActiveDocument.View.X = 10.0
    App.ActiveDocument.View.Y = 10.0
    App.ActiveDocument.Page.addObject(App.ActiveDocument.View)
    App.ActiveDocument.addObject('Drawing::FeatureViewPart','ViewRot')
    App.ActiveDocument.ViewRot.Source = App.ActiveDocument.Shape
    App.ActiveDocument.ViewRot.Direction = (0.0,0.0,1.0)
    App.ActiveDocument.ViewRot.X = 290.0
    App.ActiveDocument.ViewRot.Y = 30.0
    App.ActiveDocument.ViewRot.Scale = 1.0
    App.ActiveDocument.ViewRot.Rotation = 90.0
    App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewRot)
    App.ActiveDocument.addObject('Drawing::FeatureViewPart','ViewIso')
    App.ActiveDocument.ViewIso.Source = App.ActiveDocument.Shape
    App.ActiveDocument.ViewIso.Direction = (1.0,1.0,1.0)
    App.ActiveDocument.ViewIso.X = 335.0
    App.ActiveDocument.ViewIso.Y = 140.0
    App.ActiveDocument.ViewIso.ShowHiddenLines = True
    App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewIso)
    App.ActiveDocument.View.X = 30.0
    App.ActiveDocument.View.Y = 30.0
    App.ActiveDocument.View.Scale = 1.5
    App.ActiveDocument.recompute()

parametric_example()

setview()

def accessing_the_bits_and_pieces():
    ViewSVG = App.ActiveDocument.View.ViewResult
    print(ViewSVG)

    print("Resulting SVG document: ",App.ActiveDocument.Page.PageResult)

    file = open(App.ActiveDocument.Page.PageResult,"r")
    print("Result page is ",len(file.readlines())," lines long")
    
    del file
    App.ActiveDocument.addObject('Drawing::FeatureView','ViewSelf')
    App.ActiveDocument.ViewSelf.ViewResult = """<g id="ViewSelf"
    stroke="rgb(0, 0, 0)"
    stroke-width="0.35"
    stroke-linecap="butt"
    stroke-linejoin="miter"
    transform="translate(30,30)"
    fill="#00cc00"
    >

    <ellipse cx="40" cy="40" rx="30" ry="15"/>
    </g>"""

    App.ActiveDocument.Page.addObject(App.ActiveDocument.ViewSelf)
    App.ActiveDocument.recompute()

    del ViewSVG

accessing_the_bits_and_pieces()

setview()

def general_dimensioning_and_tolerancing():
    import gdtsvg as g # Import the module, I like to give it an easy handle
    ourFrame = g.ControlFrame("0",
        "0", 
        g.Perpendicularity(), 
        ".5", 
        g.Diameter(), 
        g.ModifyingSymbols("M"), 
        "A", 
        g.ModifyingSymbols("F"), 
        "B", 
        g.ModifyingSymbols("L"), 
        "C", 
        g.ModifyingSymbols("I"))

    ourDimension = linearDimension(point1, point2, textpoint, 
        dimensiontext, 
        linestyle=getStyle("visible"), 
        arrowstyle=getStyle("filled"), 
        textstyle=getStyle("text")

general_dimensioning_and_tolerancing()

setview()
