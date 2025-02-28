import fitz  # PyMuPDF
import pandas as pd

def read_requirements_from_excel(excel_file, sheet_name='Sheet1'):
    """Read requirements and comments from an Excel file."""
    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
    # Assuming the first column is 'Text' and the second column is 'Requirement'
    requirements = df[['Text', 'Requirement']].dropna().values.tolist()
    return requirements

def highlight_text_and_add_comment_in_pdf(pdf_file, output_file, requirements, no_matches_file):
    """Highlight text in a PDF and add comments that fulfill the requirements."""
    # Open the PDF
    pdf_document = fitz.open(pdf_file)
    
    # List to store comments for which no matches were found
    no_matches = []

    for text, comment in requirements:
        text = str(text).strip()
        comment = str(comment).strip()
        if text:
            print(f"Searching for: '{text}'")
            found = False
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                text_instances = page.search_for(text)
                if text_instances:
                    found = True
                    inst = text_instances  # Take the first instance only
                    # Highlight the found text
                    highlight = page.add_highlight_annot(inst)
                    # Add a comment annotation within the highlighted text
                    highlight.set_popup(page)
                    highlight.set_info(info={"title": "Requirement", "content": comment})
                    highlight.update()
                    print(f"Highlighted '{text}' and added comment: '{comment}' on page {page_num + 1}")
                    break  # Exit after finding the first match
            if not found:
                print(f"No matches found for: '{text}'")
                no_matches.append(f"{text}: {comment}")

    # Save the modified PDF to a new file
    pdf_document.save(output_file)
    pdf_document.close()
    print(f"Highlights and comments saved to {output_file}")

    # Write no matches to a txt file
    with open(no_matches_file, 'w') as f:
        for line in no_matches:
            f.write(line + '\n')
    print(f"No matches information saved to {no_matches_file}")

# Example usage
excel_file = "requirements.xlsx"  # Input Excel file containing text and comments
pdf_file = "input.pdf"            # Input PDF file to be highlighted
output_file = "highlighted_output_with_comments.pdf"  # Output PDF file with highlights and comments
no_matches_file = "no_matches.txt"  # Output txt file with no matches information

requirements = read_requirements_from_excel(excel_file)
highlight_text_and_add_comment_in_pdf(pdf_file, output_file, requirements, no_matches_file)