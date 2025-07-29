# File Merger Python API

[GroupDocs.Merger for Python via .NET](https://products.groupdocs.com/merger/python-net/)  is a powerful API to merge several documents into one, split single document to multiple documents, reorder or replace document pages, change page orientation, manage document protection, render documents as images and more.

Without having to install any 3rd party component, you can use GroupDocs.Merger to build different types applications. For example, GroupDocs, using its own APIs, developed a [free web application](https://products.groupdocs.app/merger/pdf) that allows people to merge their PDF documents online.

>GroupDocs.Merger for Python requires you to use python programming language. For Python, Node.js, Java and .NET languages, we recommend you get [GroupDocs.Merger for Python](https://products.groupdocs.com/merger/python-net/), [GroupDocs.Merger for Node.js](https://products.groupdocs.com/merger/nodejs-java/), [GroupDocs.Merger for Java](https://products.groupdocs.com/merger/java/) and [GroupDocs.Merger for .NET](https://products.groupdocs.com/merger/net/), respectively.

## Python Merger API Features 
* Join two or more documents into one document, join specific pages or page ranges from several source documents into single resultant document.
* Split a source document to several resultant documents.
* Move page to another position within a document.
* Remove single page or a collection of specific page numbers from the source document.
* Rotate pages within document by setting rotation angle to 90,180 or 270 degrees.
* Swap two pages positions within the source document. The result is a new document where two pages have their positions exchanged.
* Extract specified page or page ranges from source document. The result is a new document that contains only specified pages from the source document.
* Change orientation operation lets to set page orientation (portrait, landscape) for specific or all pages of the document.
* Manage document password protection: add/update/delete document password and check its existence.
* Get the basic information about source document - file type, size, pages count, page height and width etc.
* Document preview feature allows to generate image representations of document pages. This may be helpful for better understanding about document content and its structure. Preview can be generated for all document pages (by default) or for specific page numbers or page range.

## Supported File Formats
Merge documents of the [most popular file formats](https://docs.groupdocs.com/merger/python-net/supported-document-formats/) (PDF, DOCX, XLSX, PPTX, JPG, ZIP and more) into single resultant document.

## Platform Independence

GroupDocs.Merger for Python via .NET can be used to develop 32-bit and 64-bit applications for different operating systems (such as Windows, Linux and macOS) where Python 3.5 or later is installed. 

## Get Started
* Fetch the package and install **GroupDocs.Merger**. Run this command: `pip install groupdocs-merger-net`
* If you already have **GroupDocs.Merger** installed and want to get the latest version, you have to run `pip install --upgrade groupdocs-merger-net` instead.
* Call the following command from the root folder of repository `python .\Examples\run_examples.py`
* Review rendered files in `.\Examples\Output` folder

Check out GroupDocs.Merger for Python for .NET [documentation](http://docs.groupdocs.com/merger/python-net/).  

## Merge DOCX using Python

```py
import groupdocs.merger as gv

# Instantiate a Merger object and load a DOCX file
with gv.Merger("sample1.docx") as merger:
    # Add another DOCX file to merge
    merger.join("sample2.docx")
    # Merge DOCX files and save result
    merger.save("merged.docx")
```

[Product Page](https://products.groupdocs.com/merger/python-net/) | [Docs](https://docs.groupdocs.com/merger/python-net/) | [Demos](https://products.groupdocs.app/merger/family) | [API Reference](https://references.groupdocs.com/merger/) | [Blog](https://blog.groupdocs.com/category/merger/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/merger) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
