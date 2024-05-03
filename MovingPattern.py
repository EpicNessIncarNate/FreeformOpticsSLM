import pygame
import os
import glob
import time
#This script requires each pattern for each frame to be premade
# 1) convert each frame of the video you want to project to an image format supported by the Holoeye SLM Pattern Generator (jpg, png,...)
# 2) use the Holoeye SLM Pattern Generator to generate patterns for each image
# 3) place the images in a seperate directory inside the DOEs directory
# 4) change the path on line 37 to the directory you just made
def display_image(image_path, screen):
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    pygame.display.flip()

def main():
    pygame.init()

    displays = [pygame.display.Info() for i in range(pygame.display.get_num_displays())]

    if len(displays) < 2:
        print("Secondary display not found.")
        return

    secondary_display = displays[1]

    display_width = secondary_display.current_w
    display_height = secondary_display.current_h
    image_width = 1920
    image_height = 1080
    x_offset = (display_width - image_width) // 2
    y_offset = (display_height - image_height) // 2

    os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(1920, 0)

    screen = pygame.display.set_mode((1920, 1080))

    image_paths = glob.glob("DOEs/coord/*.png")  #Change this path to the directory with the correct images
    num_images = len(image_paths)
    current_image_index = 0
    last_switch_time = time.time()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = time.time()
        elapsed_time = current_time - last_switch_time

        if elapsed_time >= 1/60:
            last_switch_time = current_time
            current_image_index = (current_image_index + 1) % num_images
            image_path = image_paths[current_image_index]
            display_image(image_path, screen)

    pygame.quit()

if __name__ == "__main__":
    main()
