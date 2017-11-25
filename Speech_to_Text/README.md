# Code Usage (Google + IBM API)
- Transcibe_v1.py: Batch processing of the .wav audio files from local folder using google speech-to-text API, use it in gcloud shell, the <transcribe_gcs(gcs_uri)> function is not working properly yet
```
python C:\Users\luopa\Desktop\Cognitive\transcribe2.py C:/Users/luopa/Desktop/Cognitive/azure_audioclips
```
- blobxfer.py: Used in command prompt for interaction with Azure Blob, use it in command prompt
```
python C:\Users\luopa\Desktop\Cognitive\blobxfer.py synapsediag693 bootdiagnostics-pauline-b3337233-6ea6-4969-83fb-6c9aa4dc38f8 C:\Users\luopa\Desktop\Cognitive --subscriptionid 438f52a6-38d6-4dcd-964c-9c6d97b3877f438f52a6-38d6-4dcd-964c-9c6d97b3877f --storageaccountkey sIfK/fOUQePs/NI2eETgDUhXVrr+gNQ4/3Ni4hg0ObLGOBDbXytZLFbeWYUljTHJRqIDt5xYkyXWi47V2BdEdg== --managementcert C:\Users\luopa\Desktop\Cognitive\Azure_Blob_Cert.cer --remoteresource pauline.b3337233-6ea6-4969-83fb-6c9aa4dc38f8.screenshot.bmp --download
```
- google_speech_streaming.py: Used for transcribing recording in real-time, use in gcloud shell, wait for 2-3 seconds and start speaking to the microphone, set ```interim_results=False``` to get the complete result after the completion of speech. Note that if <interim_results> is set to True, speaking without pausing after each sentence will lead to messy result being produced. There is also an **one miniute** limitation on the maximum length of speech each time.
```
python C:\Users\luopa\Desktop\Cognitive\google_speech_streaming.py
```
- download_from_azure.py: Used for downloading audio files to local machine
- upload_result_azure.py: Used for uploading the transcription results from local machine back to Azure file storage

# Code Usage - Microsoft Client Library
- To use the client library, the download of Microsoft Visual Studio 2015 is necessary (2017 might throw error in the code)
- Place the audio files (.wav) in the **path_to_client_library_download\Cognitive-Speech-STT-Windows-master\samples\SpeechRecognitionServiceExample\bin\x86\Debug**
- Use Visual Studio to open up SpeechToText-WPF-Sample-x86 solution file
- Edit MainWindow.xaml.cs **WriteResponseResult** class code (refer to the corresponding code in Cognitive-Speech-STT-Windows-master folder) so that it writes the transcription output to the desired location as .txt file
```
        private void WriteResponseResult(SpeechResponseEventArgs e)
        {
            if (e.PhraseResponse.Results.Length == 0)
            {
                this.WriteLine("No phrase response is available.");
            }
            else
            {
                this.WriteLine("********* Final n-BEST Results *********");
                using (StreamWriter w = File.AppendText(@"<path_to_output_txt_file>"))
                {
                    for (int i = 0; i < e.PhraseResponse.Results.Length; i++)
                    {
                        this.WriteLine(
                            "[{0}] Confidence={1}, Text=\"{2}\"",
                            i,
                            e.PhraseResponse.Results[i].Confidence,
                            e.PhraseResponse.Results[i].DisplayText);
                        w.WriteLine(e.PhraseResponse.Results[i].DisplayText);
                    }
                }
            }
        }
```
- Edit app.config as following (refer to the corresponding code in Cognitive-Speech-STT-Windows-master folder) so that the application knows what file are we using for transcription and save
```
<add key="LongWaveFile" value="<name_of_auidio_file_to_transcribe>.wav" />
```
- Build Solution (x86 in this case)
- Run solution

# Python Library
- azure-storage
- auzure-servicemanagement-legacy
- azure-common
- blobxfer
- argparse
- pydub

# Process for Demo
1. Use **download_from_azure.py** to fetch all files sitting in the target directory to a local directory
2. Run **Transcribe_v1.py** in Google Cloud SDK Shell to convert stereo .wav files to mono .wav files. In the meanwhile the mono files will be read in and being passed to google speech-to-text API. The results will be generated as .txt file for each audio files.
```
python C:\Users\luopa\Desktop\Cognitive\transcribe2.py C:/Users/luopa/Desktop/Cognitive/azure_audioclips
```
3. Upload the result to Azure file storage using **upload_result_azure.py**

# Reference
Azure Blob Storage: https://docs.microsoft.com/en-us/azure/storage/files/storage-python-how-to-use-file-storage
