from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ImportDocumentToPresentation")

    with gm.Merger(constants.sample_pptx) as merger:
        print(f"Document info retrieved successfully")
        pageNumber = 2
        olePresentationOptions = gm.domain.options.OlePresentationOptions(constants.sample_pdf, pageNumber)
        olePresentationOptions.x = 1
        olePresentationOptions.y = 1
        merger.import_document(olePresentationOptions)
        merger.save(constants.output_pptx)
        print(f"Embedded object was added to the source document successfully")
        print(f"Check output: {constants.output_pptx}")
    
    print(f"----------------------------------------------------------------------------")