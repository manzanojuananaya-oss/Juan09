# dedicatoria_bonita.py
import os
import sys
import time
import shutil
from datetime import datetime

# =========================
# PERSONALIZA ESTO
# =========================
PARA = "Tu Persona Especial"
DE = "Alguien que te quiere mucho"

FRASES = [
    "Hoy quiero dedicarte unas palabras...",
    "No eres casualidad, eres regalo.",
    "Tu sonrisa tiene el poder de cambiar días grises.",
    "Tu forma de ser inspira, abraza y da paz.",
    "Gracias por existir y hacer más bonito este mundo.",
    "Nunca olvides lo valioso/a que eres.",
]

MENSAJE_FINAL = (
    "Esta dedicatoria es para recordarte que eres increíble.\n"
    "Que mereces amor bonito, paz en el corazón y sueños cumplidos.\n"
    "Sigue brillando, porque tu luz sí se nota.\n"
    "Con cariño eterno."
)

# =========================
# UTILIDADES
# =========================
RESET = "\033[0m"
BOLD = "\033[1m"
PINK = "\033[95m"
MAGENTA = "\033[35m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"

def enable_windows_ansi():
    # Intenta activar ANSI en Windows para colores
    if os.name == "nt":
        os.system("")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def terminal_width():
    return shutil.get_terminal_size((90, 30)).columns

def center(text):
    w = terminal_width()
    return text.center(w)

def typewriter(text, delay=0.03, color=WHITE, bold=False):
    style = color + (BOLD if bold else "")
    for ch in text:
        sys.stdout.write(style + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def line(char="═", color=MAGENTA):
    print(color + char * min(terminal_width(), 100) + RESET)

def box_text(text, color=CYAN):
    lines = text.split("\n")
    max_len = max(len(l) for l in lines)
    top = f"╔{'═' * (max_len + 2)}╗"
    bot = f"╚{'═' * (max_len + 2)}╝"
    print(color + top + RESET)
    for l in lines:
        print(color + f"║ {l.ljust(max_len)} ║" + RESET)
    print(color + bot + RESET)

def hearts_rain(frames=25, delay=0.08):
    symbols = ["♥", "♡", "✦", "✧", "*"]
    w = min(terminal_width(), 100)
    import random

    for _ in range(frames):
        row = [" " for _ in range(w)]
        for _ in range(w // 8):
            pos = random.randint(0, w - 1)
            row[pos] = random.choice(symbols)
        print(PINK + "".join(row) + RESET)
        time.sleep(delay)

def countdown():
    for i in [3, 2, 1]:
        clear()
        print("\n" * 5)
        print(center(PINK + BOLD + f"{i}" + RESET))
        time.sleep(0.8)

def signature():
    now = datetime.now().strftime("%d/%m/%Y")
    txt = f"Para: {PARA}\nDe: {DE}\nFecha: {now}"
    box_text(txt, color=YELLOW)

# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    enable_windows_ansi()
    clear()

    line()
    typewriter(center("✨ DEDICATORIA ESPECIAL ✨"), delay=0.01, color=PINK, bold=True)
    line()

    print()
    signature()
    print()

    typewriter(center("Respira hondo... esto es para ti 💖"), delay=0.02, color=CYAN)
    time.sleep(1)
    countdown()
    clear()

    line("─", color=PINK)
    typewriter(center(f"Hola, {PARA}"), delay=0.05, color=YELLOW, bold=True)
    line("─", color=PINK)
    print()

    for frase in FRASES:
        typewriter("  " + frase, delay=0.035, color=WHITE)
        time.sleep(0.5)

    print("\n")
    box_text(MENSAJE_FINAL, color=MAGENTA)
    print()

    typewriter(center("Un pequeño cielo de corazones para ti..."), delay=0.02, color=CYAN)
    hearts_rain(frames=18, delay=0.07)

    print()
    typewriter(center("Gracias por leer esta dedicatoria 💫"), delay=0.02, color=YELLOW, bold=True)
    typewriter(center(f"Con cariño, {DE}"), delay=0.03, color=PINK)

if __name__ == "__main__":
    main()
