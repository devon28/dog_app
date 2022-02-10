# name: Devon Miller
# project: individual final project
# date: 1/21/2021

from tkinter import *
import random
import time
import PIL
from PIL import Image, ImageTk
from tkinter import filedialog, ttk
import json
import wikipedia
import json
import re

# description: user interface from dog app, consists of main staart screen, 7 question
#               screens and 3 results pages, first reluts page converts wav barks to english
#               second returns dog breed facts from wikipedia, third finds local parks
#               based on zip code, communicates with other files via json



def start():
    """home page displays features pressing start begins questions"""
    window = Tk()
    window.title("Dog App")
    window.geometry('600x600')
    myimage = Image.open("images/doggie.jpg")
    resized = myimage.resize((600, 600), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(resized)
    background_canvas = Canvas(window, width=600, height=600)
    background_canvas.pack(fill="both", expand=True)
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 50, text="Unleash Your Dog", font=("Ariel", 50))
    feat1 = background_canvas.create_text(140, 150, anchor= CENTER, text="• Translate barks to english", font=("Ariel", 20))
    feat2 = background_canvas.create_text(130, 250, anchor=CENTER, text="• Learn about your breed", font=("Ariel", 20))
    feat3 = background_canvas.create_text(100, 350, anchor=CENTER, text="• Find local parks", font=("Ariel", 20))
    start_button = Button(window, text="Get Started", command=lambda:breed_question(background_canvas, bg, window))
    start_button_window = background_canvas.create_window(245, 470, anchor="nw", window=start_button)
    window.mainloop()


def breed_question(background_canvas, bg, window):
    """breed question"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    breed = None
    breedoptions = ["australian shepherd", "beagle"]
    clicked = StringVar()
    clicked.set("Breed")
    breed_drop = OptionMenu(window, clicked, *breedoptions)
    number = background_canvas.create_text(250, 525, text="question 1/7", font=("Ariel", 10))
    option_window = background_canvas.create_window(270, 290, anchor="nw", window=breed_drop)
    breed_text = background_canvas.create_text(150, 300, text="Whaat breed is your dog?", font=("Ariel", 20))
    breed = clicked
    name_button = Button(window, text="Continue", command=lambda: name_question(background_canvas, bg, window, breed))
    name_button_window = background_canvas.create_window(245, 470, anchor="nw", window=name_button)
    skip_button = Button(window, text="Skip", command=lambda: name_question(background_canvas, bg, window, breed))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)
   # breed_data = {"breed": breed.get()}
    #with open("breedfacts.json", "w") as outfile:
     #   breed_json = json.dump(breed_data, outfile)
  #  exec(open("dogfactsfinder.py").read())

def name_question(background_canvas, bg, window, breed):
    """name question"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    name = Entry(window, font=("Ariel", 20), width=10, bg="orange")
    name_window = background_canvas.create_window(320, 280, anchor="nw", window=name)
    name_text = background_canvas.create_text(175, 300, text="What's your furry friends name?", font=("Ariel", 20))
    number = background_canvas.create_text(250, 525, text="question 2/7", font=("Ariel", 10))
    size_button = Button(window, text="Continue", command=lambda: size_question(background_canvas, bg, window, breed, name))
    size_button_window = background_canvas.create_window(245, 470, anchor="nw", window=size_button)
    skip_button = Button(window, text="Skip", command=lambda: size_question(background_canvas, bg, window, breed, name))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)

