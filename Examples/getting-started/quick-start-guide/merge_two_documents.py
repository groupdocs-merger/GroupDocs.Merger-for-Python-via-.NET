from groupdocs.merger import Merger

def merge_two_documents():
    # Load the first DOCX as the merge base
    with Merger("./input.docx") as merger:
        # Append the second DOCX
        merger.join("./input2.docx")
        # Save the combined document
        merger.save("./output.docx")

if __name__ == "__main__":
    merge_two_documents()