#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for batch
processing.

Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

# [START import_libraries]
import argparse
import io
from pydub import AudioSegment
import wave
import audioop
import os
import re
import sys
import distance
import pandas as pd

# [END import_libraries]

# [Start read_script]
script_file = open("C:/Users/luopa/Desktop/Cognitive/script.txt", "r", encoding="utf-8")
script=script_file.read().encode('utf-8').decode('utf-8-sig')
script_file.close()
script_list=script.split()
# [END read_script]

# [Start output_dictionary]
d = {}
# [END output_dictionary]

# [START def_transcribe_file]
def transcribe_file(speech_file_directory):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]


    directory = os.fsencode(speech_file_directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".wav"):
            transcribe_result=[]
            stereo = wave.open(directory.decode("utf-8") + "/" + filename, 'rb')
            mono = wave.open("C:/Users/luopa/Desktop/Cognitive/mono_files/" + filename,
                             'wb')  # we will create the mono files here , specify the mono_filepath
            mono.setparams(stereo.getparams())
            mono.setnchannels(1)
            mono.writeframes(audioop.tomono(stereo.readframes(float('inf')), stereo.getsampwidth(), 1, 1))
            mono.close()

            audio_file=io.open("C:/Users/luopa/Desktop/Cognitive/mono_files/" + filename, 'rb')
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code='en-US')
            #[END migration_audio_config_file]

            #[START migration_sync_response]
            try:
                response = client.recognize(config, audio)
            except:
                pass
            #[END migration_sync_request]
            if len(response.results)==0:
                continue
            else:
                alternatives = response.results[0].alternatives
                for alternative in alternatives:
                    transcribe_result.append(alternative.transcript)

            # [START accuracy_test]
            transcribe_result_list = ' '.join(transcribe_result).split()
            accuracy = 1-distance.nlevenshtein(script_list,transcribe_result_list)
            # [END accuracy_test]

            # [START Writing output to txt]
            user_name=re.findall('\__(.*?)\__', filename)
            print(user_name[0])
            if user_name[0]=='':
                result_name=filename
            else:
                result_name=user_name[0]
            result_file = open('C:/Users/luopa/Desktop/Cognitive/result/'+result_name+'.txt', 'w')
            for item in transcribe_result:
                result_file.write("%s\n" % item)
            d[result_name] = accuracy
            # [END Writing output to txt]

            #[END migration_sync_response]
        #[END def_transcribe_file]

        #[START def_transcribe_gcs]
        else:
            continue
    # [Start dict_to_csv]
    data = pd.DataFrame.from_dict(d,orient='index')
    data.to_csv('C:/Users/luopa/Desktop/Cognitive/result/final_result.csv')
    # [END dict_to_csv]



def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket("audio_files_bucket")
    for blob in bucket.list_blobs(prefix="azure_audio_files/"):
        if blob.name.endswith(".wav"):
            transcribe_result = []
            stereo = wave.open("gs://"+bucket.name + "/" + blob.name, 'rb')
            mono = wave.open("gs://audio_files_bucket/mono_files/" + blob.name,
                             'wb')  # we will create the mono files here , specify the mono_filepath
            mono.setparams(stereo.getparams())
            mono.setnchannels(1)
            mono.writeframes(audioop.tomono(stereo.readframes(float('inf')), stereo.getsampwidth(), 1, 1))
            mono.close()

            audio_file = io.open("gs://audio_files_bucket/mono_files/" + blob.name, 'rb')
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code='en-US')
            # [END migration_audio_config_file]

            # [START migration_sync_response]
            try:
                response = client.recognize(config, audio)
            except Exception:
                sys.exc_clear()

            # [END migration_sync_request]
            if len(response.results) == 0:
                continue
            else:
                alternatives = response.results[0].alternatives
                for alternative in alternatives:
                    transcribe_result.append(alternative.transcript)
                print(transcribe_result)

                # [START evaluate_accuracy]
                result_string = ' '.join(transcribe_result)

                # [END evaluate_accuracy]


                # [END migration_sync_response]
        # [END def_transcribe_file]

        # [START def_transcribe_gcs]
        else:
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    args = parser.parse_args()
    if args.path.startswith('gs://'):
        transcribe_gcs(args.path)
    else:
        transcribe_file(args.path)
