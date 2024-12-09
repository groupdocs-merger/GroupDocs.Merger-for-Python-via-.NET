import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # JoinPagesUsingPageBuilder")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_simple_pdf)
        
        page_builder_options = gm.domain.options.PageBuilderOptions()
        page_builder_options.load_document_info = True
        
        page_builder = merger.create_page_builder(page_builder_options)
        page_builder.add_page(1, 1) # Add 1 page of the second document
        page_builder.add_page(0, 2) # Add 2 page of the first document
        page_builder.add_page(1, 2) # Add 2 page of the second document
        
        merger.apply_page_builder(page_builder);
        merger.save(constants.output_pdf)
        print(f"Merge to: {constants.output_pdf}")
    
    print(f"----------------------------------------------------------------------------")