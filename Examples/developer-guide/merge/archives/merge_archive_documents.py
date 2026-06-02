from groupdocs.merger import Merger

def merge_archive_documents():
    # Load the first archive as the merge base
    with Merger("./input.zip") as merger:
        # Append the second archive
        merger.join("./input2.zip")
        # Save the combined archive
        merger.save("./output.zip")

if __name__ == "__main__":
    merge_archive_documents()