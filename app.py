# Installing the packages that are needed to create the environment
import pygame as pg
import tkinter as tk
from PIL import Image, ImageTk

# Initialize pygame library
pg.mixer.init()

# Code to create GUI window
root = tk.Tk()

# Title my GUI
root.title("NightWalk")

# Code to configurate the size of GUI
root.geometry("450x600")


# Definition to place my image on GUI
def add_image(root, file_path):
    # Specifying global variables for this to work
    global pic, f1

    # Frame for the first window of the game
    f1 = tk.Frame(root)

    # Image for the first frame
    img = Image.open(file_path)

    # Resizing the image
    img = img.resize((450, 600), Image.LANCZOS)

    # Code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def add_sos_button(root):
    sos_button = tk.Button(root, text="SOS", relief=tk.RAISED, bg='#4834DF', fg="red", font='hoeflertext 16 bold',
                           borderwidth=2,
                           command=go_to_sos_page)
    sos_button.place(x=200, y=550)

def go_to_sos_page():
    sospage()

# PAGE ONE
# Call add_image function with root variable file path
add_image(root, file_path="images/homepage_background.jpg")

welcome = tk.Label(root, text="Welcome to NightWalk!", font="hoeflertext 27 italic", fg="light pink")
welcome.place(x=85, y=50)

info = tk.Label(root, text="a place to connect with friends to feel safe...", font="hoeflertext 17 italic",
                fg="#B8CF9A")
info.place(x=60, y=95)

moreinfo = tk.Label(root, text="...no matter WHERE, no matter what TIME", font="hoeflertext 17 bold", fg="#B8CF9A")
moreinfo.place(x=60, y=122)


# To clear everything off of PAGE ONE
def secondpage():
    f1.destroy()
    enter_button.destroy()
    welcome.destroy();
    info.destroy();
    moreinfo.destroy()

    # PAGE TWO
    global next_button, personalinfo, main_number, main_number_box, main_name, main_name_box, main_age, main_age_box, main_handw, main_handw_box, main_features, main_features_box, main_address, main_address_box, main_addinfo, main_addinfo_box

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/contact_background.jpg")

    personalinfo = tk.Label(text="Tell us about yourself:", font="hoeflertext 20 bold", fg="light pink")
    personalinfo.place(x=115, y=50)

    infoone = tk.Label(text="This way we can forward your information in critical situations", font="hoeflertext 11",
                       fg="light pink")
    infoone.place(x=50, y=90)

    main_number = tk.Label(text="Phone Number:", font="hoeflertext 13 bold", fg="orange")
    main_number.place(x=20, y=150)

    input_main_number = tk.StringVar()
    main_number_box = tk.Entry(root, textvar=input_main_number, font="hoeflertext 10 bold", fg="black")
    main_number_box.place(x=155, y=150)

    main_name = tk.Label(text="Surname, Name:", font="hoeflertext 13 bold", fg="orange")
    main_name.place(x=20, y=200)

    input_main_name = tk.StringVar()
    main_name_box = tk.Entry(root, textvar=input_main_name, font="hoeflertext 10 bold", fg="black")
    main_name_box.place(x=155, y=200)

    main_age = tk.Label(text="Age:", font="hoeflertext 13 bold", fg="orange")
    main_age.place(x=20, y=250)

    input_main_age = tk.StringVar()
    main_age_box = tk.Entry(root, textvar=input_main_age, font="hoeflertext 10 bold", fg="black")
    main_age_box.place(x=155, y=250)

    main_handw = tk.Label(text="Height and Weight:", font="hoeflertext 13 bold", fg="orange")
    main_handw.place(x=20, y=300)

    input_main_handw = tk.StringVar()
    main_handw_box = tk.Entry(root, textvar=input_main_handw, font="hoeflertext 10 bold", fg="black")
    main_handw_box.place(x=155, y=300)

    main_features = tk.Label(text="Other recognizable features:", font="hoeflertext 13 bold", fg="orange")
    main_features.place(x=20, y=350)

    input_main_features = tk.StringVar()
    main_features_box = tk.Entry(root, textvar=input_main_features, font="hoeflertext 10 bold", fg="black")
    main_features_box.place(x=220, y=350)

    main_address = tk.Label(text="Address:", font="hoeflertext 13 bold", fg="orange")
    main_address.place(x=20, y=400)

    input_main_address = tk.StringVar()
    main_address_box = tk.Entry(root, textvar=input_main_address, font="hoeflertext 10 bold", fg="black")
    main_address_box.place(x=155, y=400)

    main_addinfo = tk.Label(text="(Optional) Additional Information:", font="hoeflertext 13 bold", fg="orange")
    main_addinfo.place(x=20, y=450)

    input_main_addinfo = tk.StringVar()
    main_addinfo_box = tk.Entry(root, textvar=input_main_addinfo, font="hoeflertext 10 bold", fg="black")
    main_addinfo_box.place(x=250, y=450)

    # From PAGE TWO add box, that will enter next page when the user clicks on it and clears the page to launch new page
    next_button = tk.Button(text="Next", relief=tk.RAISED, bg='#4834DF', fg="light pink", font='hoeflertext 16 bold',
                            borderwidth=2, command=thirdpage)
    next_button.place(x=200, y=500)

    add_sos_button(root)


