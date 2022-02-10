import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
import json
import pymongo

# Devon Miller
# Date: 2/9/2021
# Description: reads json file, extracts numerical data from audio file,
                # gets information from database, compares audio data to database
                # data then writes result to json file

def audioTraits():
    """open json with path to local wav file and dog breed, calls
    calc_traits"""

    with open("json_audio.json", "r") as infile:
        audio_dict = json.load(infile)
    file = audio_dict.get("audio")
    breed = audio_dict.get("breed")
    wav = wave.open(file, "r")
    audio = wav.readframes(-1)
    audio = np.frombuffer(audio, "int16")
    sampleRate = wav.getframerate()
    time = np.linspace(0, len(audio) / sampleRate, num=len(audio))
    calc_traits(audio, time, breed)
    makeGraph(audio, time)


def makeGraph(audio, time):
    """creates graph to show audio"""

    plt.title("Audio Amplitude")
    plt.plot(time, audio, color="blue")
    plt.ylabel("Amplitude")
    plt.show()


def calc_traits(audio, time, breed):
    """takes audio data and calulcates wavelength, amplitude
    averate destance etc for use in comparissons"""

    count = 0
    prev_wave = audio[0]
    next_wave = audio[1]
    next_wave_index = 1
    for wave in audio:
        if wave > prev_wave and wave > next_wave:
            count += 1
        elif wave < prev_wave and wave < next_wave:
            count += 1
        prev_wave = wave
        next_wave_index += 1
        if len(audio) > next_wave_index:
            next_wave = audio[next_wave_index]
        # get amppitude
    amp = 0
    for wave in audio:
        amp += abs(wave)

    wave_count = 0
    start = 0
    end = 0

    for wave in audio:
        if abs(wave) < 110:
            start += 1
        else:
            break
    for wave in reversed(audio):
        if abs(wave) < 110:
            end += 1
        else:
            break
    for wave in audio:
        if abs(wave) > 110:
            wave_count += 1

    period = time[-1] / (count / 2)
    frequency = 1 / period
    average_amplitude = amp / len(audio)
    average_distance = 1 / average_amplitude
    distance = average_distance * len(audio)
    velocity = distance / time[-1]
    wavelength = velocity / frequency
    try:
        bark_time = wave_count / len(audio[start:-end])
    except:
        bark_time = 1
    """
    dict = {}
    dict["period"] = period
    dict["frequency"] = frequency
    dict["average_amplitude"] = average_amplitude
    dict["average_distance"] = average_distance
    dict["velocity"] = velocity
    dict["wavelength"] = wavelength
    dict["bark_time"] = bark_time
    print(dict)
    print("yes")
    """
    get_values(frequency, average_amplitude, wavelength, velocity, period, bark_time, breed)


def get_values(frequency, average_amplitude, wavelength, velocity, period, bark_time, breed):
    """gets data from database to use in comparisson of data obtained from audio file"""

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["DogFacts"]
    mycol = mydb[breed]
    print(breed)
    count = 1
    data_list = []
    for x in mycol.find():
        data_list.append(x.get("dog" + str(count)))
        count += 1
    compare(frequency, average_amplitude, wavelength, velocity, period, bark_time, breed, data_list)


def compare(frequency, average_amplitude, wavelength, velocity, period, bark_time, breed, data_list):
    """compare audio data to database data to return resulting translation"""

    dog1 = data_list[0]
    dog2 = data_list[1]
    dog3 = data_list[2]
    dog4 = data_list[4]
    dog5 = data_list[4]

    dog_list = [dog1, dog2, dog3, dog4, dog5]
    dogs = [0 ,0 ,0 ,0 ,0]
    for i in range(6):
        if i == 0:
            i = "frequency"
            value = frequency
        elif i ==1:
            i = "average_amplitude"
            value = average_amplitude
        elif i == 2:
            i = "wavelength"
            value = wavelength
        elif i == 3:
            i = "velocity"
            value = velocity
        elif i ==4:
            i = "period"
            value = period
        else:
            i ="bark_time"
            value = bark_time
        value = float(value)
        dogs[0] += abs(1 -(value / float(dog1[i])))
        dogs[1] += abs(1 - (value / float(dog2[i])))
        dogs[2] += abs(1 - (value / float(dog3[i])))
        dogs[3] += abs(1 - (value / float(dog4[i])))
        dogs[4] += abs(1 - (value / float(dog5[i])))

    num = dogs[0]
    for i in dogs:
        if i < num:
            num = i

    index = dogs.index(num)
    dog_phrase = dog_list[index]
    phrase = dog_phrase.get("phrase")
    data = {"phrase": phrase}
    with open('json_audio.json', 'w') as outfile:
        json_string = json.dump(data, outfile)


