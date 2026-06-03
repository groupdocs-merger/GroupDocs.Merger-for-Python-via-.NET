from groupdocs.merger import Merger

def merge_pdf_documents():
    # Load the first PDF as the merge base
    with Merger("./input.pdf") as merger:
        # Append the second PDF
        merger.join("./input2.pdf")
        # Save the merged PDF
        merger.save("./output.pdf")

if __name__ == "__main__":
    merge_pdf_documents()
