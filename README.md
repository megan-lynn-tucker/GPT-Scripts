# Scripts
Scripts created using Copilot and MedtronicGPT to assist with the IFU creation process.

convert_all_tmx_in_directory, convert_tmx_to_txt, & convert_xml_to_txt
- need: convert differnt filetypes into txt files (our custom GPTs can only import and export certain filetypes)
- overarching goal: generate translations using GPT and translation memory
- The TMX scripts assume Notepad++ is set as the default application for opening TMX files

highlight_pdf.py
To run the script, follow these steps:

1. Install the required libraries: Make sure you have the necessary libraries installed. You can install them using pip:
pip install pymupdf pandas
Save the script: Copy the entire script and save it to a file, for example, highlight_pdf.py.

2. Prepare your files: Ensure you have the Excel file (requirements.xlsx) and the PDF file (input.pdf) in the same directory as your script.

3. Run the script: Open a terminal or command prompt, navigate to the directory where your script is saved, and run the script using Python:
python highlight_pdf.py
The script will read the requirements from the Excel file, highlight the specified text in the PDF, add comments within the highlighted text, and save the modified PDF to a new file (highlighted_output_with_comments.pdf).
