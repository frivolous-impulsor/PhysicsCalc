import time
from math import e, floor, ceil

a = 1095369562025702556403033673059514719985657846060999038001272754193712036128714475110343472959833158083894277499580078770116751707887313066350958894258
m = 1486849462548131038391075744532018339748969593030811665429204557155898771386352512821463245755183336883785007564272951579651325540287779851348210497897
#assuming m is a prime
def eulerInverse(a: int, m: int):
    return pow(a, m-2, m)

def eucliInverse(a: int, m: int):
    r = m
    newR = a
    s = 0
    newS = 1

    while(newR != 0):
        q = r//newR

        temp = newR
        newR = r - q*newR
        r = temp
        
        temp = newS
        newS = s - q*newS
        s = temp

    if(s > 1):
        Exception("a not invertible")
    if(s < 0):
        s += m
    return s


def a1():
    micro = 10**-3
    initTeuler = time.time()/micro
    eulerResult = eulerInverse(a, m)
    finalTeuler = time.time()/micro
    timeEuler = finalTeuler - initTeuler
    print(f"time euler: {timeEuler}")

    initTeucli = time.time()/micro
    eucliResult = eucliInverse(a, m)
    finalTeucli = time.time()/micro
    timeEucli = finalTeucli - initTeucli
    print(f"time eucli: {timeEucli}")

    diffEuler_Eucli = timeEuler - timeEucli
    print(f"euler - eucli: {diffEuler_Eucli}")


exp = 7
x = 38745745356349
n = 508281196310201376192554864656699346831575429768465482788715190735760361687281737746563113895010157
y = pow(x, exp, n)

y_b = 4066488477440339689911514138508998613662966982287543919056006242924596335364286584668317646217011

def q2(z, cipher):
    x = pow((z*n + cipher), 1/exp)
    return x

def verify(guess, cipher):
    guessFloor = floor(guess)
    guessCeil = ceil(guess)
    encryptionFloor = guessFloor**exp
    encryptionCeil = guessCeil**exp
    return encryptionCeil == cipher or encryptionFloor == cipher

guess = q2(0, y_b)
print(guess)
print(verify(guess, y_b))
