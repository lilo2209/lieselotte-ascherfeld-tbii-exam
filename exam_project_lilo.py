#installing the packages that are needed to create environment
import tkinter as tk
from PIL import Image, ImageTk

#code to create GUI window
root = tk.Tk()

#title my GUI
root.title("NightWalk")

#code to configurate the size of GUI, using these sizes for portrait format (of an app)
root.geometry("450x600")

#definition to place my image on GUI
def add_image(root, file_path):

    #specifying global variables for this to work
    global pic, f1

    #frame for the first window of the game
    f1 = tk.Frame(root)

    #image for the first frame
    img = Image.open(file_path)

    #resizing the image
    img = img.resize((450, 600), Image.LANCZOS)

    #code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

#PAGE ONE
#call add_image function with root variable file path
add_image(root, file_path="images/img_street_map.jpg")

#label to welcome user
welcome = tk.Label(root, text="Welcome to NightWalk!", font="hoeflertext 25 italic", fg = "light pink")
welcome.place(x=95, y=50)

#label to add information
info = tk.Label(root, text="a place to connect with friends to feel safe...", font="hoeflertext 15 italic", fg = "light blue")
info.place(x=81, y=95)

#another label to add information
moreinfo = tk.Label(root, text="...no matter WHERE, no matter what TIME", font="hoeflertext 15 bold", fg = "light blue")
moreinfo.place(x=81, y=122)


#to clear everything off of PAGE ONE
def secondpage():
    #destroy all created on PAGE ONE
    f1.destroy()
    enter_button.destroy()
    welcome.destroy();
    info.destroy();
    moreinfo.destroy();

#PAGE TWO
    # specifying global variables for this to work
    global next_button, personalinfo, main_number, main_number_box, main_name, main_name_box, main_age, main_age_box, main_handw, main_handw_box, main_features, main_features_box, main_address, main_address_box, main_addinfo, main_addinfo_box

    #add new image as background for PAGE TWO
    add_image(root, file_path="images/avatar.jpg")

    #label for personal information
    personalinfo = tk.Label(text="Tell us about yourself:", font="hoeflertext 20 bold", fg="light blue")
    personalinfo.place(x=115, y=50)

    #label to ask for phone number
    main_number = tk.Label(text="Phone Number:", font="hoeflertext 13 italic", fg="orange")
    main_number.place(x=20, y=150)

    #create a box where user can type their phone number and save input
    input_main_number = tk.StringVar()
    main_number_box = tk.Entry(root, textvar=input_main_number, font="hoeflertext 10 bold", fg="black")
    main_number_box.place(x=155, y=150)

    #label to ask for name and surname
    main_name = tk.Label(text="Surname, Name:", font="hoeflertext 13 italic", fg="orange")
    main_name.place(x=20, y=200)

    #create a box where user can type their name and surname and save input
    input_main_name = tk.StringVar()
    main_name_box = tk.Entry(root, textvar=input_main_name, font="hoeflertext 10 bold", fg="black")
    main_name_box.place(x=155, y=200)

    #label to ask for age
    main_age = tk.Label(text="Age:", font="hoeflertext 13 italic", fg="orange")
    main_age.place(x=20, y=250)

    #create a box where user can type their age
    input_main_age = tk.StringVar()
    main_age_box = tk.Entry(root, textvar=input_main_age, font="hoeflertext 10 bold", fg="black")
    main_age_box.place(x=155, y=250)

    #label to ask for height and weight
    main_handw = tk.Label(text="Height and Weight:", font="hoeflertext 13 italic", fg="orange")
    main_handw.place(x=20, y=300)

    #create a box where user can type their height and weight
    input_main_handw = tk.StringVar()
    main_handw_box = tk.Entry(root, textvar=input_main_handw, font="hoeflertext 10 bold", fg="black")
    main_handw_box.place(x=155, y=300)

    #label to ask for other easily recognizable features
    main_features = tk.Label(text="Other recognizable features:", font="hoeflertext 13 italic", fg="orange")
    main_features.place(x=20, y=350)

    #create a box where user can type other recognizable features
    input_main_features = tk.StringVar()
    main_features_box = tk.Entry(root, textvar=input_main_features, font="hoeflertext 10 bold", fg="black")
    main_features_box.place(x=220, y=350)

    #label to ask for address
    main_address = tk.Label(text="Address:", font="hoeflertext 13 italic", fg="orange")
    main_address.place(x=20, y=400)

    #create a box where user can type their address
    input_main_address = tk.StringVar()
    main_address_box = tk.Entry(root, textvar=input_main_address, font="hoeflertext 10 bold", fg="black")
    main_address_box.place(x=155, y=400)

    #optional label to type additional information
    main_addinfo = tk.Label(text="(Optional) Additional Information:", font="hoeflertext 13 italic", fg="orange")
    main_addinfo.place(x=20, y=450)

    #create a box where user can type additional information
    input_main_addinfo = tk.StringVar()
    main_addinfo_box = tk.Entry(root, textvar=input_main_addinfo, font="hoeflertext 10 bold", fg="black")
    main_addinfo_box.place(x=250, y=450)

    #from PAGE TWO add box, that will enter next page when the user clicks on it and clears the page to launch new page
    next_button = tk.Button(text="Next", relief=tk.RAISED, bg='#4834DF', fg="light blue", font='hoeflertext 16 bold',
                            borderwidth=2, command=thirdpage)
    next_button.place(x=200, y=500)

