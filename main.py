# Author: B12901022/B12901035
from vpython import *
import math

# alpha particle
m1, q1 = 4, 2
# aurum nucleus
q2 = 79

# other related parameters
# let culoumb's constant be 1

v0 = vec(10, 0, 0)
D, k = 20, 1
b = 0.04
t, dt = 0, 0.001
b_range = 20

# number of samples
num = 500


def calc_angle(v):
    t = math.atan2(v.y, v.x)
    return t


particles = []
# y0 = []
for i in range(-num, num):
    sph = sphere(
        pos=vec(-D, i * b_range / num, 0),
        radius=0.4,
        v=v0,
        color=color.red,
        make_trail=True,
    )
    particles.append(sph)
    # y0.append(sph.pos.y)

nucleus = sphere(pos=vec(0, 0, 0), radius=1, color=color.yellow)

while t < 4:
    for par in particles:
        F = k * q1 * q2 / par.pos.mag2 * par.pos.norm()
        par.a = F / m1
        par.v += par.a * dt
        par.pos += par.v * dt

    t += dt


angles = []

for i in range(-num, num):
    par = particles[num + i]
    v = par.v
    # r.y -= i * b_range / num
    angles.append(calc_angle(v))


# print(len(particles))
# print(particles[500].pos.x, particles[500].pos.y)

angles.sort()
# for i in range(0, 4):
#     print(angles[i])
# print(angles[999])

scene = graph()
graph = gcurve(color=color.blue, graph=scene)

p = 0

for ang in angles:
    p += 1 / len(particles)
    graph.plot(pos=(ang, p))
    # if abs(p - 0.5) < 0.01:
    #     print(ang)
