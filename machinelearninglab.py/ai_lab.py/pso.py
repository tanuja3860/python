import random
def fitness(x):
    return x ** 2
n = int(input("Enter number of particles: "))
iterations = int(input("Enter number of iterations: "))
w = 0.5
c1 = 1.5
c2 = 1.5
particles = [random.uniform(-10, 10) for _ in range(n)]
velocity = [0] * n
pbest = particles.copy()
gbest = min(particles, key=fitness)
for t in range(iterations):
    for i in range(n):
        r1 = random.random()
        r2 = random.random()
        velocity[i] = (w * velocity[i]
                       + c1 * r1 * (pbest[i] - particles[i])
                       + c2 * r2 * (gbest - particles[i]))
        particles[i] += velocity[i]
        if fitness(particles[i]) < fitness(pbest[i]):
            pbest[i] = particles[i]
        if fitness(pbest[i]) < fitness(gbest):
            gbest = pbest[i]
    print("Iteration:", t + 1,
          "Best solution:", round(gbest, 5),
          "Fitness:", round(fitness(gbest), 5))
print("\nOptimal solution:", round(gbest, 5))
print("Minimum value:", round(fitness(gbest), 5))