# 🔢 Random Number Guessing Game / Juego de Adivinar el Número Aleatorio

## 📖 Description / Descripción

This is a simple Python console game where the player tries to guess a randomly generated number between 1 and 100.  
Este es un juego de consola en Python donde el jugador intenta adivinar un número aleatorio entre 1 y 100.

---

## 🎮 How to Play / Cómo Jugar

**English:**

1. Run the script.
2. The game will prompt you to guess a number between **1 and 100**.
3. You have **5 attempts** to guess the correct number.
4. After each guess, you'll receive one of the following hints:
   - 🔥 **"You are so near"** – You are very close (within 5 units).
   - 🔥❄️ **"Not too near, not too far"** – You're somewhat close (between 6–10 units).
   - ❄️ **"You are so far"** – Your guess is more than 10 units away.
5. If you guess the number correctly, the game ends with a winning message.
6. If you use all 5 attempts without guessing correctly, the game will reveal the number.

**Español:**

1. Ejecuta el script.
2. El juego te pedirá que adivines un número entre **1 y 100**.
3. Tienes **5 intentos** para adivinar el número correcto.
4. Después de cada intento, recibirás una de estas pistas:
   - 🔥 **"Estás muy cerca"** – Estás a menos de 5 números de distancia.
   - 🔥❄️ **"Ni muy cerca, ni muy lejos"** – Estás a entre 6 y 10 números.
   - ❄️ **"Estás muy lejos"** – Estás a más de 10 números del número correcto.
5. Si adivinas el número, el juego termina con un mensaje de victoria.
6. Si usas los 5 intentos sin acertar, el juego revela el número correcto.

---

## 🛠️ How It Works / Cómo Funciona

- The game uses Python’s `random` module to generate the secret number.  
- El juego utiliza el módulo `random` de Python para generar el número secreto.
- Player inputs are taken through the `input()` function and compared to the secret number.  
- Las entradas del jugador se toman con la función `input()` y se comparan con el número secreto.
- Based on how close the guess is, a message is shown.  
- Dependiendo de qué tan cerca esté el número ingresado, se muestra un mensaje.

---

## 📋 Requirements / Requisitos

- Python 3.x

---

## 🚀 Getting Started / Cómo Empezar

1. Save the code into a Python file (e.g., `guessing_game.py`).  
   Guarda el código en un archivo Python (por ejemplo, `guessing_game.py`).
2. Run the script using your terminal or an IDE:  
   Ejecuta el script desde tu terminal o IDE:

```bash
python guessing_game.py
