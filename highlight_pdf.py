import fitz  # PyMuPDF
import pandas as pd

def read_requirements_from_excel(excel_file, sheet_name='Sheet1'):
    """Read requirements and comments from an Excel file."""
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    # Assuming the first column is 'Text' and the second column is 'Comment'
    requirements = df[['Text', 'Comment']].dropna().values.tolist()
    return requirements

def highlight_text_and_add_comment_in_pdf(pdf_file, output_file, requirements):
    """Highlight text in a PDF and add comments that fulfill the requirements."""
    # Open the PDF
    pdf_document = fitz.open(pdf_file)

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        print(f"Processing page {page_num + 1}")

        for text, comment in requirements:
            text = str(text).strip()
            comment = str(comment).strip()
            if text:
                print(f"Searching for: '{text}'")
                text_instances = page.search_for(text)
                if not text_instances:
                    print(f"No matches found for: '{text}'")
                for inst in text_instances:
                    # Highlight the found text
                    highlight = page.add_highlight_annot(inst)
                    # Add a comment annotation within the highlighted text
                    highlight.set_popup(page)
                    highlight.set_info(info={"title": "Comment", "content": comment})
                    highlight.update()
                    print(f"Highlighted '{text}' and added comment: '{comment}' on page {page_num + 1}")

    # Save the modified PDF to a new file
    pdf_document.save(output_file)
    pdf_document.close()
    print(f"Highlights and comments saved to {output_file}")

# Example usage
excel_file = "requirements.xlsx"  # Input Excel file containing text and comments
pdf_file = "input.pdf"            # Input PDF file to be highlighted
output_file = "highlighted_output_with_comments.pdf"  # Output PDF file with highlights and comments

requirements = read_requirements_from_excel(excel_file)
highlight_text_and_add_comment_in_pdf(pdf_file, output_file, requirements)