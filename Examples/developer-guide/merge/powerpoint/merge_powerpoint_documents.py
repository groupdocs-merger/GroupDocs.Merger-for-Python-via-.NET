from groupdocs.merger import Merger

def merge_powerpoint_documents():
    # Load the first presentation as the merge base
    with Merger("./input.pptx") as merger:
        # Append the second PowerPoint presentation
        merger.join("./input2.pptx")
        # Save the combined presentation
        merger.save("./output.pptx")

if __name__ == "__main__":
    merge_powerpoint_documents()