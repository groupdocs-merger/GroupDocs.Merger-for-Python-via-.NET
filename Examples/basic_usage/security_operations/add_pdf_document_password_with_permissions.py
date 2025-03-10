import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge # Pdf : AddPdfDocumentPasswordWithPermissions")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        add_password_options = gm.domain.options.PdfSecurityOptions("SomePasswordString")
        add_password_options.permissions = gm.domain.options.PdfSecurityPermissions.DENY_MODIFICATION
        merger.add_password(add_password_options)
        merger.save(constants.output_pdf_permissions)
        print(f"Source document password was added successfully")
        print(f"Check output: {constants.output_pdf_permissions}")
    
    print(f"----------------------------------------------------------------------------")