from groupdocs.merger import Merger

def merge_html_documents():
    # Load the first HTML file as the merge base
    with Merger("./input.html") as merger:
        # Append the second HTML file
        merger.join("./input2.html")
        # Save the combined HTML file
        merger.save("./output.html")

if __name__ == "__main__":
    merge_html_documents()