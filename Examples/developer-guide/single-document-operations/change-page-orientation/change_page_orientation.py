from groupdocs.merger import Merger
from groupdocs.merger.domain.options import OrientationOptions, OrientationMode

def change_page_orientation():
    # Load the source Word document
    with Merger("./input.pdf") as merger:
        # Set pages 1 and 2 to Landscape orientation
        merger.change_orientation(OrientationOptions(OrientationMode.LANDSCAPE, [1, 2]))
        # Save the document with the updated page orientations
        merger.save("./output.pdf")

if __name__ == "__main__":
    change_page_orientation()