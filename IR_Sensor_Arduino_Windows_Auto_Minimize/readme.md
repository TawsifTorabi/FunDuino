# Windows Auto Minimize
**Using IR Sensor Module, Arduino and a little help from python.**

It's a simple and fun project, the idea was whenever the sensor connected on the arduino board detects any obstacle and get triggered, all the windows open in our computer would minimize or Hide. 
As I'm using windows operating system, the shortcut key to hide all the windows and show the desktop is **"Start+,(comma)"** and after pressing we have to hold it.

So where does the idea makes sense? Just imagine you are 45 years old and watching Kid vs Kat on your computer. Your wife came in and found you giggling. So that's where that simple thing might help, or maybe not.

## To make the Python Script work...
We have to install some modules of python using pip and the python environment to run the script (makes sense)

To make sure you have python installed in your system, go to powerShell in windows and type "python" and press enter. If your system don't have python installed, It should take you to microsoft store to download python runtimes and environments. 
After installation, to make sure everything is okay, go to powershell again and type in "python", this time it should show you a message that python enviroment is active.
 
So after you make sure that you have python installed in your system, go to command or powershell and type in these comnmands one by one to install each of this python modules which are required to make our auto minimize script work.

    pip install pynput
    pip install pyserial
    pip install pyautogui

Now open your code editor (VS Code, Notepad++) or just classic old notepad if you don't have any.
After opening, paste the code  and save using a name with the extension naming .py
And then just run by double clicking on the script, or you can use the command line promt to run the script.
