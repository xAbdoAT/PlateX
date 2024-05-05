import os
import re
import logging

def change_plate_text(new_plate_text):
    if not 1 <= len(new_plate_text) <= 8:
        logging.error("Error: Plate text must be between 1 and 8 characters long.")
        return
    if not re.match("^[a-zA-Z0-9 ]+$", new_plate_text):
        logging.error("Error: Plate text must contain only spaces, numbers, and English letters.")
        return

    user_home_dir = os.path.expanduser("~")
    parent_folder_path = os.path.join(user_home_dir, "AppData", "Roaming", "Stand", "Vehicles")

    if not os.path.exists(parent_folder_path):
        logging.error("Error: The directory path does not exist.")
        return
    
    for root, dirs, files in os.walk(parent_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as fin:
                    lines = fin.readlines()

                with open(file_path, 'w', encoding='utf-8') as fout:
                    for line in lines:
                        if line.startswith("Plate Text:"):
                            fout.write(f"Plate Text: {new_plate_text}\n")
                        else:
                            fout.write(line)
            except IOError as e:
                logging.error(f"Error: Unable to process file {file_path}. {e}")
            except Exception as e:
                logging.error(f"Error: An unexpected error occurred. {e}")

Plate_Text = 'TvAxR'

change_plate_text(Plate_Text)
