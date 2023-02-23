import pygame
import math
import time
import numpy as np

CAR_SIZE = 60

CAR_ANGLE = 0
POS_CENTER = {"X": 522, "Y": 522}

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def getCenter(list=False):
    global POS_CENTER
    if list:
        return POS_CENTER["X"], POS_CENTER["Y"]


def getCorner(list=False):
    global POS_CENTER
    if list:
        return POS_CENTER["X"]-CAR_SIZE/2, POS_CENTER["Y"]-CAR_SIZE/2


def create_display():
    pygame.init()
    display = pygame.display.set_mode((1200, 600))
    return display


def load_image():
    background_image = pygame.image.load(
        "/Users/davidzhu/Desktop/Projet_info/NEAT_autonomous_vehicule/map2.png")
    background_image = pygame.transform.scale(background_image, (1200, 600))
    car_image = pygame.image.load(
        "/Users/davidzhu/Desktop/Projet_info/NEAT_autonomous_vehicule/car.png")
    car_image = pygame.transform.scale(car_image, (60, 60))
    return background_image, car_image


def check_LIDAR():
    # LIDAR_ANGLE_FRONT = [-90, -45, 0, 45, 90]
    LIDAR_ANGLE_FRONT = np.linspace(-120, 120, 10)
    LIDAR_ANGLE_FRONT = LIDAR_ANGLE_FRONT.astype(int)
    LIDAR_MESURE = []
    global POS_CENTER
    for LIDAR_ANGLE_VALUE in LIDAR_ANGLE_FRONT:
        LONGUEUR = 0
        X, Y = int(POS_CENTER["X"]), int(POS_CENTER["Y"])
        while not display.get_at((X, Y))[:3] == WHITE:
            LONGUEUR += 1
            X = int(
                POS_CENTER["X"] + math.cos(math.radians(360 - (CAR_ANGLE + LIDAR_ANGLE_VALUE))) * LONGUEUR)
            Y = int(
                POS_CENTER["Y"] + math.sin(math.radians(360 - (CAR_ANGLE + LIDAR_ANGLE_VALUE))) * LONGUEUR)
        LIDAR_MESURE.append({"X": X, "Y": Y})
        print(LONGUEUR)
    return LIDAR_MESURE


def print_LIDAR(LIDAR_MESURE):
    if LIDAR_MESURE == None:
        return
    global POS
    for MESURE in LIDAR_MESURE:
        print(MESURE)
        pygame.draw.circle(display, RED, [MESURE["X"], MESURE["Y"]], 2)
        pygame.draw.lines(display, RED, False, [getCenter(
            list=True), [MESURE["X"], MESURE["Y"]]])


def print_car():
    global car_image, CAR_ANGLE
    rotated_image = pygame.transform.rotate(car_image, CAR_ANGLE)
    rect = car_image.get_rect()
    rotated_rectangle = rect.copy()
    rotated_rectangle.center = rotated_image.get_rect().center
    rotated_image = rotated_image.subsurface(rotated_rectangle).copy()

    display.blit(rotated_image, getCorner(list=True))


def move_cart():
    global POS_CENTER


def run():
    DELTA_MOVE_DISTANCE = 5
    DELTA_MOVE_ANGLE = 10
    global background_image, display, car_image
    global CAR_ANGLE
    display.blit(background_image, (0, 0))
    display.blit(car_image, getCorner(list=True))
    pygame.draw.circle(display, RED, getCenter(list=True), 2)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            print(event)
            x, y = pygame.mouse.get_pos()
            print(display.get_at((x, y))[:3])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    running = False
                if event.key == pygame.K_z:
                    DELTA_MOVE_DISTANCE = 5
                if event.key == pygame.K_s:
                    DELTA_MOVE_DISTANCE = -5
                if event.key == pygame.K_k:
                    CAR_ANGLE += DELTA_MOVE_ANGLE
                if event.key == pygame.K_m:
                    CAR_ANGLE -= DELTA_MOVE_ANGLE

        POS_CENTER["X"] = int(
            POS_CENTER["X"] + math.cos(math.radians(360 - (CAR_ANGLE))) * DELTA_MOVE_DISTANCE)
        POS_CENTER["Y"] = int(
            POS_CENTER["Y"] + math.sin(math.radians(360 - (CAR_ANGLE))) * DELTA_MOVE_DISTANCE)
        display.blit(background_image, (0, 0))

        # display.blit(car_image, getCorner(list=True))
        print_car()
        LIDAR_MESURE = None
        LIDAR_MESURE = check_LIDAR()
        print_LIDAR(LIDAR_MESURE)
        pygame.display.flip()
        time.sleep(0.01)
    pygame.quit()


if __name__ == '__main__':
    display = create_display()
    background_image, car_image = load_image()
    run()
