from decimal import Decimal
from math import pi, sqrt

WIEN_CONSTANT: float = 2.8978 * 10**-3
SPEED_OF_LIGHT = 3*10**8
eV = 1.602*10**-19

m_e = 9.11*10**-31
e = 1.6*10**-19

def printNum(num: float, name: str):
    print(name, end=": ")
    print('%.2E' % Decimal(str(num)))

def getTempWithLambdaPeak(lambdaPeak: float) -> float:
    return WIEN_CONSTANT/lambdaPeak


def Q1A():
    lambdaPeakSun = 501*10**-9
    lambdaPeakRed = 810*10**-9
    tempSun = getTempWithLambdaPeak(lambdaPeakSun)
    tempRed = getTempWithLambdaPeak(lambdaPeakRed)
    return (tempSun, tempRed)

def Q1B():
    sigma: float = 5.6704*10**-8
    Psun: float = 3.85*10**26
    Tsun: float = Q1A()[0]
    area: float = Psun/(sigma*Tsun**4)
    printNum(area, "surface area of the sun")
    radius = sqrt(area/(4*pi))
    return radius

def Q1C(magnitude: int):
    sigma: float = 5.6704*10**-8
    Psun: float = 3.85*10**26
    r_sun = Q1B()
    P_r = magnitude*Psun
    T_r = Q1A()[1]
    A_r = P_r/(sigma*T_r**4)
    printNum(A_r, f"surface area of B with mag {magnitude} of sun")
    radius = sqrt(A_r/(4*pi))
    printNum(radius, f"radius of B with mag {magnitude} of sun")
    return radius/r_sun


def Q2B():
    f0 = 2.02/(424*10**-17)
    return SPEED_OF_LIGHT/f0

def Q2C():
    f = 81.5*10**13
    V0 = 424*10**-17 * f - 2.02
    printNum(V0, "stopping potential at f")

    v = sqrt(2*e*V0/m_e)
    return v/SPEED_OF_LIGHT

def Q2D():
    phi = e*2.02
    return phi/eV
    
def Q3A():
    return 0

def main():
    printNum(Q2D(), "result")    

main()