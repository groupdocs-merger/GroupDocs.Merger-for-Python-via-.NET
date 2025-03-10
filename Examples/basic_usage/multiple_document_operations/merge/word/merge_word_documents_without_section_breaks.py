import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge # Word : MergeWordDocumentsWithoutSectionBreaks")

    with gm.Merger(constants.sample_doc) as merger:
        print(f"Document info retrieved successfully")
        word_join_options = gm.domain.options.WordJoinOptions()
        word_join_options.mode = gm.domain.options.WordJoinMode.DISABLE_SECTION_BREAKS
        merger.join(constants.sample_doc, word_join_options)
        merger.save(constants.output_doc_without_section_breaks)
        print(f"Merge to: {constants.output_doc_without_section_breaks}")
    
    print(f"----------------------------------------------------------------------------")