from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ImportDocumentToSpreadsheet")

    with gm.Merger(constants.sample_xlsx) as merger:
        print(f"Document info retrieved successfully")
        pageNumber = 2
        oleSpreadsheetOptions = gm.domain.options.OleSpreadsheetOptions(constants.sample_pdf, pageNumber)
        oleSpreadsheetOptions.row_index = 2
        oleSpreadsheetOptions.column_index = 2
        merger.import_document(oleSpreadsheetOptions)
        merger.save(constants.output_xlsx)
        print(f"Embedded object was added to the source document successfully")
        print(f"Check output: {constants.output_xlsx}")
    
    print(f"----------------------------------------------------------------------------")