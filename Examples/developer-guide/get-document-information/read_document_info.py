from groupdocs.merger import Merger

def read_document_info():
    # Load the document whose information should be retrieved
    with Merger("./input.pdf") as merger:
        # Obtain the document information object
        info = merger.get_document_info()
        # Print file type details
        print("Type:", info.type.file_format)
        # Print overall document statistics
        print("Pages:", info.page_count, "Size:", info.size, "bytes")
        # Iterate over individual page metadata
        for page in info.pages:
            print(f"  page {page.number}: {page.width}x{page.height}")

if __name__ == "__main__":
    read_document_info()