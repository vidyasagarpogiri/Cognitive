# The script is written to test the performance of IBM API for .wav format audio files recorded
# Accuracy result will be produced for both 'stereo' format of .wav file or 'mono' format of .wav file
# Therefore only the ouput of stereo files will be written to txt file

# [START import_libraries]
import requests
import json
import sys
import subprocess
import os
import argparse
import io
from pydub import AudioSegment
import wave
import audioop
import re
import distance
import pandas as pd
import string
from nltk.corpus import stopwords
# [END import_libraries]

# [START Set Configuration Parameter]
# IBM bluemix API url
url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize'
# bluemix authentication username
username = '950e6fa2-b149-4b59-966f-f223972b0218'
# bluemix authentication password
password = 'L7HDD2jgqrXC'
# Open audio file(.wav) in wave format
headers={'Content-Type': 'audio/wav'}
# [END Set Configuration Parameter]

# [Start read_script]
script_file = open("C:/Users/luopa/Desktop/Cognitive/script.txt", "r", encoding="utf-8")
script=script_file.read().encode('utf-8').decode('utf-8-sig').lower()
script_file.close()
translator = script.maketrans('', '', string.punctuation)
script_list=script.translate(translator).split()
filtered_script = [word for word in script_list if word not in stopwords.words('english')]
# [END read_script]

# [Start output_dictionary]
d_stereo = {}
d_mono = {}
# [END output_dictionary]

# [START Iterate Through Files]
directory = os.fsencode('C:/Users/luopa/Desktop/Cognitive/azure_audioclips')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)

    if filename.endswith(".wav"):
        transcribe_result_stereo = []
        transcribe_result_mono = []

        # [ (Optional) START Get Result for Stereo Files]
        stereo_file = io.open("C:/Users/luopa/Desktop/Cognitive/azure_audioclips/" + filename, 'rb')
        r_stereo = requests.post(url, data=stereo_file, headers=headers, auth=(username, password)).json()

        if len(r_stereo['results']) == 0:
            continue

        else:
            # [START Fetch Information From File Name]
            user_country = re.findall('\__(.*?)\__', filename)
            result_name = filename.split('@')[0]
            if user_country[0] == '':
                result_country = filename
            else:
                result_country = user_country[0]
            # [END Fetch Information From File Name]

            #Combine Results
            result_file = open('C:/Users/luopa/Desktop/Cognitive/ibm_result/' + result_name + '.txt', 'w')
            for item in r_stereo['results']:
                transcribe_result_stereo.append(item['alternatives'][0]['transcript'].lower())
            for item1 in transcribe_result_stereo:
                result_file.write("%s\n" % item1)
            result_file.close()

        # [START Collecting Accuracy Result - stereo]
            transcribe_result_list_stereo = ' '.join(transcribe_result_stereo).split()
            filtered_result_stereo = [word for word in transcribe_result_list_stereo if word not in stopwords.words('english')]
            accuracy_stereo = 1 - distance.nlevenshtein(script_list, transcribe_result_list_stereo)
            exact_match_stereo = len(set(filtered_script).intersection(filtered_result_stereo)) / len(set(filtered_script))
            d_stereo[result_name] = [accuracy_stereo, exact_match_stereo, result_country]
        # [END Collecting Accuracy Result - stereo]

        # [ (Optional) END Get Result for Stereo Files]

    # [ START Get Result for Mono File]
            mono_file = io.open("C:/Users/luopa/Desktop/Cognitive/mono_files/" + filename, 'rb')
            r_mono = requests.post(url, data=mono_file, headers=headers, auth=(username, password)).json()
            for item in r_mono['results']:
                transcribe_result_mono.append(item['alternatives'][0]['transcript'].lower())

        # [START Collecting Accuracy Result - Mono]
            transcribe_result_list_mono = ' '.join(transcribe_result_mono).split()
            filtered_result_mono = [word for word in transcribe_result_list_mono if word not in stopwords.words('english')]
            accuracy_mono = 1 - distance.nlevenshtein(script_list, transcribe_result_list_mono)
            exact_match_mono = len(set(filtered_script).intersection(filtered_result_mono)) / len(set(filtered_script))
            d_mono[result_name] = [accuracy_mono, exact_match_mono, result_country]
        # [END Collecting Accuracy Result - Mono]

# [Start dict_to_csv]
data_stereo = pd.DataFrame.from_dict(d_stereo, orient='index')
data_stereo.columns = ['overall_accuracy', 'exact_match_accuracy', 'country']
data_stereo.to_csv('C:/Users/luopa/Desktop/Cognitive/ibm_result/result_stereo.csv')

data_mono = pd.DataFrame.from_dict(d_mono, orient='index')
data_mono.columns = ['overall_accuracy', 'exact_match_accuracy', 'country']
data_mono.to_csv('C:/Users/luopa/Desktop/Cognitive/ibm_result/result_mono.csv')
# [END dict_to_csv]



