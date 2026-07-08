from aeropy.xfoil_module import find_coefficients
from numpy import linspace
import matplotlib.pyplot as plt

def getNACA():
    AIRFOILS = []
    print("Type '/' when finished")
    while True:
        airfoil = input("Enter naca airfoil number: ")
        if airfoil == '/':
            break
        else:
            AIRFOILS.append(airfoil)
    return AIRFOILS

def getAlpha():
    a_min = float(input("Enter the minimum alpha value: "))
    a_max = float(input("Enter the maximum alpha value: "))
    return [a_min,a_max]

def getCL(airfoils,a):
    Re = float(input("Enter Reynolds number in digits: "))
    x = linspace(a[0],a[-1],100)
    CL=[]
    cL=[]
    AlphA = []
    ALPHA=[]
    print("Calculating...")
    for af in airfoils:
        for k in x:
            result = find_coefficients(alpha=k,airfoil=f"naca{af}", NACA=True,Reynolds=Re,iteration=100,GDES='NAAR\n\n',PANE=True,dir="Analysis/temp/",delete=True)            
            if isinstance(result['CL'], float):
                cL.append(result['CL'])
                AlphA.append(k)
        CL.append(cL.copy())
        cL.clear()
        ALPHA.append(AlphA.copy())
        AlphA.clear()
    
    return CL,ALPHA

airfoils = getNACA()
angle = getAlpha()
Cls,alpha = getCL(airfoils,angle)
print("Done.")


fig, axes = plt.subplots()
for cl,Alpha,arf in zip(Cls,alpha,airfoils):
   axes.plot(Alpha,cl,label=f"NACA {arf}")

axes.legend()   
axes.set_xlabel("Alpha")
axes.set_ylabel("Lift Coefficient")
plt.grid(True)
plt.show()
