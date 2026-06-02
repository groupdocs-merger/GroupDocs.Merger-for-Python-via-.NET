from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PdfJoinOptions

def merge_pdf_with_bookmarks():
    # Load the first document as the merge base
    with Merger("./input.pdf") as merger:
        # Configure join options to preserve bookmarks
        pdf_join_options = PdfJoinOptions()
        pdf_join_options.use_bookmarks = True
        # Append the second PDF document with bookmark options applied
        merger.join("./input2.pdf", pdf_join_options)
        # Save the combined document
        merger.save("./output.pdf")

if __name__ == "__main__":
    merge_pdf_with_bookmarks()