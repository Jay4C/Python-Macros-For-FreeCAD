import Part,PartGui 
doc=App.activeDocument()
n=list() 
# create a 3D vector, set its coordinates and add it to the list 
v=App.Vector(0,0,10) 
n.append(v) 
v=App.Vector(0,10,0) 
n.append(v) 
v=App.Vector(0,0,10) 
n.append(v)
v=App.Vector(0,10,10) 
n.append(v)
#... repeat for all nodes 
# Create a polygon object and set its nodes 
p=doc.addObject("Part::Polygon","Polygon") 
p.Nodes=n 
doc.recompute()