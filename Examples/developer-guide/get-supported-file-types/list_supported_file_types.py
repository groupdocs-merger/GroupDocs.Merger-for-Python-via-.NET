from groupdocs.merger.domain import FileType

def list_supported_file_types():
    # Retrieve the complete collection of supported file types
    supported_types = FileType.get_supported_file_types()
    # Print the format name and extension for each supported type
    for ft in supported_types:
        print(ft.file_format, ft.extension)

if __name__ == "__main__":
    list_supported_file_types()