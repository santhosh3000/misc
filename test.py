# import pyautogui
# import time
# import random

# # This variable controls how far the mouse will move
# MOVE_DISTANCE = 50

# # This variable controls whether the loop should continue running
# KEEP_LOOPING = True

# # Set the pause time to a small value to allow the user to press the 'q' key
# pyautogui.PAUSE = 0.1

# while KEEP_LOOPING:
#     # Generate a random x and y offset
#     x_offset = random.randint(-MOVE_DISTANCE, MOVE_DISTANCE)
#     y_offset = random.randint(-MOVE_DISTANCE, MOVE_DISTANCE)

#     # Move the mouse by the specified offset
#     pyautogui.moveRel(x_offset, y_offset)

#     # Check if the user has pressed and released the 'q' key
#     if pyautogui.hotkey('q'):
#         # Set KEEP_LOOPING to False to stop the loop
#         KEEP_LOOPING = False

#     # Sleep for 1 minute before repeating the loop
#     time.sleep(1)




import time
import pyautogui

# move and click the mouse every 3 minutes
while True:
    try:
        # move the mouse slightly
        pyautogui.moveRel(1, 1, duration=0.25)

        # click the mouse
        pyautogui.click()

        # wait 3 minutes
        time.sleep(180)
    except KeyboardInterrupt:
        # break out of the loop on keyboard interrupt
        print("Exiting the script")
        break
