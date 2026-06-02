from groupdocs.merger import Merger
from groupdocs.merger.domain.options import LoadOptions, UpdatePasswordOptions

def update_document_password():
    # Supply the current (old) password so the protected document can be opened
    load_options = LoadOptions(password="old_p@ss")
    # Load the password-protected document
    with Merger("./protected.pdf", load_options) as merger:
        # Define the replacement password
        update_options = UpdatePasswordOptions("new_p@ss")
        # Apply the new password to the document
        merger.update_password(update_options)
        # Save the document encrypted with the new password
        merger.save("./output.pdf")

if __name__ == "__main__":
    update_document_password()