from groupdocs.merger import Merger

def merge_text_documents():
    # Load the first text file as the merge base
    with Merger("./input.txt") as merger:
        # Append the second text file
        merger.join("./input2.txt")
        # Save the combined text file
        merger.save("./output.txt")

if __name__ == "__main__":
    merge_text_documents()