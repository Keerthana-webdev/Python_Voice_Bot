## Python Voice Bot
A simple Python voice assistant that listens for your commands and performs actions like opening websites, telling the time/date, and replying with voice responses.

---

### Features
- Text-to-Speech using `pyttsx3`
- Speech Recognition with `speech_recognition`
- Opens websites using `webbrowser`
- Interactive voice responses

---

### Project Structure
```
Python Voice Bot/
├── Speech_rec.py          # Main voice bot script
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```
---

### Installation

#### Prerequisites
- Python 3.6 or higher
- A working microphone
- Internet connection for speech recognition

#### Step-by-Step Installation
1️⃣ **Clone the repository:**
   ```bash
   git clone https://github.com/Keerthana-webdev/Python_Voice_Bot.git
   cd python-voice-bot
   ```

2️⃣ **Install Python dependencies:**
   ```bash
   pip install speechrecognition pyttsx3
   ```

   Or if you prefer using a requirements file, create a `requirements.txt` with:
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

3️⃣ **Additional setup for speech recognition:**
   - On Windows: The `speechrecognition` library should work out of the box with PyAudio.
   - On Linux/Mac: You may need to install PyAudio separately:
     ```bash
     pip install pyaudio
     ```
   - If you encounter issues with PyAudio, you can use the alternative:
     ```bash
     pip install pipwin
     pipwin install pyaudio
     ```
---

### Usage
Run the voice assistant from the project folder:
```powershell
python Speech_rec.py
```

Speak commands like:
- "YouTube"
- "Google"
- "Gmail"
- "Time"
- "Date"
- "Hello"
- "Who are you"
- "Stop" / "Exit" / "Quit"

---

### Requirements
- `speech_recognition` - For speech-to-text conversion
- `pyttsx3` - For text-to-speech functionality
- `webbrowser` - Built-in Python module for opening URLs
- `datetime` - Built-in Python module (currently unused but imported)
- `time` - Built-in Python module for delays

---

### Notes
- The bot uses Google speech recognition, so internet access is required for recognizing spoken commands.
- If the microphone is not detected, verify your audio device settings.

---

### Contributing
Feel free to fork this project and add more voice commands!

---

### Author

#### Keerthana S



