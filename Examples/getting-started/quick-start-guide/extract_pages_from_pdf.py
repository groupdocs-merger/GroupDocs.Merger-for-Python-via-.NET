from groupdocs.merger import Merger
from groupdocs.merger.domain.options import ExtractOptions

def extract_pages_from_pdf():
    # Load the source PDF
    with Merger("./input.pdf") as merger:
        # Extract pages 1 and 2 into a new document
        merger.extract_pages(ExtractOptions([1, 2]))
        # Save the extracted pages as a new PDF
        merger.save("./output.pdf")

if __name__ == "__main__":
    extract_pages_from_pdf()