import sys
from PyPDF2 import PdfReader, PdfMerger

def merge_pdfs(pdf_file1, pdf_file2, output_file="merged.pdf"):
  """
  Merges two PDFs and saves the output to a specified file.

  Args:
    pdf_file1 (str): Path to the first PDF file.
    pdf_file2 (str): Path to the second PDF file.
    output_file (str, optional): Path to the output merged PDF file. Defaults to "merged.pdf".
  """
  try:
    merger = PdfMerger()
    merger.append(PdfReader(pdf_file1))
    merger.append(PdfReader(pdf_file2))
    with open(output_file, 'wb') as output:
      merger.write(output)
    print(f"PDFs merged successfully! Output: {output_file}")
  except FileNotFoundError:
    print(f"Error: One or both PDF files not found!")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  # Check for enough arguments
  if len(sys.argv) < 3:
    print("Usage: python main.py <pdf_file1> <pdf_file2> [output_file]")
    sys.exit(1)

  # Get arguments
  pdf_file1 = sys.argv[1]
  pdf_file2 = sys.argv[2]
  output_file = sys.argv[3] if len(sys.argv) > 3 else "merged.pdf"

  # Merge PDFs
  merge_pdfs(pdf_file1, pdf_file2, output_file)
