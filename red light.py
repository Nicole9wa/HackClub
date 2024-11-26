import turtle
import time
import random
import keyboard 
import pygame
import tkinter as tk
import numpy as np 
import cv2  
list1 = []
pygame.init()   

def calculate_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)
def close_turtle_window():
    turtle.bye()
def calculate_sad(image1, image2):
    return np.sum(np.abs(image1 - image2))

def normalize_image(image):
    return image.astype(np.float32) / 255.0
def is_change():
    if len(list1) == 2:
        image1 = list1[0]
        image2 = list1[1]

        mse = calculate_mse(image1, image2)
        sad = calculate_sad(image1, image2)
        num_pixels = image1.size
        normalized_sad = sad / num_pixels

        print(f"MSE: {mse:.2f}")
        print(f"SAD: {normalized_sad:.2f}")

        if mse > 0.01 or normalized_sad > 0.029:
            close_turtle_window()
            create_you_lose_window()  
        list1.clear
def get_im():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        exit()
    
    list1.clear()  
    
    for _ in range(2):
        ret, frame = cap.read()
        if ret:  
            grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            normalized_frame = normalize_image(grayscale_frame)
        
            list1.append(normalized_frame)
            
            cv2.waitKey(750)
    cap.release()
    
              
            # cv2.imshow('Grayscale Frame', grayscale_frame)
    # cv2.destroyWindow('grayscale frame')


# def get_im():
#     for _ in range(2):
#         ret, frame = cap.read()
#         if ret:
#             grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             normalized_frame = normalize_image(grayscale_frame)
#             cv2.imshow('Grayscale Frame', grayscale_frame)
            
#             list1.append(normalized_frame)
#             cv2.waitKey(500) 
  
#     cap.release()
     
def calculate_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

def calculate_sad(image1, image2):
    return np.sum(np.abs(image1 - image2))

def normalize_image(image):
    return image.astype(np.float32) / 255.0     

def close_window(window):
    window.destroy()

def create_you_win_window():
    window = tk.Tk()
    window.title("You Win")
    window.geometry("1000x300")
    label = tk.Label(window, text="You Win", font=("Arial", 100 , "bold"), fg="green")
    label.pack(expand=True)   
    sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/80 Kenilworth Ave 16.wav')
    sound.play()
    window.after(10000, close_window, window)
    window.mainloop()
    quit()

def create_you_lose_window():
    window = tk.Tk()
    window.title("You LOSE")
    window.geometry("1000x300")
    label = tk.Label(window, text="You LOSE", font=("Arial", 100        , "bold"), fg="Red")
    label.pack(expand=True)
    sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/New Recording 2.wav')
    sound.play()
    window.after(10000, close_window, window)
    window.mainloop()
    quit()
                       

def create_Start_window():
    window = tk.Tk()
    window.title("Press Space to Start")
    window.geometry("1000x300")
    label = tk.Label(window, text="Press Space To Start", font=("Arial", 30, "bold"), fg="Black")
    label.pack(expand=True)
    def close_window(event):
        window.destroy()
    window.bind('<space>', close_window)
    sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/Mount Pleasant Rd.wav')
    sound.play()
    # pygame.time.delay(int(sound.get_length() * 1000))
    window.mainloop()
     
def create_countdown_window():
    window = tk.Tk()
    window.title("CountDown")
    window.geometry("1000x1000")
    countdown_number = 11
    label = tk.Label(window, text=str(countdown_number), font=("Arial", 90, "bold"), fg="black")
    label.pack(expand=True)
    def countdown():
        nonlocal countdown_number
        if countdown_number > 0:
            countdown_number -= 1
            label.config(text=str(countdown_number))
            window.after(1000, countdown)
        else:   
            window.destroy()
    countdown()
    window.mainloop()

def is_space_pressed():
    return keyboard.is_pressed('space')

def change_light(light, color, duration):
    light.color(color)

    if color == ("red"):
        sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/_Audio Message from Diana Greenwood-[AudioTrimmer.com].wav')
        sound.play()
        time.sleep(0.5)
        get_im()
        is_change()
    start_time = time.time()

    if color == ("green"):
        sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/_Audio Message from Andy Greenwood.wav')
        sound.play()
    
    if color == ("yellow"):
        sound = pygame.mixer.Sound('C:/Users/nicol/Downloads/Greenwood College School 2.wav')
        sound.play()
        
        
    
    while time.time() - start_time < duration:
        if is_space_pressed():
            return True 
        time.sleep(0.01) 
    
    light.color("grey")
    return False 

def run_traffic_light():
    while True:
        if change_light(red_light, "red", random.uniform(1.5, 2)):
            break
        if change_light(yellow_light, "yellow", random.uniform(1, 1.5 )):
            break
        if change_light(green_light, "green", random.uniform(1.5, 2.5)):
            break 

    
create_Start_window()
create_countdown_window()        


# def create_Start_window():
#     window = tk.Tk()
#     window.title("Press Space to Start")
#     window.geometry("1000x300")
#     label = tk.Label(window, text="Press Space To Start", font=("Arial", 30        , "bold"), fg="Black")
#     label.pack(expand=True)
    
#     keyboard.is_pressed('space')
#     window.mainloop()
#     window.destroy()                                        

# def k_check():
#     if keyboard.is_pressed('space'):
#         return True
#     else:
#         return False
wn = turtle.Screen()
wn.title("Stop_light")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

#red light 

red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)

#yellow light 

yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

#green light 

green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)




if __name__ == "__main__":
    run_traffic_light()
    close_turtle_window()
    create_you_win_window()  
    pygame.quit()


# while True:

#     if keyboard.is_pressed('space'):
#         break
#     red_light.color("red")
#     time.sleep(random.randrange(2, 3))
#     if keyboard.is_pressed('space'):
#         break
#     red_light.color("grey")
#     yellow_light.color("yellow")
#     time.sleep(random.randrange(0, 1))
#     if keyboard.is_pressed('space'):
#         break
#     yellow_light.color("grey")  
#     green_light.color("green")
#     if keyboard.is_pressed('space'):
#         break
#     time.sleep(random.randrange(2, 5))
#     if keyboard.is_pressed('space'):
#         break 
#     green_light.color("grey")


                               
 
      
