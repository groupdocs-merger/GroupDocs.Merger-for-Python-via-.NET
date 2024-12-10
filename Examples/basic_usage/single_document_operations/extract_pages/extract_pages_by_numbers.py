from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ExtractPagesByNumbers")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        extractOptions = gm.domain.options.ExtractOptions([1, 4 ])
        merger.extract_pages(extractOptions)
        merger.save(constants.output_docx)
        print(f"Source document pages were extracted successfully")
        print(f"Check output: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")