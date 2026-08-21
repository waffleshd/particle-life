import pygame
import particle as p

# Boring stuff here
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

#Init particles array to keep track of all particles
particles = []
particle_mass = 1

while running:
    screen.fill("black")

    #Input handling here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(p.Particle(pygame.mouse.get_pos(),particle_mass))
        if event.type == pygame.K_UP:
            particle_mass +=1
            print(particle_mass)
        if event.type == pygame.K_DOWN:
            particle_mass -= 1
            print(particle_mass)

    for particle in particles:
        particle.tick(particles)
        pygame.draw.circle(screen,"red",particle.get_pos(),particle.get_rad())


    #Boring stuff here
    pygame.display.flip()
    clock.tick(60)

pygame.quit()