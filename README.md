# Alexa_TiVo_Control
Control your TiVo using an Amazon Echo &amp; a Raspberry Pi

Controlling you TiVo using an Amazon Echo & a Raspberry Pi is pretty easy to set up using this code.

Steps Required:
----------------------------------------------------------------------------------
1: Setup your TiVo to allow it to be controlled via a network connection
2: Download code on your raspberry pi (your pi need Python installed to run) 
3: Edit downloaded code (Your TV channel numbers will be different than the code)
4: Have Alexa discover new devices (so it learns what channels are programmed)

Step 1: TiVo Setup (TiVo HD Instructions).
----------------------------------------------------------------------------------
-Hit your TiVo Remote button and go to Messages & Settings
-Choose Settings
-Choose Remote, CableCard, & Devices
-Choose Network Remote Control
-Choose Enable
-Press Thumbs Up, Thumbs Up, Thumbs Up
-Your TiVo can now be controlled via TelNet commands over port 31339

Step 1: Tivo Setup (TiVo Bolt Instructions)
----------------------------------------------------------------------------------

Step 2: Download Code
----------------------------------------------------------------------------------

First verify that your Raspberry Pi is running Python. (This programming language is required to run our code.)
To do so, just type python on your pi...if Python is installed, the pi will show which version is installed. Hit Control+D to exit the Python infomation screen
next type the following
git clone https://github.com/shrocky2/Alexa_TiVo.git
this will download our code to a directory called "Alexa_TiVo" (minus the quotation marks), change to this directory
cd Alexa_TiVo
There are 2 files that you DON'T need to modify, "fauxmo.py" & "debounce_handler.py", so just forget they exist.


Step 3: Edit Code to match your channel situation
----------------------------------------------------------------------------------
There are 3 .py files that you can edit to personalize the TV channels that Alexa can change on the TiVo.
TiVo_List1.py & TiVo_List2.py are used to teach Alexa the TV Channels
These 2 files are needed because Alexa can only learn 12 new devices at a given time. (Alexa only searches for new 'devices' for 20 seconds, which is only enough time to learn 12 devices.) So if we run these 2 python programs seperately, we can teach Alexa 24 'devices')
to edit a programs enter the following: sudo nano TiVo_List1.py 
(hit Control + X to Save Changes)
Once you've edited TiVo_List1.py & TiVo_List2.py, we can move onto editing TiVo.py
Any Changes you made to TiVo_List1.py & TiVo_List2.py need to be copied into TiVo.py
TiVo.py is the real code that is used to actually change the TiVo Channels, 
----------------------------------------------------------------------------------
