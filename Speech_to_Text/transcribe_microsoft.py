import os
import re
import sys
import distance
import pandas as pd
import string
import inflect
from nltk.corpus import stopwords

# [START prepare conversion from numeric number to word representation]
p = inflect.engine()
def convert_to_word(word):
    if p.number_to_words(word)=="zero":
        return(word)
    else:
        return(p.number_to_words(word))
# [END prepare conversion from numeric number to word representation]

# [Start output_dictionary]
d = {}
# [END output_dictionary]

# [Start read_script]
script_file = open("C:/Users/luopa/Desktop/Cognitive/script.txt", "r", encoding="utf-8")
script=script_file.read().encode('utf-8').decode('utf-8-sig').lower()
script_file.close()
translator = script.maketrans('', '', string.punctuation)
script_list=script.translate(translator).split()
filtered_script = [word for word in script_list if word not in stopwords.words('english')]
# [END read_script]

# [START parse file]
transcribe_file_directory="C:/Users/luopa/Desktop/Cognitive/microsoft_result"
directory = os.fsencode(transcribe_file_directory)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    transcribe_file = open("C:/Users/luopa/Desktop/Cognitive/microsoft_result/"+filename, "r", encoding="utf-8")
    transcribe_result = transcribe_file.read().encode('utf-8').decode('utf-8-sig').lower()
    transcribe_file.close()

    # [START clean result file]
    result_trans = transcribe_result.maketrans('', '', string.punctuation)
    result_list = transcribe_result.translate(result_trans).split()
    result_list = [convert_to_word(word) for word in result_list]
    filtered_result = [word for word in result_list if word not in stopwords.words('english')]
    # [END clean result file]

    # [START calculate accuracy rate]
    accuracy = 1 - distance.nlevenshtein(script_list, result_list)
    exact_match = len(set(filtered_script).intersection(filtered_result)) / len(set(filtered_script))
    # [END calculate accuracy rate]

    # [START Writing output to csv]
    user_country = re.findall('\__(.*?)\__', filename)
    result_name = filename.split('@')[0]
    if user_country[0] == '':
        result_country = filename
    else:
        result_country = user_country[0]
    d[result_name] = [accuracy, exact_match, result_country]

    # [Start dict_to_csv]
    data = pd.DataFrame.from_dict(d, orient='index')
    data.columns = ['overall_accuracy', 'exact_match_accuracy', 'country']
    data.to_csv('C:/Users/luopa/Desktop/Cognitive/microsoft_result/final_result.csv')
    # [END dict_to_csv]

    # [END Writing output to csv]
# [END parse file]