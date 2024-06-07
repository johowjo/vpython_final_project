from vpython import *

r1, m1, q1, c1 = 4, 4, 2, color.red
v0 = vec(10, 0, 0)
b, L, k = 1, 40, 1
alpha = sphere(pos=vec(-0.5*L + r1, b, 0), radius=r1, m=m1, q=q1, v=v0, color=c1, make_trail=True)
particles = []
for i in range(-5, 5):
    sph = sphere(pos=vec(-0.5*L*i + r1, b, 0), radius=r1, m=m1, q=q1, v=v0, color=c1, make_trail=True)
    particles.append(sph)

particles[2].pos.y += 12


# particles.append(sphere(pos=vec(-0.5*L + r1, b, 0), radius=r1, m=m1, q=q1, v=v0, color=c1, make_trail=True))

print(len(particles))


