import pygame
import math

class Particle:
    def __init__(self,pos,mass = 1):
        self.pos = pygame.Vector2(pos[0],pos[1])
        self.mass = mass
        self.velocity = pygame.Vector2(0,0) # x and y speeds
        self.rad = self.mass + 5
        self.drag = 1

    def get_pos(self):
        return self.pos

    def get_rad(self):
        return self.rad

    def get_vel(self):
        return self.velocity

    def get_dist(self,target_pos):
        return math.dist([self.pos.x,self.pos.y],[target_pos.x,target_pos.y])

    def get_dir(self,target_pos):
        return math.atan2(self.pos.y - target_pos.y, self.pos.x - target_pos.x)

    def gravity(self,particle):
        dist = self.get_dist(particle.get_pos())
        direction = self.get_dir(particle.get_pos())
        if dist < 1:
            dist = 1
        force = self.mass * particle.mass / dist**2
        x_force = force * math.cos(direction)
        y_force = force * math.sin(direction)
        if dist > self.rad + particle.get_rad():
            self.velocity += pygame.Vector2(x_force,y_force)
        else:
            rel_x_vel = self.velocity.x - particle.get_vel().x
            rel_y_vel = self.velocity.y - particle.get_vel().y
            rel_vel = math.hypot(rel_x_vel,rel_y_vel)
            self.drag += (rel_vel + (2**(1/(2*dist)))) * 2
            self.velocity -= pygame.Vector2(x_force / self.drag,y_force / self.drag)

    def tick(self,particles):
        for particle in particles:
            if particle != None and particle != self:
                self.gravity(particle)

        self.pos -= self.velocity

"""

AI GENERATED CODE HERE
Will not be using this until i know how it works. Also doesn't really work as well as i would like it to so..

import pygame
import math

class Particle:
    def __init__(self, pos, mass=1, rad=10):
        self.pos = pygame.Vector2(pos[0], pos[1])
        self.mass = mass
        self.velocity = pygame.Vector2(0, 0)
        self.rad = rad
        self.base_drag = 0.98  # Applied every tick globally

    def get_pos(self):
        return self.pos

    def get_rad(self):
        return self.rad

    def get_vel(self):
        return self.velocity

    def get_dist(self, target_pos):
        return math.dist([self.pos.x, self.pos.y], [target_pos.x, target_pos.y])

    def get_dir(self, target_pos):
        return math.atan2(self.pos.y - target_pos.y, self.pos.x - target_pos.x)

    def gravity(self, particle):
        dist = self.get_dist(particle.get_pos())
        
        if dist < 1:
            return
        
        direction = self.get_dir(particle.get_pos())
        touch_dist = self.rad + particle.rad
        
        if dist > touch_dist:
            # Normal gravity (attraction)
            force = self.mass * particle.mass / (dist ** 2)
            x_force = force * math.cos(direction)
            y_force = force * math.sin(direction)
            self.velocity += pygame.Vector2(x_force, y_force)
        else:
            # Touching: couple velocities + add outward pressure
            rel_vel = self.velocity - particle.get_vel()
            rel_vel_mag = rel_vel.length() if rel_vel.length() > 0 else 0.001
            
            coupling_strength = (1 - (dist / touch_dist)) * 0.1
            self.velocity += (particle.get_vel() - self.velocity) * coupling_strength
            
            separation_drag = rel_vel_mag * 0.05
            self.velocity *= (1 - separation_drag)
            
            # NEW: Outward pressure to prevent collapse
            pressure_force = (1 - (dist / touch_dist)) * 0.5  # Stronger when very close
            outward_dir = pygame.Vector2(math.cos(direction), math.sin(direction))
            self.velocity += outward_dir * pressure_force

    def tick(self, particles):
        for particle in particles:
            if particle is not None and particle != self:
                self.gravity(particle)
        
        # Apply global drag each frame
        self.velocity *= self.base_drag
        self.pos -= self.velocity

"""
