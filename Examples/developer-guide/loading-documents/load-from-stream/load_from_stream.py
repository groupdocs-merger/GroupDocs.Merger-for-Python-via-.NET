from groupdocs.merger import Merger

def load_from_stream():
    # Open the base document as a binary stream
    with open("./input.pdf", "rb") as f:
        # Load the document directly from the stream
        with Merger(f) as merger:
            # Append a second document by file path
            merger.join("./input2.pdf")
            # Save the merged result to disk
            merger.save("./output.pdf")

if __name__ == "__main__":
    load_from_stream()