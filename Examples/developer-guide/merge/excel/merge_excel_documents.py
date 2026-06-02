from groupdocs.merger import Merger

def merge_excel_documents():
    # Load the first document as the merge base
    with Merger("./input.xlsx") as merger:
        # Append the second Excel spreadsheet
        merger.join("./input2.xlsx")
        # Save the combined document
        merger.save("./output.xlsx")

if __name__ == "__main__":
    merge_excel_documents()