#to clear everything off of PAGE TWO
def thirdpage():
    #destroy all created on PAGE TWO
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


#PAGE THREE
    # specifying global variables for this to work
    global gettingstarted_button, emergencycontact, ec_one_number, ec_one_number_box, ec_one_name, ec_one_name_box, ec_two_number, ec_two_number_box, ec_two_name, ec_two_name_box, ec_three_number, ec_three_number_box, ec_three_name, ec_three_name_box

    #add new image as background for PAGE TWO
    add_image(root, file_path="images/friends.jpg")

    #label for emergency contacs
    emergencycontact = tk.Label(text="Appoint your emergency contact(s):", font="hoeflertext 20 bold", fg="light blue")
    emergencycontact.place(x=55, y=50)

    #label to ask for emergency 1's phone number
    ec_one_number = tk.Label(text="Friend #1 Phone Number:", font="hoeflertext 13 italic", fg="red")
    ec_one_number.place(x=20, y=150)

    #create a box where user can type emergency 1's phone number and save input
    input_ec_one_number = tk.StringVar()
    ec_one_number_box = tk.Entry(root, textvar=input_ec_one_number, font="hoeflertext 10 bold", fg="black")
    ec_one_number_box.place(x=200, y=150)

    #label to ask for emergency 1's name and surname
    ec_one_name = tk.Label(text="Friend #1 Surname, Name:", font="hoeflertext 13 italic", fg="red")
    ec_one_name.place(x=20, y=200)

    #create a box where user can type emergency 1's name and surname and save input
    input_ec_one_name = tk.StringVar()
    ec_one_name_box = tk.Entry(root, textvar=input_ec_one_name, font="hoeflertext 10 bold", fg="black")
    ec_one_name_box.place(x=200, y=200)


    #label to ask for emergency 2's phone number
    ec_two_number = tk.Label(text="Friend #2 Phone Number:", font="hoeflertext 13 italic", fg="orange")
    ec_two_number.place(x=20, y=250)

    #create a box where user can type emergency 2's phone number and save input
    input_ec_number = tk.StringVar()
    ec_two_number_box = tk.Entry(root, textvar=input_ec_number, font="hoeflertext 10 bold", fg="black")
    ec_two_number_box.place(x=200, y=250)

    #label to ask for emergency 2's name and surname
    ec_two_name = tk.Label(text="Friend #2 Surname, Name:", font="hoeflertext 13 italic", fg="orange")
    ec_two_name.place(x=20, y=300)

    #create a box where user can type emergency 2's name and surname and save input
    input_ec_two_name = tk.StringVar()
    ec_two_name_box = tk.Entry(root, textvar=input_ec_two_name, font="hoeflertext 10 bold", fg="black")
    ec_two_name_box.place(x=200, y=300)

    #label to ask for emergency 3's phone number
    ec_three_number = tk.Label(text="Friend #3 Phone Number:", font="hoeflertext 13 italic", fg="yellow")
    ec_three_number.place(x=20, y=350)

    #create a box where user can type emergency 3's phone number and save input
    input_ec_number = tk.StringVar()
    ec_three_number_box = tk.Entry(root, textvar=input_ec_number, font="hoeflertext 10 bold", fg="black")
    ec_three_number_box.place(x=200, y=350)

    #label to ask for emergency 3's name and surname
    ec_three_name = tk.Label(text="Friend #3 Surname, Name:", font="hoeflertext 13 italic", fg="yellow")
    ec_three_name.place(x=20, y=400)

    #create a box where user can type emergency 3's name and surname and save input
    input_ec_three_name = tk.StringVar()
    ec_three_name_box = tk.Entry(root, textvar=input_ec_three_name, font="hoeflertext 10 bold", fg="black")
    ec_three_name_box.place(x=200, y=400)

    #from PAGE THREE add box, that will enter next page when the user clicks on it and clears the page to launch new page
    gettingstarted_button = tk.Button(text="Your Options", relief=tk.RAISED, bg='#4834DF', fg="light pink", font='hoeflertext 16 bold',
                            borderwidth=2, command=fourthpage)
    gettingstarted_button.place(x=150, y=500)

#to clear everything off of PAGE THREE
def fourthpage():
    #destroy all created on PAGE THREE
    f1.destroy()
    emergencycontact.destroy()
    ec_one_number.destroy()
    ec_one_number_box.destroy()
    ec_one_name.destroy()
    ec_one_name_box.destroy()
    ec_two_number.destroy()
    ec_two_number_box.destroy()
    ec_two_name.destroy()
    ec_two_name_box.destroy()
    ec_three_number.destroy()
    ec_three_number_box.destroy()
    ec_three_name.destroy()
    ec_three_name_box.destroy()
    gettingstarted_button.destroy()

