   M S B A M L   `   `   `  ����   SpeechToText-WPF-Sample>    8Microsoft.CognitiveServices.SpeechRecognition.MainWindow   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     -     �Name$  _mainWindow�� � Title$; 5Microsoft.CognitiveServices.SpeechRecognition Example��$��5,5,5,5q�$	��800��.��� $��5q� � RowDefinitions �� $
��auto ��� $��* � � ColumnDefinitions �� $��* �$	��200���� $��* �$	��200��.+��� $��0��$��0��$
��Left=�.��20Project Cognitive Services Speech To Text Sample� $��0��$��1��$��0,0,10,0q�.+���  �� Orientation$ 
Horizontal=�$��Right=�.+��� $��Stretch=�$��Stretch=�$��2q�����  �� ElementName$ _mainWindow�� �� Path$ SubscriptionKey� �� Mode$ TwoWay=��� -   $��
5, 0, 0, 0q�$��
5, 0, 5, 0q�$��30��$	��Top=�.��
Save Key�� -   $��
5, 0, 0, 0q�$��
5, 0, 5, 0q�.��
Delete Key�� -   $��Center=�$��
5, 0, 0, 0q�$��
5, 0, 5, 0q�$��Get Key��� $��1��$��0�� �� $
��auto ��� $��* ��� $
��auto �.+��� -    ��Name$ _radioGroup��$��0��$��10,10,10,10q�$��0, 0, 10, 10q�.���� $ Vertical=�.+��� .��Speech Recognition Source:	� -   	 	�Name$	 _micRadioButton��$��10, 10, 0, 0q�
 d� 	IsChecked
 �� $ _mainWindow��$# IsMicrophoneClientShortPhrase�.��&$Use Microphone with ShortPhrase mode	� -   $	 _micDictationRadioButton��$��10, 10, 0, 0q�
 �� $ _mainWindow��$! IsMicrophoneClientDictation�.��(&Use Microphone with LongDictation mode	� -   $	 _micIntentRadioButton��$��10, 10, 0, 0q�
 �� $ _mainWindow��$" IsMicrophoneClientWithIntent�.��%#Use Microphone and intent detection�� $��30,0,0,0q�.��" (* LUIS registration is needed.)	� -	   $	 _dataShortRadioButton��$��10, 10, 0, 0q�
 �� $ _mainWindow��$ IsDataClientShortPhrase�.��#!Use wav file for ShortPhrase mode	� -
   $	 _dataLongRadioButton��$��10, 10, 0, 0q�
 �� $ _mainWindow��$ IsDataClientDictation�.��%#Use wav file for LongDictation mode	� -   $!	 _dataShortIntentRadioButton��$��10, 10, 0, 0q�
 �� $ _mainWindow��$ IsDataClientWithIntent�.��#!Use wav file and intent detection�� $��30,0,0,0q�.��" (* LUIS registration is needed.)� $��2��$��10, 0, 10, 10q� �� $
��auto ��� $
��auto �.+��� -    ��Name$ _startButton��$��0��$��Start _Recognition��$��5q�$��5q��� -    ��Name$ _logText��$��1��$��1��$��Stretch=�$��Stretch=� �� TextWrapping$
 Wrap=�$�� ��" �� VerticalScrollBarVisibility$ Visible=�$��0, 10, 10, 10q