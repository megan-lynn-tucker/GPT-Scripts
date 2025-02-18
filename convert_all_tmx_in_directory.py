import os
import time
import pyperclip
import pyautogui

def open_tmx_in_notepad_plus_plus(tmx_file):
    try:
        os.startfile(tmx_file)
        time.sleep(3)  # Increased wait time for Notepad++ to open
    except Exception as e:
        print(f"Error opening {tmx_file}: {e}")

def copy_text_from_notepad_plus_plus():
    try:
        pyautogui.hotkey('ctrl', 'a')  # Select all text
        time.sleep(1)  # Increased wait time for the selection to complete
        pyautogui.hotkey('ctrl', 'c')  # Copy selected text
        time.sleep(1)  # Increased wait time for the copy to complete
    except Exception as e:
        print(f"Error copying text: {e}")

def paste_text_to_new_txt_file(txt_file):
    try:
        with open(txt_file, 'w', encoding='utf-8') as f:
            text = pyperclip.paste()  # Get the copied text from clipboard
            text = text.strip()  # Remove leading and trailing whitespace
            lines = text.splitlines()
            cleaned_lines = []
            for line in lines:
                cleaned_line = line.rstrip()  # Remove trailing whitespace but keep leading whitespace (tabs)
                cleaned_lines.append(cleaned_line)
            cleaned_text = '\n'.join(cleaned_lines)
            f.write(cleaned_text)
    except Exception as e:
        print(f"Error pasting text to {txt_file}: {e}")

def close_notepad_plus_plus_tab():
    try:
        pyautogui.hotkey('ctrl', 'w')  # Close current tab in Notepad++
        time.sleep(1)  # Wait for the tab to close
    except Exception as e:
        print(f"Error closing Notepad++ tab: {e}")

def convert_tmx_to_txt(tmx_file, output_directory):
    txt_file = os.path.join(output_directory, f"{os.path.splitext(os.path.basename(tmx_file))}.txt")
    open_tmx_in_notepad_plus_plus(tmx_file)
    copy_text_from_notepad_plus_plus()
    paste_text_to_new_txt_file(txt_file)
    close_notepad_plus_plus_tab()
    print(f"Converted {tmx_file} to {txt_file}")

def convert_all_tmx_in_directory(directory, output_directory):
    for filename in os.listdir(directory):
        if filename.endswith(".tmx"):
            tmx_file = os.path.join(directory, filename)
            try:
                convert_tmx_to_txt(tmx_file, output_directory)
            except Exception as e:
                print(f"Error converting {tmx_file}: {e}")
                continue

directory = input(r"Input the filepath of the tmx files you want to convert to txt files: ")

# Specify the directory containing the TMX files
input_directory = directory

# Specify the directory where the TXT files will be saved
output_directory = directory + "\\Converted"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Convert all TMX files in the specified directory
convert_all_tmx_in_directory(input_directory, output_directory)