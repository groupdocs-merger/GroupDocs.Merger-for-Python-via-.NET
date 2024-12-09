from turtle import update
import requests
import io
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Advanced Usage] # Loading # LoadDocumentFromUrl")

    url = "https://github.com/groupdocs-merger/GroupDocs.Merger-for-.NET/tree/master/Examples/GroupDocs.Merger.Examples.CSharp/Resources/SampleFiles/Pdf/sample.pdf?raw=true"
    stream = download_file(url)
    with gm.Merger(stream) as merger:
        print(f"Document loaded from URL successfully")
    
    print(f"----------------------------------------------------------------------------")

def download_file(url):
    response = requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0"}, timeout=10)
         
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    
    # Create a BytesIO stream from the content
    stream = io.BytesIO(response.content)
    
    return stream