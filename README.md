# Rapid-Gcode
Change feedrate for .gcode files using your retraction settings. 


This Python script modifies G-code files for CNC machining. It prompts the user to input the Z retraction distance used in Fusion360 and the new F(Rapid Feedrate) value. It then modifies the G-code file based on the specified parameters, replacing the feed rate value for specific lines and generating a new modified G-code file and a change log file.

This is to combat Fusion 360's limited rapid feed for personal use accounts. 

It simply ask you for your Z retraction from Fusion 360 and to set a feed value that you want to safe travel with.
It will auto read the newest .gcode file in the directory where you placed the .py file and output to the same folder. 
It will output a new .gcode file with your new travel feedrate. 


1. Download the .py file (make sure you have Python installed)
2. Put the .py file in your NC Program folder (or whatever folder you post process your Gcodes to)
3. Type in your Z retraction that you used in Fusion 360
4. Type in your chosen feedrate for safe travel. 
5. Check the folder where you place the .py file for new .gcode file and a change_log.txt (change log file will show you all the lines that got changed if you want to double check that its not setting a fast travelspeed for a Z-1 command. Even tho the script should never do that but better safe than sorry. 
6. Thats it

99% made by ChatGPT, so if you know Python and want to help make this a better script im all ears.
