import matplotlib.pyplot as plt

import numpy as np

import scipy as sp

import pandas as pd

plt.close('all')

df = pd.read_csv('IdvsVgForNominalmodel.txt', sep = '\t')

plt.figure()
plt.plot(df['vg'], df['Id(M1)'])
plt.xlabel('Vg')
plt.ylabel('Id(M1)')
plt.title('Id(Vgs) for L = 45nm')
plt.grid()
plt.show()

df130 = pd.read_csv('IdvsVgForNominalmodel130nm.txt', sep = '\t')

plt.figure()
plt.plot(df130['vg'], df130['Id(M1)'])
plt.xlabel('Vg')
plt.ylabel('Id(M1)')
plt.title('Id(Vgs) for L = 130nm')
plt.grid()
plt.show()

vg = np.array(df['vg'])
Id = np.array(df['Id(M1)'])

vg130 = np.array(df130['vg'])
Id130 = np.array(df130['Id(M1)'])

def getlin(vgs, K, Vt):
    return 0.5*K*((vgs-Vt)**2)

def condModel(vgs, K, Vt):
    v1 = vgs-Vt
    Id = np.piecewise(v1, [v1 <= 0, v1 > 0], [0, lambda v1: 0.5*K*(v1**2)])
    return Id

plt.figure()
params, cov = sp.optimize.curve_fit(getlin, vg, Id)
K_1 = params[0]
print(K_1)
Vt_1 = params[1]
print(Vt_1)
# K, Vt = params
plt.plot(vg, Id, '+', vg, getlin(vg, K_1, Vt_1))
plt.xlabel('Vg')
plt.ylabel('Simulated Id(M1) and Model Id(M1)')
plt.title('Id(Vgs) for L = 45nm')
plt.grid()

lowBound = [0.0,0.0]
highBound = [0.001,1.0]

plt.figure()
params, cov = sp.optimize.curve_fit(condModel, vg, Id, bounds = (lowBound, highBound))
K = params[0]
print(K)
Vt = params[1]
print(Vt)
IdModel = condModel(vg, K, Vt)
# K, Vt = params
plt.plot(vg, Id, '+', vg, IdModel) 
plt.xlabel('Vg')
plt.ylabel('Simulated Id(M1) and Model Id(M1)')
plt.title('Id(Vgs) for L = 45nm')
plt.grid()

erro45_1 = abs((getlin(vg, K_1, Vt_1) - Id)/Id) * 100;

plt.figure()
plt.plot(vg, erro45_1)
plt.grid()
plt.xlabel('Vg')
plt.ylabel('Relative error: Model_1 + Simulation Id(M1)')
plt.title('Relative error 45nm')

erro45 = abs((IdModel - Id)/Id) * 100;

plt.figure()
plt.plot(vg, erro45)
plt.grid()
plt.xlabel('Vg')
plt.ylabel('Relative error: Model + Simulation Id(M1)')
plt.title('Relative error 45nm')

plt.figure()
params, cov = sp.optimize.curve_fit(getlin, vg130, Id130)
K130_1 = params[0]
print(K130_1)
Vt130_1 = params[1]
print(Vt130_1)
# K, Vt = params
plt.plot(vg130, Id130, '+', vg130, getlin(vg130, K130_1, Vt130_1))
plt.xlabel('Vg')
plt.ylabel('Simulated Id(M1) and Model Id(M1)')
plt.title('Id(Vgs) for L = 130nm')
plt.grid()

lowBound130 = [0.0,0.0]
highBound130 = [0.001,1.3]

plt.figure()
params, cov = sp.optimize.curve_fit(condModel, vg130, Id130, bounds = (lowBound130, highBound130))
K130 = params[0]
print(K)
Vt130 = params[1]
print(Vt)
IdModel130 = condModel(vg130, K130, Vt130)
# K, Vt = params
plt.plot(vg130, Id130, '+', vg130, IdModel130) 
plt.xlabel('Vg')
plt.ylabel('Simulated Id(M1) and Model Id(M1)')
plt.title('Id(Vgs) for L = 130nm')
plt.grid()

erro130_1 = abs((getlin(vg130, K130_1, Vt130_1) - Id130)/Id130) * 100;

plt.figure()
plt.plot(vg130, erro130_1)
plt.grid()
plt.xlabel('Vg')
plt.ylabel('Relative error: Model + Simulation Id(M1)')
plt.title('Relative error 130nm')

erro130 = abs((IdModel130 - Id130)/Id130) * 100;

plt.figure()
plt.plot(vg130, erro130)
plt.grid()
plt.xlabel('Vg')
plt.ylabel('Relative error: Model + Simulation Id(M1)')
plt.title('Relative error 130nm')