# To clear everything off of PAGE TWO
def thirdpage():
    f1.destroy()
    personalinfo.destroy()
    main_number.destroy()
    main_number_box.destroy()
    main_name.destroy()
    main_name_box.destroy()
    main_age.destroy()
    main_age_box.destroy()
    main_handw.destroy()
    main_handw_box.destroy()
    main_features.destroy()
    main_features_box.destroy()
    main_address.destroy()
    main_address_box.destroy()
    main_addinfo.destroy()
    main_addinfo_box.destroy()
    next_button.destroy()

    # PAGE THREE
    global gettingstarted_button, emergencycontact, ec_one_number, ec_one_number_box, ec_one_name, ec_one_name_box, ec_two_number, ec_two_number_box, ec_two_name, ec_two_name_box, ec_three_number, ec_three_number_box, ec_three_name, ec_three_name_box

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/contact_background.jpg")

    emergencycontact = tk.Label(text="Appoint your emergency contact(s):", font="hoeflertext 20 bold", fg="light pink")
    emergencycontact.place(x=55, y=50)

    infotwo = tk.Label(text="We will contact them in case of emergency", font="hoeflertext 10", fg="light pink")
    infotwo.place(x=120, y=90)

    ec_one_number = tk.Label(text="Friend #1 Phone Number:", font="hoeflertext 13 bold", fg="red")
    ec_one_number.place(x=20, y=150)

    input_ec_one_number = tk.StringVar()
    ec_one_number_box = tk.Entry(root, textvar=input_ec_one_number, font="hoeflertext 10 bold", fg="black")
    ec_one_number_box.place(x=200, y=150)

    ec_one_name = tk.Label(text="Friend #1 Surname, Name:", font="hoeflertext 13 bold", fg="red")
    ec_one_name.place(x=20, y=200)

    input_ec_one_name = tk.StringVar()
    ec_one_name_box = tk.Entry(root, textvar=input_ec_one_name, font="hoeflertext 10 bold", fg="black")
    ec_one_name_box.place(x=200, y=200)

    ec_two_number = tk.Label(text="Friend #2 Phone Number:", font="hoeflertext 13 bold", fg="orange")
    ec_two_number.place(x=20, y=250)

    input_ec_number = tk.StringVar()
    ec_two_number_box = tk.Entry(root, textvar=input_ec_number, font="hoeflertext 10 bold", fg="black")
    ec_two_number_box.place(x=200, y=250)

    ec_two_name = tk.Label(text="Friend #2 Surname, Name:", font="hoeflertext 13 bold", fg="orange")
    ec_two_name.place(x=20, y=300)

    input_ec_two_name = tk.StringVar()
    ec_two_name_box = tk.Entry(root, textvar=input_ec_two_name, font="hoeflertext 10 bold", fg="black")
    ec_two_name_box.place(x=200, y=300)

    ec_three_number = tk.Label(text="Friend #3 Phone Number:", font="hoeflertext 13 bold", fg="#E6CF00")
    ec_three_number.place(x=20, y=350)

    input_ec_number = tk.StringVar()
    ec_three_number_box = tk.Entry(root, textvar=input_ec_number, font="hoeflertext 10 bold", fg="black")
    ec_three_number_box.place(x=200, y=350)

    ec_three_name = tk.Label(text="Friend #3 Surname, Name:", font="hoeflertext 13 bold", fg="#E6CF00")
    ec_three_name.place(x=20, y=400)

    input_ec_three_name = tk.StringVar()
    ec_three_name_box = tk.Entry(root, textvar=input_ec_three_name, font="hoeflertext 10 bold", fg="black")
    ec_three_name_box.place(x=200, y=400)

    # From PAGE THREE add box, that will enter next page when the user clicks on it and clears the page to launch new page
    gettingstarted_button = tk.Button(text="Your Options", relief=tk.RAISED, bg='#4834DF', fg="light pink",
                                      font='hoeflertext 16 bold',
                                      borderwidth=2, command=fourthpage)
    gettingstarted_button.place(x=165, y=500)

    add_sos_button(root)


