import random
import math

def function(x1,x2):
  root = math.sqrt((x1**2)+(x2**2))
  f = -1 * (abs(math.sin(x1)*math.cos(x2) * math.exp(abs(1-(root/math.pi)))))
  return f


if __name__ == "__main__":
    x1 = float(random.uniform(-10, 10))
    x2 = float(random.uniform(-10, 10))

    t = 100
    t_final = 0.001
    deltaT = 0.009

    currentState = function(x1, x2)
    best = currentState

    while t > t_final:
        x1 = float(random.uniform(-10, 10))
        x2 = float(random.uniform(-10, 10))
        newState = function(x1, x2)
        deltaE = newState - currentState

        if deltaE < 0:
            currentState = newState
            best = newState
            t = t - deltaT

        elif deltaE >= 0:
            p = math.exp(-1 * (deltaE) / t)
            r = float(random.uniform(0, 1))
            if (r <= p):
                currentState = newState
                t = t - deltaT

    print("x1 = ", x1)
    print("x2 = ", x2)
    print("delta E = ", deltaE)
    print("best = ", best)
