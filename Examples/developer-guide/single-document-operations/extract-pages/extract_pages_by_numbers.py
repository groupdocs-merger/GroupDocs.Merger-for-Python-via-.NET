from groupdocs.merger import Merger
from groupdocs.merger.domain.options import ExtractOptions, RangeMode

def extract_pages_by_numbers():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Extract pages 2, 4, and 6 into a new document
        merger.extract_pages(ExtractOptions([2, 4, 6]))
        # Save the document that contains only the extracted pages
        merger.save("./output.pdf")

def extract_pages_even_range():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Extract all even-numbered pages between pages 1 and 6 (i.e. pages 2, 4, 6)
        merger.extract_pages(ExtractOptions(
            start_number=1,
            end_number=6,
            mode=RangeMode.EVEN_PAGES,
        ))
        # Save the resulting document
        merger.save("./output.pdf")

if __name__ == "__main__":
    extract_pages_by_numbers()
    extract_pages_even_range()