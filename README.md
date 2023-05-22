# Rapid-Gcode
Change feedrate for .gcode files using your retraction settings. 
99% made by ChatGPT, so if you know Python and want to help make this a better script im all ears.
This is mostly a personal project for a Lowrider 3 CNC running Klipper. 
This is to combat Fusion 360's limited rapid feed for personal use accounts. 

Download "RapidGcode-OctoUpload" folder if you want to use Octo-Upload. (The Post-Processor does support this too, but it would upload the "slow travel" version directly from Fusion) 
or
Download "RapidGcode" folder if you dont want Octo-Upload.

1. Download the folder of your choice. 
2. Read the "How-to.txt" file in the folder to set-up correctly. 
3. After that is done continue to step 4.
------------------------------------------------------------------
------------------------------------------------------------------
4. Run "RapidGcode.py", it will auto read the newest .gcode file in the folder where the script is located. 
5. Press "Enter" after reading the warning. (Dont blame me if you crash)
6. Type in your Z retraction that you used in Fusion 360, (5, 10, 15, 20, etc) 
7. Type in your desired feedrate for safe travel. 
8. Scrip will then do its thing and output a new .gcode file called ("WhatEverYounNamedItWhenPosting"_Z15_F4000.gcode) if you had a retraction of 15 and a new safe travel of 4000.
9. Check either ("WhatEverYounNamedItWhenPosting"_Z15_F4000.gcode) or ("WhatEverYounNamedItWhenPosting"Change_log_Z15_F4000.txt) to see if everything is OK. 
10. Send it to your CNC as you would normally do if it looks fine. 
11. Thats it, dont crash, be safe. You can make some test paths in Fusion and run it throug the script and "dry-run" the new file for testing. 

Here is how the actual Gcode looks after the scripts edit. (all F values was set to F300 in fusion, cause of the limitations where Fusion sets cutting speed to rapid travel on "free" accounts)

Original (slow travel)    ->  Modified (fast travel)
1.  G1 X100 Y0 Z15 F300   ->  G1 X100 Y0 Z15 F4000
2.  G1 Z-15 F300          ->  G1 Z-15 F300
3.  G1 Z15 F300           ->  G1 Z15 F4000
4.  G1 X300 Y0 F300       ->  G1 X300 Y0 F4000
5.  G1 Z-15 F300          ->  G1 Z-15 F300
6.  G1 Z15 F300           ->  G1 Z15 F4000
7.  G1 X300 Y300 F300     ->  G1 X300 Y300 F4000
8.  G1 Z-15 F300          ->  G1 Z-15 F300
9.  G1 Z15 F300           ->  G1 Z15 F4000
10. G1 X0 Y300 F300       ->  G1 X0 Y300 F4000
11. G1 Z-15 F300          ->  G1 Z-15 F300
12. G1 Z15 F300           ->  G1 Z15 F4000
13. G1 X0 Y0 F300         ->  G1 X0 Y0 F4000



This is taken from the change_log.txt it provides after editing to show only the lines that got changed

Original: G1 X100 Y0 Z15 F300            -> Modified: G1 X100 Y0 Z15 F4000          
Original: G1 Z15 F300                    -> Modified: G1 Z15 F4000                  
Original: G1 X300 Y0 F300                -> Modified: G1 X300 Y0 F4000              
Original: G1 Z15 F300                    -> Modified: G1 Z15 F4000                  
Original: G1 X300 Y300 F300              -> Modified: G1 X300 Y300 F4000            
Original: G1 Z15 F300                    -> Modified: G1 Z15 F4000                  
Original: G1 X0 Y300 F300                -> Modified: G1 X0 Y300 F4000              
Original: G1 Z15 F300                    -> Modified: G1 Z15 F4000                  
Original: G1 X0 Y0 F300                  -> Modified: G1 X0 Y0 F4000                
               
In this example we used 15 as the retraction on Z, so it changed the F value all the G1 lines with a Z value of 15 to F5000, and also changed the next line after a Z15 line to F5000 as long as that lines does not have a new Z value. This ensures that it will retract to Z15 fast, and the next "travel" command gets sped up.
It will never change a F value if Z is under 5. 
