from groupdocs.merger import Merger
from groupdocs.merger.domain.options import SplitOptions

def split_document_pages():
    # Load the source PDF
    with Merger("./input.pdf") as merger:
        # Split pages 1, 2, and 3 into separate files
        # {0} in the path format is replaced with the page number
        merger.split(SplitOptions("./page_{0}.pdf", [1, 2, 3]))

if __name__ == "__main__":
    split_document_pages()