#PAGE FOUR
    #specifying global variables for this to work
    global followingoptions, SOS_button, OMW_button, voice_button, tel_button

    #add new image as background for PAGE TWO
    add_image(root, file_path="images/location.jpg")

    #label to specify the following options
    followingoptions = tk.Label(text="Take Action:", font="hoeflertext 20 bold", fg="black")
    followingoptions.place(x=160, y=50)

    #SOS button to contact police
    SOS_button = tk.Button(text="SOS", relief=tk.RAISED, bg='#4834DF', fg="red",
                                      font='hoeflertext 16 bold',
                                      borderwidth=2, command=sospage)
    SOS_button.place(x=190, y=120)

    #"I am on my way home NOW" button to text to friends (emergency contact(s))
    OMW_button = tk.Button(text="I am on my way home NOW", relief=tk.RAISED, bg='#4834DF', fg="light pink",
                           font='hoeflertext 16 bold',
                           borderwidth=2, command=omwpage)
    OMW_button.place(x=102, y=240)

    #Record a voice message button to be sent to contacts
    voice_button = tk.Button(text="Record a voice message…", relief=tk.RAISED, bg='#4834DF', fg="light blue",
                           font='hoeflertext 16 bold',
                           borderwidth=2, command=voicepage)
    voice_button.place(x=102, y=360)

    #Heimwegtelefon button to call them
    tel_button = tk.Button(text="Call Heimwegtelefon", relief=tk.RAISED, bg='#4834DF', fg="orange", font='hoeflertext 16 bold', borderwidth=2, command=telpage)
    tel_button.place(x=120, y=480)

#PAGES that you are led to when pushing one of the buttons
def sospage():
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()

    global calling, backtooption

    calling = tk.Label(text="Calling 911 NOW", font="hoeflertext 15 italic", fg="black")
    calling.place(x=30, y=130)

    #Button to go back to the second page
    backtooption = tk.Button(text="Back to Option page…",font="hoeflertext 10 bold", fg="light blue",
                       command=backtooption)
    backtooption.place(x=30, y=200)

def backtooption():

    calling.destroy()
    backtooption.destroy()

    fourthpage()

def omwpage():
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()

    global message, messagetwo, backtooptiontwo

    message = tk.Label(text="You are now sharing your location with your emergency contact(s)!", font="hoeflertext 10 italic", fg="black")
    message.place(x=30, y=130)

    messagetwo = tk.Label(text="A text has been sent to your emergency contact(s)!",font="hoeflertext 10 italic", fg="black")
    messagetwo.place(x=30, y=200)

    #Button to go back to the second page
    backtooptiontwo = tk.Button(text="Back to Option page…",font="hoeflertext 10 bold", fg="light blue",
                       command=backtooptiontwo)
    backtooptiontwo.place(x=30, y=300)

def backtooptiontwo():

    message.destroy()
    messagetwo.destroy()
    backtooptiontwo.destroy()

    fourthpage()
def voicepage():
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()

    global voicemessage, voicemessage_info, backtooptionthree

    voicemessage = tk.Label(text="You can now record a voice message to be sent to your emergency contact(s)!", font="hoeflertext 10 italic", fg="black")
    voicemessage.place(x=30, y=130)

    voicemessage_info = tk.Label(text="It will automatically be sent to emergency contact(s) if it expands the limit of 45mins!", font="hoeflertext 10 italic", fg="black")
    voicemessage_info.place(x=30, y=200)

    #Button to go back to the second page
    backtooptionthree = tk.Button(text="Back to Option page…",font="hoeflertext 10 bold", fg="light blue",
                       command=backtooptionthree)
    backtooptionthree.place(x=30, y=300)

def backtooptionthree():

    voicemessage.destroy()
    voicemessage_info.destroy()
    backtooptionthree.destroy()

    fourthpage()
def telpage():
    followingoptions.destroy()
    SOS_button.destroy()
    OMW_button.destroy()
    voice_button.destroy()
    tel_button.destroy()

    global telefon, backtooptionfour

    telefon = tk.Label(text="Calling Heimwegtelefon NOW",font="hoeflertext 15 italic", fg="black")
    telefon.place(x=30, y=130)

    #Button to go back to the second page
    backtooptionfour = tk.Button(text="Back to Option page…",font="hoeflertext 10 bold", fg="light blue",
                       command=backtooptionfour)
    backtooptionfour.place(x=30, y=200)

def backtooptionfour():

    telefon.destroy()
    backtooptionfour.destroy()

    fourthpage()

#BUTTONS
#from PAGE ONE add box, that will enter next page when the user clicks on it and clear the page to launch new page
enter_button = tk.Button(text="Let's feel safe together", relief=tk.RAISED, bg='#4834DF', fg = "light pink", font='hoeflertext 16 bold', borderwidth=2, command=secondpage)
enter_button.place(x=120, y=500)

#code to execute the code
root.mainloop()
