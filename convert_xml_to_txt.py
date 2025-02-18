import pyautogui
import pyperclip
import time
import os
import subprocess

def open_xml_in_notepad_plus_plus(xml_file):
    # Path to Notepad++ executable
    notepad_plus_plus_path = r"C:\Program Files\Notepad++\notepad++.exe"
    
    # Open the XML file with Notepad++
    subprocess.Popen([notepad_plus_plus_path, xml_file])
    time.sleep(2)  # Wait for Notepad++ to open

def copy_text_from_notepad_plus_plus():
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    pyautogui.hotkey('ctrl', 'c')  # Copy selected text

def paste_text_to_new_txt_file(txt_file):
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

def convert_xml_to_txt(xml_file):
    txt_file = f"{os.path.splitext(xml_file)}.txt"
    open_xml_in_notepad_plus_plus(xml_file)
    copy_text_from_notepad_plus_plus()
    paste_text_to_new_txt_file(txt_file)
    print(f"Converted {xml_file} to {txt_file}")

# Example usage
directory = input("Provide the full name of the file you want to convert: ")
convert_xml_to_txt(directory)