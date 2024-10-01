import pygame
from pygame.locals import *
from gl import RendererRT
from figures import *
from material import *
from lights import *
from texture import Texture

# Configuración de pantalla
width =  512
height = 512

screen = pygame.display.set_mode((width, height), pygame.SCALED )
clock = pygame.time.Clock()

rt = RendererRT(screen)
rt.envMap = Texture('Textures/fondo.bmp')

rt.glClearColor(0.5,0.0,0.0)
rt.glClear()

brick = Material(difuse = [1, 0.2, 0.2], spec = 128, Ks = 0.25)
grass = Material(difuse = [0.2, 1.0, 0.2], spec = 64, Ks = 0.2)
mirror = Material(difuse = [0.9,0.9,0.9], spec = 128, Ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(difuse=[0.2,0.2,0.9], spec=128, Ks=0.2, matType=REFLECTIVE)

glass = Material(spec = 128, Ks=0.2, ior=1.5, matType= REFLECTIVE)
vidrio = Material(texture = Texture('Textures/vidrio.bmp'), spec=128, Ks=0.2, matType=REFLECTIVE)
lava = Material(texture = Texture('Textures/lava.bmp'), spec=128, Ks=0.2, matType=TRANSPARENT)
mandala = Material(texture = Texture('Textures/mandala.bmp'), spec=128, Ks=0.2, matType=TRANSPARENT)
bubuja = Material(texture = Texture('Textures/burbujas.bmp'), spec=128, Ks=0.2, matType=TRANSPARENT)
reptil = Material(texture = Texture('Textures/reptil.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
deathStar = Material(difuse=[1, 1, 1], texture=Texture('Textures/deathStar.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
champions = Material(texture = Texture('Textures/champions.bmp'), spec=128, Ks=0.2, matType=OPAQUE)
holograma = Material(texture = Texture('Textures/holograma.bmp'), spec=128, Ks=0.2, matType=OPAQUE)


# Iluminación de la escena
rt.lights.append(DirectionalLight(direction=[0, 0, -1], intensity=1.0))  # Luz desde abajo hacia arriba
rt.lights.append(AmbientLight(intensity=0.5))  # Luz ambiental débil


rt.scene.append( Sphere(position = [0, 0 , -5], radius = 1, material = brick) )
rt.scene.append( Plane(position = [0,-2, -5], normal = [0,1,0], material = brick ))
rt.scene.append( Disk(position = [0, -1, -5], normal = [0,1,0], radius = 1.5, material = mirror))
rt.scene.append( AABB(position = [0,0,-5], sizes = [1,1,1], material = brick))

# Renderizado de la escena
rt.glRender()

isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