def size_question(background_canvas, bg, window, breed, name):
    """size question"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    sizeoptions = ["<50lbs", "50-75lbs", "75-100lbs", "100-150lbs", "150-200lbs", ">200lbs"]
    click=StringVar()
    click.set("Size")
    size_drop = OptionMenu(window, click, *sizeoptions)
    size_window = background_canvas.create_window(230, 290, anchor="nw", window=size_drop)
    size_text = background_canvas.create_text(130, 300, text="How big is your dog?", font=("Ariel", 20))
    size = click
    number = background_canvas.create_text(250, 525, text="question 3/7", font=("Ariel", 10))
    age_button = Button(window, text="Continue", command=lambda: age_question(background_canvas, bg, window, breed, name, size))
    age_button_window = background_canvas.create_window(245, 470, anchor="nw", window=age_button)
    skip_button = Button(window, text="Skip", command=lambda: age_question(background_canvas, bg, window, breed, name, size))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)


def age_question(background_canvas, bg, window, breed, name, size):
    """age question"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    ageoptions = ["<1 year old", "1-3 years old", "4-7 years old", "8-11 years old", ">12 years old"]
    ageclick = StringVar()
    ageclick.set("Age")
    age_drop = OptionMenu(window, ageclick, *ageoptions)
    age_window = background_canvas.create_window(230, 290, anchor="nw", window=age_drop)
    age_text = background_canvas.create_text(130, 300, text="How old is your dog?", font=("Ariel", 20))
    age = ageclick
    number = background_canvas.create_text(250, 525, text="question 4/7", font=("Ariel", 10))
    gender_button = Button(window, text="Continue", command=lambda: gender_question(background_canvas, bg, window, breed, name, size, age))
    gender_button_window = background_canvas.create_window(245, 470, anchor="nw", window=gender_button)
    skip_button = Button(window, text="Skip", command=lambda: gender_question(background_canvas, bg, window, breed, name, size, age))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)


def gender_question(background_canvas, bg, window, breed, name, size, age):
    """gender question"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    sexoptions = ["Boy", "Girl"]
    sexclick = StringVar()
    sexclick.set("Gender")
    sex_drop = OptionMenu(window, sexclick, *sexoptions)
    sex_window = background_canvas.create_window(270, 290, anchor="nw", window=sex_drop)
    sex_text = background_canvas.create_text(150, 300, text="Is he a boy or is she a girl?", font=("Ariel", 20))
    sex = sexclick
    number = background_canvas.create_text(250, 525, text="question 5/7", font=("Ariel", 10))
    zip_button = Button(window, text="Continue", command=lambda: zip_question(background_canvas, bg, window, breed, name, size, age, sex))
    zip_button_window = background_canvas.create_window(245, 470, anchor="nw", window=zip_button)
    skip_button = Button(window, text="Skip", command=lambda: zip_question(background_canvas, bg, window, breed, name, size, age, sex))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)


def zip_question(background_canvas, bg, window, breed, name, size, age, sex):
    """asks user for zip code, optional"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    zip = Entry(window, font=("Ariel", 20), width=10, bg="orange")
    area_window = background_canvas.create_window(245, 284, anchor="nw", window=zip)
    area_text = background_canvas.create_text(135, 300, text="What is your zip code?", font=("Ariel", 20))
    number = background_canvas.create_text(250, 525, text="question 6/7", font=("Ariel", 10))
    upload_button = Button(window, text="Continue", command=lambda: upload_question(background_canvas, bg, window, breed, name, size, age, sex, zip))
    upload_button_window = background_canvas.create_window(245, 470, anchor="nw", window=upload_button)
    skip_button = Button(window, text="Skip", command=lambda: upload_question(background_canvas, bg, window, breed, name, size, age, sex, zip))
    skip_button_window = background_canvas.create_window(205, 470, anchor="nw", window=skip_button)


