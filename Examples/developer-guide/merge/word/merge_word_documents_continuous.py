from groupdocs.merger import Merger
from groupdocs.merger.domain.options import WordJoinOptions, WordJoinMode

def merge_word_documents_continuous():
    # Load the first document as the merge base
    with Merger("./input.docx") as merger:
        # Configure join options for continuous (no page break) merging
        word_join_options = WordJoinOptions()
        word_join_options.mode = WordJoinMode.CONTINUOUS
        # Append the second document in continuous mode
        merger.join("./input2.docx", word_join_options)
        # Save the combined document
        merger.save("./output.docx")

if __name__ == "__main__":
    merge_word_documents_continuous()