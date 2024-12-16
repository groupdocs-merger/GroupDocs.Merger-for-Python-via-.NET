from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ImportDocumentToWordProcessing")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        pageNumber = 2
        oleWordProcessingOptions = gm.domain.options.OleWordProcessingOptions(constants.sample_pdf, pageNumber)
        oleWordProcessingOptions.width = 300
        oleWordProcessingOptions.height = 300
        merger.import_document(oleWordProcessingOptions)
        merger.save(constants.output_docx)
        print(f"Embedded object was added to the source document successfully")
        print(f"Check output: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")