import pyautogui
import keyboard
from pynput.mouse import Listener
import time

# Lista per memorizzare i due punti cliccati
click_positions = []
clicks = 2 # clicks ciclici di default, cambia questa variabile se vuoi più clicks per ogni ciclo
# Funzione per registrare i clic
def on_click(x, y, button, pressed):
    if pressed and len(click_positions) < 3:  # Se si sono registrati meno di due clic
        click_positions.append((x, y))  # Aggiungi le coordinate del clic
        print(f"Clic registrato a ({x}, {y})")

        # Se sono stati registrati entrambi i clic, stampa un messaggio e ferma il listener
        if len(click_positions) == 3:
            print("Entrambi i clic registrati. Lo script simulerà i clic a ripetizione.")
            return False  # Ferma il listen

# Funzione per simulare i clic a ripetizione
def simulate_clicks():
    print("Simulazione dei clic in corso. Premi 'a' per fermare.")
    try:
        while True:
            # Controlla se il tasto 'a' è stato premuto per uscire
            if keyboard.is_pressed('a'):
                print("Tasto 'a' premuto. Uscita dalla simulazione.")
                break

            # Simula il clic sui due punti registrati
            for pos in click_positions:
                pyautogui.click(pos)  # Clicca sul punto
                time.sleep(1)  # Pausa breve tra i clic

    except KeyboardInterrupt:
        print("Interrotto manualmente.")

# Avvia la registrazione dei clic
time.sleep(3)
print("Clicca due volte per registrare i punti. Poi lo script simulerà i clic.")
with Listener(on_click=on_click) as listener:
    listener.join()
time.sleep(3)
# Una volta registrati i clic, avvia la simulazione
simulate_clicks()

print("Script terminato.")