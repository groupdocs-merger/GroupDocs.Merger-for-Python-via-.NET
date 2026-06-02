from groupdocs.merger import Merger
from groupdocs.merger.domain.options import SwapOptions

def swap_document_pages():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Swap page 1 and page 3 — they will exchange positions in the output
        merger.swap_pages(SwapOptions(1, 3))
        # Save the document with the pages swapped
        merger.save("./output.pdf")

if __name__ == "__main__":
    swap_document_pages()