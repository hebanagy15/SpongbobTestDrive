from OpenGL.GL import *
import pygame

######################################################################
###########################texture  function #########################
######################################################################
texture_names = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def my_init():
    loadTextures()


def texture_setup(texture_image_binary, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                    GL_REPEAT)  # GL_MIRRORED_REPEAT , GL_CLAMP_TO_EDGE, GL_CLAMP_TO_BORDER
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D,
                 0,  # mipmap
                 3,  # Bytes per pixel
                 width, height,
                 0,  # Texture border
                 GL_RGBA,  # RGBA Exactly as in  pygame.image.tostring(image, "RGBA", True)
                 GL_UNSIGNED_BYTE,
                 texture_image_binary)  # texture init step [7]


def loadTextures():
    glEnable(GL_TEXTURE_2D)
    images = []
    images.append(pygame.image.load("img src/game/road10.jpg"))  # 0
    images.append(pygame.image.load("img src/game/day walls.jpeg"))  # 1
    images.append(pygame.image.load("img src/game/day sky.jpg"))  # 2
    images.append(pygame.image.load("img src/game/finalsh.jpg"))  # 3
    images.append(pygame.image.load("img src/game/fish.jpg"))  # 4
    images.append(pygame.image.load("img src/game/finalraceline.jpg"))  # 5
    images.append(pygame.image.load("img src/start/StartBg.jpg"))  # 6
    images.append(pygame.image.load("img src/end/Loser.png"))  # 7
    images.append(pygame.image.load("img src\end\Backgroung.png"))  # 8
    images.append(pygame.image.load("img src\end\sand.png"))  # 9
    images.append(pygame.image.load("img src\end\Victory.png"))  # 10
    images.append(pygame.image.load("img src/game/road7.jpg"))  # 11
    textures = [pygame.image.tostring(image, "RGBA", True)
                for image in images]

    glGenTextures(len(images), texture_names)

    for i in range(len(images)):
        texture_setup(textures[i],  # binary images
                      texture_names[i],  # identifiers
                      images[i].get_width(),
                      images[i].get_height())
