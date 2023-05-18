# -*- coding: utf-8 -*-

import pygame
from time import sleep
from gpiozero import LED, Button, MCP3008

led_one = LED(24)         # gpio17
led_two = LED(25)      # gpio27
led_three = LED(26)       # gpio22
led_four = LED(16)

button_one = Button(23)    # gpio2
button_two = Button(22)  # gpio3
button_three = Button(27)  # gpio4
button_four = Button(17)

potentiometer = MCP3008(channel=0)

pygame.mixer.init()
sound = pygame.mixer.Sound("snare5.wav")  # kick5.wav - snare5.wav


def toggle_led_one():
    led_one.toggle()


def toggle_led_two():
    led_two.toggle()


def toggle_led_three():
    led_three.toggle()


def toggle_led_four():
    led_four.toggle()


button_one.when_pressed = toggle_led_one
button_two.when_pressed = toggle_led_two
button_three.when_pressed = toggle_led_three
button_four.when_pressed = toggle_led_four


def get_potentiometer_value():
    """
    Récupère la valeur du potentiomètre en secondes
    """
    # Transformer la valeur du potentiomètre entre 0 et 1 en secondes
    # val_in_seconds = potentiometer.value * 10
    # return round(val_in_seconds)
    return round(potentiometer.value, 2)


while True:
    if led_one.value == 1:
        sound.play()
        # wt = get_potentiometer_value()
        # if wt < 0.5:
        #     sleep(0.5)
        # else:
        #     sleep(1)
        # pygame.time.wait(1000)
        # sleep(get_potentiometer_value())
        #         pygame.time.wait(1000)

    sleep(get_potentiometer_value())
    # pygame.time.wait(1000)

    if led_two.value == 1:
        sound.play()

    sleep(get_potentiometer_value())

    if led_three.value == 1:
        sound.play()
    sleep(get_potentiometer_value())

    if led_four.value == 1:
        sound.play()

    sleep(get_potentiometer_value())
    print(f"Vitesse : {get_potentiometer_value()}")
    # Attendre 0.1 seconde
    sleep(0.1)
    # pygame.time.wait(1000)
