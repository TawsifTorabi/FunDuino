# ESP32_NetworkMonitor
**Using Some Servos, LEDs, ESP32 and almost all the help from python.**

It's a simple and fun project, the idea is to get the realtime network usage data through a websocket using python and then pass the data to ESP32, after passing the data, we will parse and convert the data to be mapped to servo angles and LED levels. Then we should be able to see our netspeed meter on our table.

So where does the idea makes sense? Actually it doesn't. it just looks dope.

## To make the Python Script work...
We have to install some modules of python using pip and the python environment to run the script (makes sense)

To make sure you have python installed in your system, go to powerShell in windows and type "python" and press enter. If your system don't have python installed, It should take you to microsoft store to download python runtimes and environments. 
After installation, to make sure everything is okay, go to powershell again and type in "python", this time it should show you a message that python enviroment is active.
 
So after you make sure that you have python installed in your system, go to command or powershell and type in these comnmands one by one to install each of this python modules which are required to make our auto minimize script work.

  ```python
pip install psutil scapy pandas
```

Now open your code editor (VS Code, Notepad++) or just classic old notepad if you don't have any.
After opening, paste the code  and save using a name with the extension naming .py
And then just run by double clicking on the script, or you can use the command line promt to run the script.




 
