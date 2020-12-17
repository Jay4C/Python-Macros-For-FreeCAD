# https://wiki.freecadweb.org/Scripting_examples
# https://wiki.freecadweb.org/Quantity

from FreeCAD import Units

# creating a unit with certain signature
Units.Unit(0,1)      # Mass     (kg)
Units.Unit(1)        # Length   (mm)
Units.Unit(-1,1,-2)  # Pressure (kg/mm*s^2)

# using predefined constants
Units.Unit(Units.Length)
Units.Unit(Units.Mass)
Units.Unit(Units.Pressure)

# parsing unit out of a string
Units.Unit('kg/(m*s^2)')    # Pressure
Units.Unit('Pa')            # the same as combined unit Pascale
Units.Unit('J')             # Joule (work,energy) mm^2*kg/(s^2)

# you can use units from all supported systems of units
Units.Unit('psi')           # imperial pressure
Units.Unit('lb')            # imperial  mass
Units.Unit('ft^2')          # imperial area

# comparing units
Units.Unit(0,1) == Unit(Units.Mass)

# getting type of unit
Units.Unit('kg/(m*s^2)').Type == 'Pressure'

# calculating
Units.Unit('kg') * Units.Unit('m^-1*s^-2') == Units.Unit('kg/(m*s^2)')

from FreeCAD import Units

# to create a quantity you need a value (float) and a unit
Units.Quantity(1.0,Units.Unit(0,1))     # Mass       1.0 kg
Units.Quantity(1.0,Units.Unit(1))       # Length    1.0 mm
Units.Quantity(1.0,Units.Unit(-1,1,-2)) # Pressure  1.0 kg/mm*s^2
Units.Quantity(1.0,Units.Pressure)      # Pressure  1.0 kg/mm*s^2

# you can directly give a signature
Units.Quantity(1.0,0,1)     # Mass       1.0 kg
Units.Quantity(1.0,1)       # Length    1.0 mm
Units.Quantity(1.0,-1,1,-2) # Pressure  1.0 kg/mm*s^2

# parsing quantities out of a string
Units.Quantity('1.0 kg/(m*s^2)') # Pressure
Units.Quantity('1.0 Pa')         # the same as combined Unit Pascale
Units.Quantity('1.0 J')          # Joule (Work,Energy) mm^2*kg/(s^2)

# You can use a point or comma as float delimiter
Units.Quantity('1,0 m')
Units.Quantity('1.0 m')

# you can use units from all supported systems of units
Units.Quantity('1.0 psi')  # imperial pressure
Units.Quantity('1.0 lb')   # imperial mass
Units.Quantity('1.0 ft^2') # imperial area

# the quantity parser can do calculations too
Units.Quantity('360/5 deg')        # splitting circle 
Units.Quantity('1/16 in')          # fractions
Units.Quantity('5.3*6.3 m^2')      # calculating an area
Units.Quantity('1/(log(2.3)/sin(pi)*3.4)+1.8e-3 m')
Units.Quantity('1ft 3in')          # imperial style

# and for sure calculation and comparison
Units.Quantity('1 Pa') * Units.Quantity(2.0) == Units.Quantity('2 Pa')
Units.Quantity('1 m') * Units.Quantity('2 m') == Units.Quantity('2 m^2')
Units.Quantity('1 m') * Units.Quantity('2 ft') + Units.Quantity('2 mm^2')
Units.Quantity('1 m') > Units.Quantity('2 ft')

# accessing the components
Units.Quantity('1 m').Value # get the number (always internal system (mm/kg/s))
Units.Quantity('1 m').Unit  # get the unit
Units.Quantity('1 m') == Units.Quantity( Units.Quantity('1 m').Value , Units.Quantity('1 m').Unit)

# translating the value into other units than the internal system (mm/kg/s)
Units.Quantity('1 km/h').getValueAs('m/s')                  # translate value
Units.Quantity('1 m').getValueAs(2.45,1)                    # translation value and unit signature
Units.Quantity('1 kPa').getValueAs(Units.Pascal)            # predefined standard units 
Units.Quantity('1 MPa').getValueAs(Units.Quantity('N/m^2')) # a quantity

