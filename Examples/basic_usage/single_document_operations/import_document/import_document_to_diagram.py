from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ImportDocumentToDiagram")

    with gm.Merger(constants.sample_vsdx) as merger:
        print(f"Document info retrieved successfully")
        pageNumber = 2
        oleDiagramOptions = gm.domain.options.OleDiagramOptions(constants.sample_pptx, pageNumber)
        oleDiagramOptions.x = 1
        oleDiagramOptions.y = 1
        merger.import_document(oleDiagramOptions)
        merger.save(constants.output_vsdx)
        print(f"Embedded object was added to the source document successfully")
        print(f"Check output: {constants.output_vsdx}")
    
    print(f"----------------------------------------------------------------------------")