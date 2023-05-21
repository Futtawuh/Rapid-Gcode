import os

# Display warning message
warning_message = r"""
 __        __   _      ____    _   _   ___   _   _    ____ 
 \ \      / /  / \    |  _ \  | \ | | |_ _| | \ | |  / ___|
  \ \ /\ / /  / _ \   | |_) | |  \| |  | |  |  \| | | |  _ 
   \ V  V /  / ___ \  |  _ <  | |\  |  | |  | |\  | | |_| |
    \_/\_/  /_/   \_\ |_| \_\ |_| \_| |___| |_| \_|  \____|
                                                             
"""
warning_message += "\nUse this at your own risk! Only use this if you know what you are doing. Please triple-check the .gcode or the changelog.txt after modifying."
print(warning_message)

# Prompt user to continue
input("Press Enter to continue...")

def extract_feed_rate(lines):
    # Function to extract the feed rate value from the G-code lines
    for line in lines:
        if line.startswith('G1') and 'F' in line:
            f_index = line.index('F')
            f_value = line[f_index+1:].split()[0]
            return int(f_value)
    return None

def replace_first_g1_feed_rate(lines, new_f_value):
    # Function to replace the feed rate value of the first G1 command in the G-code lines
    for i, line in enumerate(lines):
        if line.startswith('G1') and 'F' in line:
            f_index = line.index('F')
            old_f_value = line[f_index+1:].split()[0]
            
            # Check if Z value is above 5
            z_index = line.index('Z')
            z_value = float(line[z_index+1:].split()[0])
            
            if z_value > 5:
                line = line[:f_index+1] + str(new_f_value) + line[f_index+1+len(old_f_value):]
            
            lines[i] = line
            break
    return lines

# Function to modify the G-code file
def modify_gcode_file(file_path, new_z_value, new_f_value):
    # Read the original G-code file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the feed rate value from the G-code lines
    f_value = extract_feed_rate(lines)

    if f_value is None:
        # If no feed rate is found, print a message and exit
        print("No feed rate found in the G-code file.")
        return

    modified_lines = []
    skip_next_f_update = False
    changed_lines = []

    for line_number, line in enumerate(lines, start=1):
        if line.startswith('G1'):
            if f'Z{new_z_value}' in line:
                # If the Z value matches the new_z_value, replace the feed rate with the new value
                line = line.replace('F' + str(f_value), 'F' + str(new_f_value))
                skip_next_f_update = True
                changed_lines.append(f"Line {line_number}: {line}")
            elif 'Z' not in line and skip_next_f_update:
                # If 'Z' is not found and the flag is set, replace the feed rate with the new value
                line = line.replace('F' + str(f_value), 'F' + str(new_f_value))
                skip_next_f_update = False
                changed_lines.append(f"Line {line_number}: {line}")
            elif 'Z' in line and float(line.split('Z')[1].split()[0]) < 5:
                # If 'Z' is found and the Z value is less than 5, clear the flag
                skip_next_f_update = False

        modified_lines.append(line)

    # Replace the feed rate value of the first G1 command
    modified_lines = replace_first_g1_feed_rate(modified_lines, new_f_value)

    # Create a new file with modified G-code
    output_file_path = os.path.splitext(file_path)[0] + f'_Z{new_z_value}_F{new_f_value}.gcode'
    with open(output_file_path, 'w') as file:
        file.writelines(modified_lines)

    # Create a change log file with the modified lines
    change_log_path = os.path.splitext(file_path)[0] + f'_Z{new_z_value}_F{new_f_value}change_log.txt'
    with open(change_log_path, 'w') as change_log_file:
        change_log_file.writelines(changed_lines)

    # Print the path of the modified G-code file and change log file
    print(f"Modified G-code file saved as: {output_file_path}")
    print(f"Change log file saved as: {change_log_path}")


# Get the newest .gcode file in the specified directory
script_directory = os.path.dirname(os.path.abspath(__file__))
newest_file = max([f for f in os.listdir(script_directory) if f.endswith('.gcode')], key=os.path.getctime)
file_path = os.path.join(script_directory, newest_file)

print("* This has to match your Fusion 360 retraction to work. e.g. 10,15,20. *")
# Prompt the user to input the retraction distance in fusion (default 5)
new_z_value = int(input("Enter the value for your Z retraction in Fusion: "))

print("* New F(RapidFeed) value should not change your cutting feedrate, please check gcode before running. *")
print("* This value should only change if your Z axis is at the level specified by Z retraction *")

# Prompt the user to input the desired F(Rapid Feedrate) value
new_f_value = int(input("Enter the value to use as new F(Rapid Feedrate): "))

# Check if the value exceeds 5000
if new_f_value > 5000:
    confirm = input("Warning: The specified F value is over 5000. Continue? (Y/N): ")
    if confirm.lower() != 'y':
        print("Script canceled.")
    else:
        # Modify the G-code file and generate change log
        modify_gcode_file(file_path, new_z_value, new_f_value)
else:
    # Modify the G-code file and generate change log
    modify_gcode_file(file_path, new_z_value, new_f_value)

# Generated using ChatGPT.