# To clear everything off of PAGE THREE
def fourthpage():
    f1.destroy()

    # PAGE FOUR
    global followingoptions, SOS_button, OMW_button, voice_button, tel_button, chat_button

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/action_background.jpg")

    # Label to specify the following options
    followingoptions = tk.Label(text="Take Action:", font="hoeflertext 20 bold", fg="light pink")
    followingoptions.place(x=160, y=50)

    # SOS button to contact police
    SOS_button = tk.Button(text="SOS", relief=tk.RAISED, bg='#4834DF', fg="red",
                           font='hoeflertext 16 bold',
                           borderwidth=2, command=sospage)
    SOS_button.place(x=185, y=550)

    # "I am on my way home NOW" button to text to friends (emergency contact(s))
    OMW_button = tk.Button(text="I am on my way home NOW", relief=tk.RAISED, bg='#4834DF', fg="#B8CF9A",
                           font='hoeflertext 16 bold',
                           borderwidth=2, command=omwpage)
    OMW_button.place(x=102, y=150)

    # Record a voice message button to be sent to contacts
    voice_button = tk.Button(text="Record a voice message…", relief=tk.RAISED, bg='#4834DF', fg="light blue",
                             font='hoeflertext 16 bold',
                             borderwidth=2, command=voicepage)
    voice_button.place(x=100, y=250)

    # Heimwegtelefon button to call them
    tel_button = tk.Button(text="Call Heimwegtelefon", relief=tk.RAISED, bg='#4834DF', fg="orange",
                           font='hoeflertext 16 bold',
                           borderwidth=2, command=telpage)
    tel_button.place(x=120, y=450)

    # Chatbot Button to contact support line or AI
    chat_button = tk.Button(text="Chatbot", relief=tk.RAISED, bg='#4834DF', fg="purple",
                            font='hoeflertext 16 bold',
                            borderwidth=2, command=chatpage)
    chat_button.place(x=170, y=350)


# PAGES that you are led to when pushing one of the buttons
def sospage():
    f1.destroy()

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/911_background.jpg")

    def play_music():
        # Play some music
        pg.mixer.music.load("music/911-ringing.mp3")
        pg.mixer.music.play()

    # Call the play_music function to start playing the music
    play_music()

    global calling, backtooption

    calling = tk.Label(text="Please stay on the line", font="hoeflertext 15", fg="white", bg="red")
    calling.place(x=140, y=130)

    # Button to go back to the second page
    backtooption = tk.Button(text="<- Back", font="hoeflertext 10 bold", fg="light blue",
                             command=backtooption)
    backtooption.place(x=15, y=5)

