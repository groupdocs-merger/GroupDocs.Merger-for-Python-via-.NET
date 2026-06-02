from groupdocs.merger import Merger
from groupdocs.merger.domain.options import RotateOptions, RotateMode

def rotate_document_pages():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Rotate pages 1 and 2 by 90 degrees clockwise
        # Pass page numbers as a list — positional integer arguments are not supported
        merger.rotate(RotateOptions(RotateMode.ROTATE90, [1, 2]))
        # Save the document with the rotated pages
        merger.save("./output.pdf")

if __name__ == "__main__":
    rotate_document_pages()