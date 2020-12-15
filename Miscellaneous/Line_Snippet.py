import Part, PartGui
doc=App.activeDocument() 
# add a line element to the document and set its points 
l=Part.LineSegment()
l.StartPoint=(0.0,0.0,0.0)
l.EndPoint=(1.0,1.0,1.0)
doc.addObject("Part::Feature","Line").Shape=l.toShape() 
doc.recompute() 