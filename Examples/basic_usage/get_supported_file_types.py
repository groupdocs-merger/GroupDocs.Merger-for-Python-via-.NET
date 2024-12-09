import groupdocs.merger as gm

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # GetSupportedFileFormats : Get supported file formats")

    supported_file_types = gm.domain.FileType.get_supported_file_types()
    for supported_file_type in supported_file_types:
        print(f"Property value: {supported_file_type.extension}")
                    
    print(f"----------------------------------------------------------------------------")