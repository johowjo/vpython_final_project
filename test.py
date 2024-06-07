from vpython import sphere, vector, rate, color, canvas, arrow, mag, norm

# Constants
k = 8.99e9  # Coulomb's constant, N m²/C²
q_alpha = 2 * 1.6e-19  # Charge of alpha particle, C
q_nucleus = 79 * 1.6e-19  # Charge of gold nucleus (assuming gold), C
m_alpha = 6.64e-27  # Mass of alpha particle, kg

# Create a scene
scene = canvas(title='Rutherford Scattering Simulation',
               width=800, height=600, center=vector(0, 0, 0), background=color.black)

# Create the nucleus
nucleus = sphere(pos=vector(0, 0, 0), radius=1e-14, color=color.yellow, mass=197*1.66e-27)

# Create the alpha particle
alpha = sphere(pos=vector(-5e-14, 1e-14, 0), radius=5e-15, color=color.red, make_trail=True)
alpha.mass = m_alpha
alpha.charge = q_alpha
alpha.velocity = vector(2e7, 0, 0)  # Initial velocity of the alpha particle

# Time step
dt = 1e-22

while True:
    rate(1000)

    # Calculate the vector from alpha particle to nucleus
    r = alpha.pos - nucleus.pos
    r_mag = mag(r)
    r_hat = norm(r)

    # Coulomb force
    force = (k * q_alpha * q_nucleus / r_mag**2) * r_hat

    # Update momentum
    alpha.velocity += (force / alpha.mass) * dt

    # Update position
    alpha.pos += alpha.velocity * dt

    # Update trail (optional, for visualization)
    alpha.trail.append(pos=alpha.pos)