from FreeCAD import Units

# Use the translated string:
Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3

Units.Quantity('22 m').getUserPreferred() # gets a tuple:('22 m', 1000.0, 'm')
Units.Quantity('2  m').getUserPreferred() # Tuple: ('2000 mm', 1.0, 'mm')

import FreeCAD

params = App.ParamGet("User parameter:BaseApp/Preferences/Units")
params.GetInt('Decimals') # returns an int

from FreeCAD import Units

 "nm"  = Units.Quantity(1.0e-6    ,Units.Unit(1));         // nano meter
 "µm"  = Units.Quantity(1.0e-3    ,Units.Unit(1));         // micro meter
 "mm"  = Units.Quantity(1.0       ,Units.Unit(1));         // milli meter
 "cm"  = Units.Quantity(10.0      ,Units.Unit(1));         // centi meter
 "dm"  = Units.Quantity(100.0     ,Units.Unit(1));         // deci meter
 "m"   = Units.Quantity(1.0e3     ,Units.Unit(1));         // meter
 "km"  = Units.Quantity(1.0e6     ,Units.Unit(1));         // kilo meter
 "l"   = Units.Quantity(1000000.0 ,Units.Unit(3));         // liter dm^3
                                                  
 "µg"  = Units.Quantity(1.0e-9    ,Units.Unit(0,1));       // micro gram
 "mg"  = Units.Quantity(1.0e-6    ,Units.Unit(0,1));       // milli gram
 "g"   = Units.Quantity(1.0e-3    ,Units.Unit(0,1));       // gram
 "kg"  = Units.Quantity(1.0       ,Units.Unit(0,1));       // kilo gram
 "t"   = Units.Quantity(1000.0    ,Units.Unit(0,1));       // ton
                                                  
 "s"   = Units.Quantity(1.0       ,Units.Unit(0,0,1));     // second (internal standard time)
 "min" = Units.Quantity(60.0      ,Units.Unit(0,0,1));     // minute
 "h"   = Units.Quantity(3600.0    ,Units.Unit(0,0,1));     // hour  
                                                  
 "A"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,1));   // Ampere (internal standard electric current)
 "mA"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,1));   // milli Ampere         
 "kA"  = Units.Quantity(1000.0    ,Units.Unit(0,0,0,1));   // kilo Ampere         
 "MA"  = Units.Quantity(1.0e6     ,Units.Unit(0,0,0,1));   // Mega Ampere         
                                                  
 "K"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,1)); // Kelvin (internal standard thermodynamic temperature)
 "mK"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,0,1)); // Kelvin         
 "µK"  = Units.Quantity(0.000001  ,Units.Unit(0,0,0,0,1)); // Kelvin         

 "mol" = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,1)); // Mole (internal standard amount of substance)        

 "cd"  = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,0,1)); // Candela (internal standard luminous intensity)        

 "deg" = Units.Quantity(1.0         ,Units.Unit(0,0,0,0,0,0,0,1)); // degree (internal standard angle)
 "rad" = Units.Quantity(180/M_PI    ,Units.Unit(0,0,0,0,0,0,0,1)); // radian         
 "gon" = Units.Quantity(360.0/400.0 ,Units.Unit(0,0,0,0,0,0,0,1)); // gon         

 "in"  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "\""  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "fo"  = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "'"   = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "th"  = Units.Quantity(0.0254      ,Units.Unit(1));       // thou
 "yd"  = Units.Quantity(914.4       ,Units.Unit(1));       // yard



 "lb"  = Units.Quantity(0.45359237   ,Units.Unit(0,1));    // pound
 "oz"  = Units.Quantity(0.0283495231 ,Units.Unit(0,1));    // ounce
 "st"  = Units.Quantity(6.35029318   ,Units.Unit(0,1));    // Stone
 "cwt" = Units.Quantity(50.80234544  ,Units.Unit(0,1));    // hundredweights
