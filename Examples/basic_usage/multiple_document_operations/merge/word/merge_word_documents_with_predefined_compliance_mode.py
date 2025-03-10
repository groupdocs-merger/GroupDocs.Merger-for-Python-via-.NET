import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge # Word : MergeWordDocumentsWithPredefinedComplianceMode")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        word_join_options = gm.domain.options.WordJoinOptions()
        word_join_options.compliance = gm.domain.options.WordJoinCompliance.ISO_29500_2008_STRICT
        merger.join(constants.sample_docx, word_join_options)
        merger.save(constants.output_docx_with_predefined_compliance_mode)
        print(f"Merge to: {constants.output_docx_with_predefined_compliance_mode}")
    
    print(f"----------------------------------------------------------------------------")