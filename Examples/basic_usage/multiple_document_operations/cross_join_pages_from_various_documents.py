import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # CrossJoinPagesFromVariousDocuments")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        page_join_options = gm.domain.options.PageJoinOptions(1, 2)
        merger.join(constants.sample_docx, page_join_options)
        merger.join(constants.sample_tiff, page_join_options)
        merger.save(constants.output_pdf)
        print(f"Merge to: {constants.output_pdf}")
    
    print(f"----------------------------------------------------------------------------")