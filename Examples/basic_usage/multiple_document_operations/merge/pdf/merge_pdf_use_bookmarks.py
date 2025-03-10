import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge # Pdf : MergePdfUseBookmarks")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        pdf_join_options = gm.domain.options.PdfJoinOptions()
        pdf_join_options.use_bookmarks = True
        merger.join(constants.sample_pdf_bookmarks, pdf_join_options)
        merger.save(constants.output_pdf_bookmarks)
        print(f"Merge to: {constants.output_pdf_bookmarks}")
    
    print(f"----------------------------------------------------------------------------")