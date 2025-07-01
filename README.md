# 🚪 Smart Motion-Sensing Door System
This is a smart door system built using the `engi1020.arduino.api` (Memorial University’s Python-Arduino interface). The system combines motion detection, audio/visual feedback, and user interaction via rotary dial input to simulate automated door access.

---

## 🧠 Project Overview
This project detects motion using a PIR sensor and responds by:
- Alerting the user with a buzzer and OLED screen
- Prompting user interaction on an RGB LCD
- Using a rotary dial to choose whether to open the door
- Controlling a servo motor to simulate door opening or closing

---

## ⚙️ Hardware Components
- **PIR Motion Sensor** (Pin 2): Detects motion
- **Button** (Pin 6): Triggers interactive access sequence
- **Rotary Dial (Potentiometer)** (Analog Pin 0): Used for YES/NO input
- **Push Button for Confirmation** (Pin 3): Confirms rotary dial selection
- **OLED Display**: Shows motion detection and messages
- **RGB LCD**: Displays interaction prompts and decisions
- **Buzzer** (Pin 5): Sounds alerts
- **LED** (Pin 4): Lights up on motion
- **Servo Motor** (Pin 7): Controls door simulation (opens to 90°, closes to 0°)

---

## 🧾 How It Works

### 🔍 Motion Detection Mode
When the button (pin 6) is **not pressed**:
- The PIR sensor checks for motion.
- If motion is detected:
  - OLED shows “MOTION DETECTED”
  - LED and buzzer are activated briefly
- If no motion:
  - OLED displays “No Motion Detected”

### 🚪 Interactive Access Mode
When the button (pin 6) **is pressed**:
1. OLED displays a “Knock Knock :)” welcome message with a smiley face.
2. Buzzer plays a chime (3 cycles).
3. RGB LCD prompts the user to open the door:
   - User selects **YES or NO** using the rotary dial.
   - Confirms the choice by pressing the button (pin 3).
4. If **YES**:
   - Servo rotates to 90° to simulate door opening.
5. If **NO**:
   - Door stays closed (servo at 0°).

---

## 🛠️ Setup
1. Connect all components to the correct GPIO and analog pins as described above.
2. Ensure the `engi1020.arduino.api` package is installed and your board is configured properly.
3. Run the Python script in a loop to keep the system active.

---

## 🧪 Example Use Cases
- Dorm room smart lock simulation
- Simple home automation demonstration
- Smart security system prototype for hackathons or labs

---

## 📸 Screenshots / Video Demo
_Add images or videos of the working system here._

---

## 📚 Credits
Built as part of the ENGI 1020 course at Memorial University of Newfoundland.  
Developed using the `engi1020.arduino.api` Python interface.

---

## ✅ Future Improvements
- Add face recognition or keypad for secure access
- Store access logs in memory or send to a server
- Add temperature or light sensors for extended functionality

