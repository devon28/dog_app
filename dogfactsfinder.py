import wikipedia
import json
import re

def dog_facts():
    line_len = 65
    dict_index = 1
    with open("breedfacts.json", "r") as infile:
        breed_dict = json.load(infile)
    breed = breed_dict.get("breed")
    try:
        result = wikipedia.summary(breed, sentences=3)
    except:
        result = wikipedia.summary("Beagle + " dog", sentences=3)
    bullets = re.split("[.?!]", result)
    index = 1
    bullet_dict = {}
    for bullet in bullets:
        lines = len(bullet) // line_len
        for i in range(lines):
            index = (i+1) * line_len
            while bullet[index] != " ":
                index += 1
            bullet = bullet[:index] + "\n " + bullet[index:]
            bullet_dict[dict_index] = "•"+ bullet
        dict_index += 1
    with open("breedfacts.json", "w") as outfile:
        dogs = json.dump(bullet_dict, outfile)
    print(bullet_dict)
if __name__ == "__main__":
    dog_facts()
