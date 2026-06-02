from groupdocs.merger import Merger
from groupdocs.merger.domain.options import AddPasswordOptions

def add_document_password():
    # Load the source document
    with Merger("./input.pdf") as merger:
        # Define the password to apply
        options = AddPasswordOptions("p@ss")
        # Encrypt the document with the specified password
        merger.add_password(options)
        # Save the password-protected document
        merger.save("./output.pdf")

if __name__ == "__main__":
    add_document_password()