def upload_question(background_canvas, bg, window, breed, name, size, age, sex, zip):
    """asks user to upload audio"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    title = background_canvas.create_text(220, 100, text="About your dog", font=("Ariel", 50))
    number = background_canvas.create_text(260, 525, text="question 7/7", font=("Ariel", 10))
    audio_text = background_canvas.create_text(175, 300, text="Upload audio of your dogs bark:", font=("Ariel", 20))
    audio = audio_button = Button(window, text='upload audio .wav file', command=lambda: open_audio(breed))
    audio_button_window = background_canvas.create_window(320, 290, anchor="nw", window=audio_button)
    start_button = Button(window, text="Continue", command=lambda:next(background_canvas, bg, window, name, zip, breed, size, age, sex))
    start_button_window = background_canvas.create_window(225, 470, anchor="nw", window=start_button)



def next(background_canvas, bg, window, name, zip, breed, size, age, sex):
    """writes all data to jsons files and prompts results screen"""
    data ={"name":name.get(), "size":size.get(), "age":age.get(), "sex":sex.get(), "zip":zip.get()}
    with open('json_data.json', 'w') as outfile:
        json_data = json.dump(data, outfile)
    breed_data = {"breed": breed.get()}
    print(breed.get())
    with open("breedfacts.json", "w") as outfile:
        breed_json = json.dump(breed_data, outfile)
    #exec(open("dogfactsfinder.py").read())
    results(background_canvas, bg, window, name, zip, breed)
  #  exec(open("dogfactsfinder.py").read())


def results(background_canvas, bg, window, name, zip, breed):
    """translation results page"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    tobreedfacts = Button(window, text="To Breed Facts", command=lambda: dogfacts(background_canvas, bg, window, name, zip, breed))
    tobreedfacts_window = background_canvas.create_window(230, 470, anchor="nw", window=tobreedfacts)
    if name.get() !="":
        title = background_canvas.create_text(250, 100, text=name.get()+" is trying to say:", font=("Ariel", 50))
        with open("json_audio.json", "r") as infile:
            phrase_dict = json.load(infile)
        phrase = phrase_dict.get("phrase")
        translation = background_canvas.create_text(200, 290, text=phrase, font=("Ariel", 22))

    else:
        title = background_canvas.create_text(270, 100, text="Your dog is trying to say:", font=("Ariel", 50))
        with open("json_audio.json", "r") as infile:
            phrase_dict = json.load(infile)
        phrase = phrase_dict.get("phrase")
        translation = background_canvas.create_text(200, 290, text=phrase, font=("Ariel", 22))

    page = background_canvas.create_text(277, 525, text="Results Page 3/3", font=("Ariel", 10))


def dogfacts(background_canvas, bg, window, name, zip, breed):
    """breed facts page"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    back = Button(window, text="Back", command=lambda: results(background_canvas, bg, window, name, zip, breed))
    back_window = background_canvas.create_window(220, 470, anchor="nw", window=back)
    parks = Button(window, text="Find Local Parks", command=lambda: findparks(background_canvas, bg, window, name, zip, breed))
    parks_window = background_canvas.create_window(272, 470, anchor="nw", window=parks)
    if breed.get() != "Breed":
        facts = []
        title = background_canvas.create_text(300, 100, text="Here's some info about \n "+breed.get()+"s:", font=("Ariel", 28))
        with open("breedfacts.json", "r") as infile:
            dictfacts = json.load(infile)
        fact1 = background_canvas.create_text(300, 190, text= dictfacts.get("1"), font=("Ariel", 12))
        fact2 = background_canvas.create_text(300, 290, text=dictfacts.get("2"), font=("Ariel", 12))
        fact3 = background_canvas.create_text(300, 390, text=dictfacts.get("3"), font=("Ariel", 12))

    else:
        title = background_canvas.create_text(300, 220, text="You need to enter your dogs breed \n to get facts about them",font=("Ariel", 28))
    page = background_canvas.create_text(277, 525, text="Results Page 2/3", font=("Ariel", 10))


def findparks(background_canvas,bg, window, name, zip, breed):
    """local parks page"""
    background_canvas.delete("all")
    background_canvas.create_image(0, 0, image=bg, anchor="nw")
    back = Button(window, text="Back", command=lambda: dogfacts(background_canvas, bg, window, name, zip, breed))
    back_window = background_canvas.create_window(252, 470, anchor="nw", window=back)
    if zip.get() != "":
        print(zip)
        title1 = background_canvas.create_text(300, 100, text="We've found these parks near you!", font=("Ariel", 35))
    else:
        title1 = background_canvas.create_text(300, 220, text="You need to enter your zip \n code to find local parks", font=("Ariel", 35))
    page = background_canvas.create_text(277, 525, text="Results Page 3/3", font=("Ariel", 10))


def open_audio(breed):
    """opens user uploaded audio file and writes path to json file"""
    global audio_file
    audio_file = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg"), ("All Files", "*.*")))
    data = {"audio": audio_file, "breed": breed.get()}
    with open('json_audio.json', 'w') as outfile:
        json_string = json.dump(data, outfile)


if __name__ == '__main__':
    start()