if __name__ == "__main__":

    audioTraits()


"""
{"beagle1": {"breed": "beagle", "phrase": "Who's There?", "size": 40, "age": 4, 'period': 4.9213495434081264e-05, 'frequency': 20319.629629629628, 'average_amplitude': 1160.287121021248, 'average_distance': 0.0008618556406278402, 'velocity': 38.00783375168775, 'wavelength': 0.0018704983527980047, 'bark_time': 0.5685394715513049},
"beagle2": {"breed": "beagle", "phrase": "I want something!", "size": 40, "age": 4,'period': 4.842572374445305e-05, 'frequency': 20650.18181818182, 'average_amplitude': 1328.5500886415173, 'average_distance': 0.0007527002621500935, 'velocity': 33.19408156081913, 'wavelength': 0.00160744742361507, 'bark_time': 0.5051738735549022},
"beagle3": {"breed": "beagle", "phrase": "I'm excited! Let me do it!", "size": 40, "age": 4, 'period': 4.800182244207238e-05, 'frequency': 20832.542372881355, 'average_amplitude': 1327.0473038933087, 'average_distance': 0.0007535526405623876, 'velocity': 33.23167144880129, 'wavelength': 0.001595180792338646, 'bark_time': 0.507246190197202},
"beagle4": {"breed": "beagle", "phrase": "I'm so happy I love you!", "size": 40, "age": 4, 'period': 4.658135011583394e-05, 'frequency': 21467.81914893617, 'average_amplitude': 701.8376994680851, 'average_distance': 0.0014248308416003996, 'velocity': 68.39188039681918, 'wavelength': 0.003185786125844474, 'bark_time': 0.631799765953297},
"beagle5": {"breed": "beagle", "phrase": "I'm scared", "size": 40, "age": 4,'period': 4.797888928871296e-05, 'frequency': 20842.500000000004, 'average_amplitude': 507.6382575252323, 'average_distance': 0.0019699066907901334, 'velocity': 86.87288506384489, 'wavelength': 0.004168064534669299, 'bark_time': 0.5963015337273265}
}



[{"dog1":{"breed":"aussie", "phrase":"I want something now! Please!", "size":"50", "age":"5", "period": "0.00667334000667334", "frequency": "149.85", "average_amplitude": "1232.0488503401361", "average_distance": "0.0008116561285081565", "velocity": "35.7940352672097", "wavelength": "0.23886576754894695", "bark_time": "0.8733015564908206"},
{"dog2": {"breed":"aussie", "phrase":"I'm so mad", "size": "95", "age": "6", "period": "4.837382450291952e-05", "frequency": "20672.33695652174", "average_amplitude": "1690.6047027506654", "average_distance": "0.0005915043288197232", "velocity": "26.085340900949795", "wavelength": "0.0012618477028413738", "bark_time": "1"},
{"dog3": {"breed": "aussie", "phrase": "I love you!", "size": "60", "age":"6", "period": "4.5314653626116346e-05", "frequency": "22067.916666666668", "average_amplitude": "470.3347048611111", "average_distance": "0.0021261454654835604", "velocity": "102.05498234321088", "wavelength": "0.004624586175702021", "bark_time": "1"},
{"dog4": {"breed"; "aussie", "phrase": "I like talking to you", "size": "50", "age": "7", "period": "4.9192791020079604e-05", "frequency": "20328.181818181816", "average_amplitude": "1887.34775304061", "average_distance": "0.0005298440620648477", "velocity": "23.366123137059784", "wavelength": "0.0011494448124308289", "bark_time":"1"},
{"dog5": {"breed": "aussie", "phrase": "This isnt good, I wanna pee or eat", "size": "50", "age": "6", "period": "0.000997628187886642", "frequency": "1002.3774509803923", "average_amplitude": "103.53184051398337", "average_distance": "0.009658864316866236", "velocity": "425.9559163738011", "wavelength": "0.42494562897158916", "bark_time": "1"}
]




"""