def backtooption():
    calling.destroy()
    backtooption.destroy()

    fourthpage()

def omwpage():
    f1.destroy()
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()
    chat_button.destroy()

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/omw_background.jpg")

    global message, messagetwo, messagethree, backtooptiontwo

    message = tk.Label(text="Now sharing location with emergency contact(s)!", font="hoeflertext 11", fg="black",
                       bg="#B8CF9A")
    message.place(x=160, y=250)

    messagetwo = tk.Label(text="I am on my way home NOW.", font="hoeflertext 18", fg="black", bg="#B8CF9A")
    messagetwo.place(x=120, y=325)

    messagethree = tk.Label(text="Sent to you emergency contact(s)!", font="hoeflertext 10 italic", fg="black",
                            bg="#B8CF9A")
    messagethree.place(x=140, y=400)

    # Button to go back to the second page
    backtooptiontwo = tk.Button(text="<- Back ", font="hoeflertext 10 bold", fg="light blue",
                                command=backtooptiontwo)
    backtooptiontwo.place(x=15, y=5)


def backtooptiontwo():
    message.destroy()
    messagetwo.destroy()
    messagethree.destroy()
    backtooptiontwo.destroy()

    fourthpage()

def voicepage():
    f1.destroy()
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()
    chat_button.destroy()

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/voicemessage_background.jpg")

    global voicemessage, voicemessage_info, backtooptionthree

    voicemessage = tk.Label(text="You can NOW record a voice message", font="hoeflertext 16 italic", fg="black",
                            bg="light blue")
    voicemessage.place(x=110, y=200)

    voicemessage_info = tk.Label(text="Automatically sent to emergency contact(s) if limit of 45mins is reached!",
                                 font="hoeflertext 10 italic", fg="black", bg="light blue")
    voicemessage_info.place(x=50, y=370)

    # Button to go back to the second page
    backtooptionthree = tk.Button(text="<- Back", font="hoeflertext 10 bold", fg="light blue",
                                  command=backtooptionthree)
    backtooptionthree.place(x=15, y=5)

def backtooptionthree():
    voicemessage.destroy()
    voicemessage_info.destroy()
    backtooptionthree.destroy()

    fourthpage()

def telpage():
    f1.destroy()
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()
    chat_button.destroy()

    # Add new image as background for PAGE TWO
    add_image(root, file_path="images/Heimwegtelefon_background.jpg")

    def play_music():
        # Play some music
        pg.mixer.music.load("music/phone-outgoing-call.mp3")
        pg.mixer.music.play()

    # Call the play_music function to start playing the music
    play_music()

    global backtooptionfour, telefon

    telefon = tk.Label(text="Please stay on the line", font="hoeflertext 15", fg="white", bg="orange")
    telefon.place(x=140, y=130)

    # Button to go back to the second page
    backtooptionfour = tk.Button(text="<- Back", font="hoeflertext 10 bold", fg="light blue",
                                 command=backtooptionfour)
    backtooptionfour.place(x=10, y=5)

def backtooptionfour():
    telefon.destroy()
    backtooptionfour.destroy()

    fourthpage()


