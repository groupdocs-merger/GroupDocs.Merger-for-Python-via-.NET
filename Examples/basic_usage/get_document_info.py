import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # GetDocumentInfo : Get document info")

    with gm.Merger(constants.sample_xlsx) as merger:
        print(f"Document info retrieved successfully")
        info = merger.get_document_info()
        print(f"File format: {info.type.file_format}")
        print(f"File extension: {info.type.extension}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
    
    print(f"----------------------------------------------------------------------------")