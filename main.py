from vpython import *

r1, m1, q1, c1 = 0.4, 4, 2, color.red
r2, m2, q2, c2 = 1, 197, 79, color.yellow
v0 = vec(10, 0, 0)
L, k = 40, 1
b = 0.1 * r1
t, dt = 0, 0.001

num = 500

particles = []
for i in range(-num, num):
    sph = sphere(pos=vec(-0.5 * L + r1, i * b, 0), radius=r1, v=v0, color=c1, make_trail=True)
    particles.append(sph)

nucleus = sphere(pos = vec(0, 0, 0), radius = r2, color = c2)

while(True):
    for par in particles:
        F = k * q1 * q2 / par.pos.mag2 * par.pos.norm()
        par.a = F / m1
        par.v += par.a * dt
        par.pos += par.v * dt

    t += dt
    if(t > 50):
        break


