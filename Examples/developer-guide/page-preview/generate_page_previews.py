from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PreviewOptions, PreviewMode

def generate_page_previews():
    # Callback: called once per requested page; must return a writable FILE stream
    def create_page_stream(page_number):
        # Open a file for writing — do NOT return BytesIO here
        return open(f"./page-{page_number}.png", "wb")

    # Load the source document
    with Merger("./input.pdf") as merger:
        # Configure preview: PNG format, render pages 1 and 2
        preview_options = PreviewOptions(create_page_stream, PreviewMode.PNG, [1, 2])
        # Rasterize the requested pages and write them via the callback streams
        merger.generate_preview(preview_options)

if __name__ == "__main__":
    generate_page_previews()