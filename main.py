import os

print("Welcome to ROBO Speaker - Created by Ritik")
while True:
    text = input("Type what you want me to speak : ")
    if text == "quit":
        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'"Bye Bye Friend - See you later"\')"'
        os.system(command)
        break
    command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    os.system(command)