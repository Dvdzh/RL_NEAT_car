import pygame
import math

# constante
white = (255, 255, 255)
black = (0, 0, 0)
car_size = 60

# initialisation fenetre
pygame.init()
display = pygame.display.set_mode((1200, 600))


# rajoute background
background_image = pygame.image.load(
    "/Users/davidzhu/Desktop/Projet_info/NEAT_autonomous_vehicule/map2.png")
background_image = pygame.transform.scale(background_image, (1200, 600))
display.blit(background_image, (0, 0))


# car
car = pygame.image.load(
    "/Users/davidzhu/Desktop/Projet_info/NEAT_autonomous_vehicule/car.png")
car = pygame.transform.scale(car, (60, 60))
display.blit(car, (522-car_size/2, 522-car_size/2))
pygame.display.update()


# LIDAR entree
lidar = [0, 0, 0, 0, 0]
nb_input = [0, 45, 90, 135, 180]

# positions initial
pos = {"x": 522, "y": 522}
angle = 0
delta_angle = 0
delta_avance = 0  # dans le référentiel de la voiture


# écriture
font = pygame.font.Font(None, 20)
text_surface = font.render("{} {} {} {}".format(
    pos, angle, delta_angle, delta_avance), True, black)


avance = 0
d_angle = 0
angle = 0
x = 522-car_size/2
y = 522-car_size/2
running = True
while running:
    display.blit(background_image, (0, 0))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                running = False
            if event.key == pygame.K_d:
                avance = 5
            if event.key == pygame.K_s:
                avance = 0
            if event.key == pygame.K_q:
                avance = -5
            if event.key == pygame.K_k:
                check_radar(x, y)
            if event.key == pygame.K_u:
                d_angle = +5
            if event.key == pygame.K_i:
                d_angle = 0
            if event.key == pygame.K_o:

        display.blit(car, (x, y))
        d_angle = -5
    x += avance
    angle += d_angle
    car = pygame.transform.rotate(car, angle)
    display.blit(text_surface, (30, 30))
    pygame.display.flip()


pygame.quit()
