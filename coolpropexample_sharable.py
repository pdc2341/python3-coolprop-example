import CoolProp.CoolProp as CP

#keep the following warning in all copies of software
print("Use at your own risk, this is a preliminary program not error checked or verified at the quality level for production/ corporate/ or commercial use. No warranty is given or implied for this software.")
print("\n\nIt is your responsibility to verify the output from this program is correct")
print("\nThis software is protected by the GNU General Public License V3.0")
print("\nPlease include this warning with all copies of software.")

print("\n\nFunction parameters and output units are available at the bottom of the following web-page: http://www.coolprop.org/coolprop/HighLevelAPI.html#parameter-table")

fluid = b'WATER'
fluid2 = b'AIR'

pressure_at_critical_point = CP.PropsSI(fluid,b'pcrit')
print("\n\nMassic volume [specific volume] (in m^3/kg) is the inverse of density")
# (or volumic mass in kg/m^3).




outp = input("Enter property to output (H for enthalpy, S for entropy, D for density, P for pressure, T for temperature, Q for Quality): ")
param1a = input("Enter property type 1 (H for enthalpy, S for entropy, D for density, P for pressure, T for temperature, Q for Quality): ")
param1b = input("Enter property 1 value: ")
param2a = input("Enter property type 2 (H for enthalpy, S for entropy, D for density, P for pressure, T for temperature, Q for Quality): ")
param2b = input("Enter property 2 value: ")

outp=outp.encode('UTF-8')
param1a=param1a.encode('UTF-8')
param2a=param2a.encode('UTF-8')
param1b=int(param1b)
param2b=int(param2b)

pressure_at_critical_point = CP.PropsSI(fluid,b'pcrit')
print("\n\nMassic volume [specific volume] (in m^3/kg) is the inverse of density")
# (or volumic mass in kg/m^3).

print("Let's compute the specific enthalpy of water at 1 bar (1e5 Pa) of pressure: \n")
#The parameters in the following function are:
#H=Enthalpy
#P=Pressure
#Q=Quality
#fluid=fluid type=water
sEnth = CP.PropsSI(outp,param1a,param1b,param2a,param2b,fluid)
#sEnth = CP.PropsSI(b'H',b'P',1e5,b'Q',0,fluid)
print(sEnth)
print("J/Kg")




print("Let's compute the specific enthalpy of saturated liquid water at 1 bar (1e5 Pa) of pressure: \n")
#The parameters in the following function are:
#H=Enthalpy
#P=Pressure
#Q=Quality
#fluid=fluid type=water
sEnth = CP.PropsSI(b'H',b'P',1e5,b'Q',0,fluid)
print(sEnth)
print("J/Kg")

#print a line break
print("\n")

print("Let's compute the massic volume of saturated liquid water at 1 bar (1e5 Pa) of pressure: \n")
#The parameters in the following function are:
#D=Density
#P=Pressure
#Q=Quality
#fluid=fluid type=water
vL = 1/CP.PropsSI(b'D',b'P',1e5,b'Q',0,fluid)
print(vL)
print("m^3/kg")

#print a line break
print("\n")

print("Same calculation but for a saturated vapor: ")
vG = 1/CP.PropsSI(b'D',b'P',1e5,b'Q',1,fluid)
print(vG)
print("m^3/kg")

print("\n")

print("Let's compute the density of saturated liquid water at 1bar (1e5 Pa) of pressure: ")
#directly below is the standard function used to return property values, The first parameter is the output, the other parameters are the known values/properties
vv=CP.PropsSI(b'D',b'T',293.15,b'Q',0,fluid)
print("Density of water at quality 0, temp 293.15 K\n")
print(vv)
print("kg/m^3")

print("\n")

#viscocity of water at known Temp and Pressure
#The parameters in the following function are:
#V=Viscosity
#T=Temperature
#P=Pressure
#fluid2=fluid type=air
av=CP.PropsSI(b'V', b'T', 293.15, b'P', 101325, fluid2)
#density of water at known Temp and Pressure
#The parameters in the following function are:
#D=Density
ad=CP.PropsSI(b'D', b'T', 293.15, b'P', 101325, fluid2)
print("Viscosity divided by density gives kinematic viscosity")
akv=av/ad
print("Kinematic viscosity of air at 20 C in [(m^2)/s] : \n")
print(akv)


#The parameters in the following function are:
#L=Thermal Conductivity
kth=CP.PropsSI(b'L', b'T', 293.15, b'P', 101325, fluid2)
print("\nThermal conductivity of air at 20 C: \n")
print(kth)
