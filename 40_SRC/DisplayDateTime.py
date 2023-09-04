"""
    USE:
        Display a small window with date and time.

    INSTALLATION :
        None

"""

"""
    IMPORT SECTION
"""
import tkinter as tk            # Graphic windows
import tkinter.font             # Fonts management
from datetime import datetime   # Date and time
import pyautogui                # Mouse position



"""
    GLOBAL CONSTANTS
"""
# SECTION
    # Colors
BACKGD_COLOR = "black"


"""
    GLOBAL VARIABLES
"""
# Mouse-button 1 status
global is_pressed



"""
    FUNCTIONS DEFINITION
"""
# main function
def main():
    global is_pressed, origin_x, origin_y
    is_pressed = False

    print("Début du programme")

    # Define the window
    window = tk.Tk()
    window.title("Date / Time")
    # Does not display the title bar
    window.overrideredirect(True)
    # Set the window always on top
    window.wm_attributes("-topmost", True)

    # Define the labels
    time_label = tk.Label(window, text="Time", font=("DSEG7 Classic", 9))
    date_label = tk.Label(window, text="Date", font=("DSEG7 Classic", 8))

    # Set the font for the labels
    time_label.config(foreground="white")
    date_label.config(foreground="#A0A0A0")

    # Set the background color of the window
    time_label.config(bg=BACKGD_COLOR)
    date_label.config(bg=BACKGD_COLOR)
    window.configure(background=BACKGD_COLOR)

    # Set the location of the labels
    time_label.pack(side="top")
    date_label.pack(side="bottom")

    # DATE / TIME
    # Update the date and time labels every second
    time_label.config(text=datetime.now().strftime("%H:%M"))
    def update_labels():
        now = datetime.now()
        date_label.config(text=now.strftime("%d . %m . %Y"))

        # Make the colon flash
        text_label = time_label.cget("text")
        if ':' in text_label:
            time_label.config(text=now.strftime("%H %M"))
        else:
            time_label.config(text=now.strftime("%H:%M"))

        window.after(1000, update_labels)


    # WINDOW MOVEMENT
    # Move the window according to the mouse click & move
        # Register button press/release
    def press_button(event):
        global is_pressed
        is_pressed = True
    
    def release_button(event):
        global is_pressed
        is_pressed = False

        # Move the window if needed
    def move_window(event):
        # Get the coordinates of the mouse pointer
        x, y = pyautogui.position()
        # Move the window to the new coordinates
        if is_pressed:
            window.pack_propagate(False)
            window.geometry("+{}+{}".format(x, y))
            print(pyautogui.position())
            window.update()

    # Handle the Button-1 events
    window.bind("<Button-1>", press_button)
    window.bind("<ButtonRelease-1>", release_button)
    # Handle the mouse movements
    window.bind("<Motion>", move_window)

    # Start the update loop
    update_labels()
    window.mainloop()

# end main function


# Call to main() function when launching the program:
if __name__ == "__main__":
    main()

# end of file
