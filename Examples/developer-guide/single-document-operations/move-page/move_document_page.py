from groupdocs.merger import Merger
from groupdocs.merger.domain.options import MoveOptions

def move_document_page():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Move page 4 to position 1 (the beginning of the document)
        merger.move_page(MoveOptions(4, 1))
        # Save the document with the updated page order
        merger.save("./output.pdf")

if __name__ == "__main__":
    move_document_page()