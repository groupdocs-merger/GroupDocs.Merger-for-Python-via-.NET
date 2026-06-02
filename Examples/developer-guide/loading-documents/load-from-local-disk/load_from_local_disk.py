from groupdocs.merger import Merger

def load_from_local_disk():
    # Provide a relative or absolute path to the source document
    with Merger("./input.pdf") as merger:
        # Retrieve document information to confirm the file loaded correctly
        info = merger.get_document_info()
        print("Format:", info.type.file_format)
        print("Pages:", info.page_count)
        print("Size:", info.size, "bytes")

if __name__ == "__main__":
    load_from_local_disk()