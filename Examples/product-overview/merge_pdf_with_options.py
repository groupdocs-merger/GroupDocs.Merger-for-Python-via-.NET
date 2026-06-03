from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PageJoinOptions, PdfJoinOptions

def merge_pdf_with_options():
    # Load the first PDF as the merge base
    with Merger("./input.pdf") as merger:
        # Append only pages 1 and 3 from the second PDF
        merger.join("./input2.pdf", PageJoinOptions([1, 3]))

        # Append a third PDF and preserve its bookmarks
        pdf_join = PdfJoinOptions()
        pdf_join.use_bookmarks = True
        merger.join("./input3.pdf", pdf_join)

        # Save the result
        merger.save("./output.pdf")

if __name__ == "__main__":
    merge_pdf_with_options()
