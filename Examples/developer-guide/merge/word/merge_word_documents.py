from groupdocs.merger import Merger

def merge_word_documents():
    # Load the first document as the merge base
    with Merger("./input.docx") as merger:
        # Append the second Word document
        merger.join("./input2.docx")
        # Save the combined document
        merger.save("./output.docx")

if __name__ == "__main__":
    merge_word_documents()