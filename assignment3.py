from decimal import Decimal
from math import pi, sqrt, cos, acos, sin, asin 

WIEN_CONSTANT: float = 2.8978 * 10**-3
SPEED_OF_LIGHT = 3*10**8
eV = 1.602*10**-19

m_e = 9.11*10**-31
e = 1.6*10**-19
h = 6.63*10**-34

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


Angs = 1*10**-10
    
def Q3A():
    lambdaInit: float = 0.539 * Angs
    lambdaFinal: float = 0.557 * Angs
    deltaLambda: float = lambdaFinal - lambdaInit
    lambdaC: float = 2.42*10**-12
    temp: float = 1-(deltaLambda/lambdaC)
    result = acos(temp)
    
    return result

def Q3B():
    lambdaInit: float = 0.539 * Angs
    lambdaFinal: float = 0.557 * Angs
    GammaU = h*(1/lambdaInit - 1/lambdaFinal)/(m_e*SPEED_OF_LIGHT)+1
    u = sqrt(1-1/(GammaU**2))*SPEED_OF_LIGHT
    temp = h/lambdaFinal*sin(Q3A())/(GammaU*m_e*u)
    result = asin(temp)
    return result * 180/pi

m_p = 1.67*10**-27


def Q4A():
    return h/(2*m_p*SPEED_OF_LIGHT)

def Q4B():
    u = 0.8*SPEED_OF_LIGHT
    GammaU = 1/(sqrt(1-0.8**2))
    printNum(GammaU, "gammaU")
    return h/(2*GammaU*m_p*SPEED_OF_LIGHT)

m_Pb = 207.2 * 1.66*10**-27
def Q4C1():
    lambdaA = Q4A()
    u_Pb = h/(lambdaA*m_Pb)
    K_Pb = 0.5 * m_Pb * (u_Pb**2)
    E_photon = h*SPEED_OF_LIGHT/lambdaA
    return K_Pb/E_photon

def Q4C2():
    lambdaB = Q4B()
    u_Pb = h/(lambdaB*m_Pb)
    printNum(u_Pb, "u of lead")
    K_Pb = 0.5 * m_Pb * (u_Pb**2)
    printNum(K_Pb, "K of lead")
    E_photon = h*SPEED_OF_LIGHT/lambdaB
    printNum(E_photon, "engergy of gamma")
    return K_Pb/E_photon

micro = 10**-6
nano = 10**-9

SLIT_WIDTH = 2.5 * micro
def Q5AB(wavelengthNM):
    lambdaVal = wavelengthNM * nano
    angle = asin(lambdaVal/SLIT_WIDTH)
    result = 2*angle*180/pi
    return result

def Q5C():
    E_per_area = 8.33*10**-15
    return (SLIT_WIDTH/SPEED_OF_LIGHT, E_per_area) 

E_per_area = Q5C()[1]
def Q5D12(wavelengthNM):
    lambdaVal = wavelengthNM * nano
    E_photon = h*SPEED_OF_LIGHT/lambdaVal
    printNum(E_photon, "energy of single photon")
    numPhoton = E_per_area/E_photon
    return numPhoton



def main():
    printNum(Q5D12(0.15), "number of photons")

main()