from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PdfSecurityOptions, PdfSecurityPermissions

def add_password_to_pdf_with_permissions():
    # Load the source PDF document
    with Merger("./input.pdf") as merger:
        # Create PDF-specific security options with an open password
        security_options = PdfSecurityOptions("p@ss")
        # Deny printing so the recipient cannot print the document
        security_options.permissions = PdfSecurityPermissions.DENY_PRINTING
        # Apply the password and permissions
        merger.add_password(security_options)
        # Save the protected PDF
        merger.save("./output.pdf")

if __name__ == "__main__":
    add_password_to_pdf_with_permissions()