def chatpage():
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()
    chat_button.destroy()

    global chat, backtooptionfive
    # Create variables to format
    bg_colour = "#A683AF"
    text_colour = "#F6F4ED"
    font = "Helvetica 14"
    font_bold = "Helvetica 13 bold"

    # To be able to send something to the Bot
    def send():
        user_message = entry_box.get()

        if user_message:
            text_box.insert(tk.END, f"\nUser: {user_message}")
            if (user_message == "Yes"):
                text_box.insert(tk.END,
                                f"\n" + "Bot: 911 has been notified and given your location and personal information!")
                text_box.insert(tk.END, f"\nBot: Don't worry! Help is on the way!")

            elif (user_message == "yes"):
                text_box.insert(tk.END,
                                f"\n" + "Bot: 911 has been notified and given your location and personal information!")
                text_box.insert(tk.END, f"\nBot: Don't worry! Help is on the way!")

            elif (user_message == "No"):
                text_box.insert(tk.END,
                                f"\n" + "Bot: Do you want to speak to your Emergency Contacts(1) or Heimwegtelefon(2)?")
                text_box.insert(tk.END, f"\nBot: Please choose an option")

            elif (user_message == "no"):
                text_box.insert(tk.END,
                                f"\n" + "Bot: Do you want to speak to your Emergency Contacts(1) or Heimwegtelefon(2)?")
                text_box.insert(tk.END, f"\nBot: Please choose an option")

            elif (user_message == "1"):
                text_box.insert(tk.END, f"\n" + "Bot: Calling your Number 1 emergency contact now.")

            elif (user_message == "2"):
                text_box.insert(tk.END, f"\n" + "Bot: Calling Heimwegtelefon now.")


            else:
                text_box.insert(tk.END, f"\nBot: I do not understand. Please check your spelling and try again!")

                entry_box.destroy()
                send_button.destroy()

        # Delete what was entered by user in entry box after sending
        entry_box.delete(0, tk.END)

    def create_chatbot():
        global entry_box, send_box, text_box, welcome_label, scroll_bar, send_button, backtooptionfour

    def backtooptionfive():
        # Destroy widgets associated with the chat page
        welcome_label.destroy()
        text_box.destroy()
        scroll_bar.destroy()
        entry_box.destroy()
        send_button.destroy()
        backtooptionfour.destroy()

        # Call the function to navigate to the previous page
        fourthpage()

    # Place a welcome label
    welcome_label = tk.Label(root,
                             text="I am here to help you",
                             bg=bg_colour,
                             fg=text_colour,
                             font=font_bold,
                             # pady=10,
                             width=30,
                             height=1)

    welcome_label.place(relx=0.5,
                        y=17,
                        anchor=tk.CENTER)  # place in center

    # Create the text box
    text_box = tk.Text(root,
                       bg=bg_colour,
                       fg=text_colour,
                       font=font,
                       width=60)
    text_box.place(x=0, y=30, relwidth=1, relheight=1)  
    # Add some text that introduces the chatbot
    text_box.insert(tk.END, "Bot: Hello, are you in danger? Send Yes or No.")

    # Create a scrollbar for the textbox
    # Relx and Rely is relative position
    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1,
                     relx=0.974)

    # Create an entry box for user to enter message
    entry_box = tk.Entry(root,
                         bg="#2C3E50",
                         fg=text_colour,
                         font=font,
                         width=55
                         )
    entry_box.place(x=5,
                    rely=0.925)

    send_button = tk.Button(root,
                            text="Send",
                            font=font_bold,
                            bg="#ABB2B9",
                            # command=send to make sure my message is sending to the Bot
                            command=send,
                            width=10)
    send_button.place(relx=0.77,
                      rely=0.925
                      )

    # Button to go back to the second page
    backtooptionfour = tk.Button(text="<- Back", font="hoeflertext 10 bold", fg="light blue",
                                 command=backtooptionfive)
    backtooptionfour.place(x=10, y=5)


# BUTTONS
# From PAGE ONE add box, that will enter next page when the user clicks on it and clear the page to launch new page
enter_button = tk.Button(text="Let's feel safe together", relief=tk.RAISED, bg='#4834DF', fg="light pink",
                         font='hoeflertext 16 bold', borderwidth=2, command=secondpage)
enter_button.place(x=120, y=500)

# Code to execute the code
root.mainloop()
