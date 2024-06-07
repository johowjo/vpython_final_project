from vpython import *

r1, m1, q1, c1 = 4, 4, 2, color.red
r2, m2, q2, c2 = 1, 197, 79, color.yellow
v0 = vec(10, 0, 0)
b, L, k = 1, 40, 1
t, dt = 0, 0.001

particles = []
for i in range(-50, 50):
    sph = sphere(pos=vec(-0.5 * L + r1, i * b, 0), radius=r1, m=m1, q=q1, v=v0, color=c1, make_trail=True)
    particles.append(sph)

nucleus = sphere(pos = vec(0, 0, 0), radius = r2, m = m2, q = q2, color = c2)

while(True):
    for par in particles:
        F = k * par.q * nucleus.q / par.pos.mag2 * par.pos.norm()
        par.a = F / par.m
        par.v += par.a * dt
        par.pos += par.v * dt

    t += dt
    if(t > 500):
        break


