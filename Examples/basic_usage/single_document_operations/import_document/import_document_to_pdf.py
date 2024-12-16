from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ImportDocumentToPdf")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        pdfAttachmentOptions = gm.domain.options.PdfAttachmentOptions(constants.sample_pptx)
        merger.import_document(pdfAttachmentOptions)
        merger.save(constants.output_pdf)
        print(f"Embedded object was added to the source document successfully")
        print(f"Check output: {constants.output_pdf}")
    
    print(f"----------------------------------------------------------------------------")