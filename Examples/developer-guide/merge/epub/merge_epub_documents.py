from groupdocs.merger import Merger

def merge_epub_documents():
    # Load the first EPUB file as the merge base
    with Merger("./input.epub") as merger:
        # Append the second EPUB file
        merger.join("./input2.epub")
        # Save the combined EPUB file
        merger.save("./output.epub")

if __name__ == "__main__":
    merge_epub_documents()