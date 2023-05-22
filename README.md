# Rapid-Gcode
## Change feedrate for .gcode files using your retraction settings. 

**99% made by ChatGPT, so if you know Python and want to help make this a better script I'm all ears.  
This is mostly a personal project for a Lowrider 3 CNC running Klipper.   
This is to combat Fusion 360's limited rapid feed for personal use accounts.**   

I've used this myself for a few jobs now and so far it works fine, but i take **NO** responsibility if you crash.  
It might work for other DIY CNC machines running Marlin and a different post-processor etc as it only changes the F value, but this has not been tested. Should support any .gcode file. 

Download *"RapidGcode-OctoUpload"* folder if you want to use Octo-Upload. (The Post-Processor does support this too, but it would upload the "slow travel" version directly from Fusion)  
  
or  
  
Download *"RapidGcode"* folder if you don't want Octo-Upload.  
  
Both of these folders contain the post-processor used for a klipper based CNC (Credit to https://github.com/cristianku/mpcnc_config)

1. Download the folder of your choice. 
2. Read the "How-to.txt" file in the folder to set up correctly. 
3. After that is done, continue to step 4.
------------------------------------------------------------------
------------------------------------------------------------------
4. Run "GcodeRapidFeed.py" or "RapidGcode-OctoUpload", it will auto-read the newest .gcode file in the folder where the script is located. 
5. Press "Enter" after reading the warning.
6. Enter the IP to your CNC to set the IP for Octo-upload (only for "RapidGcode_OctoUpload.py")
7. Type in your Z retraction that you used in Fusion 360 (5, 10, 15, 20, etc). 
8. Type in your desired feedrate for safe travel. 
9. The script will then do its thing and output a new .gcode file called ("WhatEverYouNamedItWhenPosting"_Z15_F4000.gcode) if you had a retraction of 15 and a new safe travel of 4000.
10. Check either ("WhatEverYouNamedItWhenPosting"_Z15_F4000.gcode) or ("WhatEverYouNamedItWhenPosting"Change_log_Z15_F4000.txt) to see if everything is OK. 
11. Send it to your CNC as you would normally do if it looks fine. 
12. That's it, don't crash, be safe. You can make some test paths in Fusion and run it through the script and "dry-run" the new file for testing.  
  
If nothing changed in the .gcode and the change_log.txt is empty after running the script you might have entered the wrong retraction value and the script didnt find any lines to change.   

Here is how the actual G-code looks after the script's edit. (all F values were set to F300 in Fusion, cause of the limitations where Fusion sets cutting speed to rapid travel on "free" accounts)

Original (slow travel) |  Modified (fast travel)
-----------------------|----------------------
G1 X100 Y0 Z15 F300    |  G1 X100 Y0 Z15 F4000
G1 Z-15 F300           |  G1 Z-15 F300
G1 Z15 F300            |  G1 Z15 F4000
G1 X300 Y0 F300        |  G1 X300 Y0 F4000
G1 Z-15 F300           |  G1 Z-15 F300
G1 Z15 F300            |  G1 Z15 F4000
G1 X300 Y300 F300      |  G1 X300 Y300 F4000
G1 Z-15 F300           |  G1 Z-15 F300
G1 Z15 F300            |  G1 Z15 F4000
G1 X0 Y300 F300        |  G1 X0 Y300 F4000
G1 Z-15 F300           |  G1 Z-15 F300
G1 Z15 F300            |  G1 Z15 F4000
G1 X0 Y0 F300          |  G1 X0 Y0 F4000

This is taken from the change_log.txt it provides after editing to show only the lines that got changed  
Easier to check here since you dont have to check lines that didnt get changed. 

Original                                         | Modified
-------------------------------------------------|-----------------------------------
G1 X100 Y0 Z15 F300                              | G1 X100 Y0 Z15 F4000          
G1 Z15 F300                                      | G1 Z15 F4000                  
G1 X300 Y0 F300                                  | G1 X300 Y0 F4000              
G1 Z15 F300                                      | G1 Z15 F4000                  
G1 X300 Y300 F300                                | G1 X300 Y300 F4000            
G1 Z15 F300                                      | G1 Z15 F4000                  
G1 X0 Y300 F300                                  | G1 X0 Y300 F4000              
G1 Z15 F300                                      | G1 Z15 F4000                  
G1 X0 Y0 F300                                    | G1 X0 Y0 F4000                

In this example, we used 15 as the retraction on Z, so it changed the F value of all the G1 lines with a Z value of 15 to F4000 and also changed the next line after a Z15 line to F4000 as long as that line does not have a new Z value. This ensures that it will retract to Z15 fast, and the next "travel" command gets sped up. It will never change the F value of a line if Z is under 5.
