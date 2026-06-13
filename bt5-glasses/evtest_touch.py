import evdev
import threading

# Replace 'X' with your specific event number (e.g., /dev/input/event0)
# You can find your device by running 'cat /proc/bus/input/devices'
DEVICE_PATH = '/dev/input/event25' 

def listen_for_bt_touch():
    try:
        device = evdev.InputDevice(DEVICE_PATH)
        print(f"Listening for events on {DEVICE_PATH}...")
        
        for event in device.read_loop():
            # Filter for key press events
            if event.type == evdev.ecodes.EV_KEY:
                data = evdev.categorize(event)
                
                # event.value == 1 means key down (pressed), 0 is key up (released)
                if data.keystate == data.key_down:
                    print(f"Touch/Key Pressed: {data.keycode}")
                    
                    # Add your custom touch action handling here
                    if 'PLAY' in data.keycode or 'PAUSE' in data.keycode:
                        print("Play/Pause action detected!")

    except FileNotFoundError:
        print(f"Device not found at {DEVICE_PATH}. Check your connection.")

# Run the listener in a background thread to prevent blocking your main application
touch_thread = threading.Thread(target=listen_for_bt_touch, daemon=True)
touch_thread.start()

# Keep main script running
try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped listening.")
