from groupdocs.merger import Merger
from groupdocs.merger.domain.options import LoadOptions

def remove_document_password():
    # Supply the current password so the protected document can be opened
    load_options = LoadOptions(password="p@ss")
    # Load the password-protected document
    with Merger("./protected.pdf", load_options) as merger:
        # Remove the open password from the document
        merger.remove_password()
        # Save the decrypted (unprotected) document
        merger.save("./output.pdf")

if __name__ == "__main__":
    remove_document_password()