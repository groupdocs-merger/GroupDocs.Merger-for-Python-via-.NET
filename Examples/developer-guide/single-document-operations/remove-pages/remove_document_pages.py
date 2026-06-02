from groupdocs.merger import Merger
from groupdocs.merger.domain.options import RemoveOptions

def remove_document_pages():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Remove page 2 from the document
        merger.remove_pages(RemoveOptions([2]))
        # Save the document with the specified page removed
        merger.save("./output.pdf")

if __name__ == "__main__":
    remove_document_pages()