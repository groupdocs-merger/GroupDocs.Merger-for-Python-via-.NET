from groupdocs.merger import Merger

def merge_pdf_documents():
    # Load the first document as the merge base
    with Merger("./input.pdf") as merger:
        # Append the second PDF document
        merger.join("./input2.pdf")
        # Save the combined document
        merger.save("./output.pdf")

if __name__ == "__main__":
    merge_pdf_documents()