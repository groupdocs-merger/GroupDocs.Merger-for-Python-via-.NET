from groupdocs.merger import Merger
from groupdocs.merger.domain.options import SplitOptions, SplitMode

def split_document():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Split into separate one-page files for pages 1, 2, and 3
        # Output files: page_0.pdf (page 1), page_1.pdf (page 2), page_2.pdf (page 3)
        merger.split(SplitOptions("./page_{0}.pdf", [1, 2, 3]))

def split_document_by_interval():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Split into multi-page files using page boundaries [2, 4]
        # INTERVAL mode: pages 1 → part_0.pdf, pages 2-3 → part_1.pdf, pages 4+ → part_2.pdf
        merger.split(SplitOptions("./part_{0}.pdf", [2, 4], split_mode=SplitMode.INTERVAL))

if __name__ == "__main__":
    split_document()
    split_document_by_interval()