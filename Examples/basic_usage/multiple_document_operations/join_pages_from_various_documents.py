import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # JoinPagesFromVariousDocuments")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        page_join_options_1 = gm.domain.options.PageJoinOptions(2, 3)
        merger.join(constants.sample_docx, page_join_options_1)
        page_join_options_2 = gm.domain.options.PageJoinOptions(4, 5)
        merger.join(constants.sample_docx, page_join_options_2)
        merger.save(constants.output_docx)
        print(f"Merge to: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")