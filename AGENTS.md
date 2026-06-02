<!-- generator:skip -->
# GroupDocs.Merger for Python via .NET -- AGENTS.md

> Instructions for AI agents working with this package.

Merge, split, reorder, swap, move, rotate, and extract pages across documents -- Word, Excel, PowerPoint, PDF, Visio, images, eBooks, email, and text formats, all without MS Office or any external software installed. Add, remove, or change passwords, change page orientation, and render page previews through one unified API.

## Install

```bash
pip install groupdocs-merger-net
```

**Python**: 3.5 - 3.14 | **Platforms**: Windows, Linux, macOS

## Resources

| Resource | URL |
|---|---|
| Documentation | https://docs.groupdocs.com/merger/python-net/ |
| LLM-optimized docs | https://docs.groupdocs.com/merger/python-net/llms-full.txt |
| API reference | https://reference.groupdocs.com/merger/python-net/ |
| Code examples | https://docs.groupdocs.com/merger/python-net/developer-guide/ |
| Release notes | https://releases.groupdocs.com/merger/python-net/release-notes/ |
| PyPI | https://pypi.org/project/groupdocs-merger-net/ |
| Free support forum | https://forum.groupdocs.com/c/merger/ |
| Temporary license | https://purchase.groupdocs.com/temporary-license |

## MCP Server

If your environment has MCP configured, you can connect your AI tool to the GroupDocs documentation server for on-demand API lookups:

```json
{
  "mcpServers": {
    "groupdocs-docs": {
      "url": "https://docs.groupdocs.com/mcp"
    }
  }
}
```

Works with Claude Code (`~/.claude/settings.json`), Cursor (`.cursor/mcp.json`), VS Code Copilot (`.vscode/mcp.json`), and any MCP-compatible client. If MCP is unavailable, fall back to the LLM-optimized docs URL above and this file -- both are shipped inside the wheel.

## Imports

```python
from groupdocs.merger import (
    License, Metered, Merger, MergerSettings,
)
from groupdocs.merger.domain import FileType
from groupdocs.merger.domain.options import (
    # Join
    JoinOptions, PageJoinOptions, ImageJoinOptions, ImageJoinMode,
    WordJoinOptions, WordJoinMode, PdfJoinOptions,
    # Split
    SplitOptions, SplitMode, TextSplitOptions, TextSplitMode,
    # Page operations
    ExtractOptions, RemoveOptions, SwapOptions, MoveOptions,
    RotateOptions, RotateMode, OrientationOptions, OrientationMode, RangeMode,
    # Security
    AddPasswordOptions, UpdatePasswordOptions, PdfSecurityOptions, PdfSecurityPermissions,
    # Load / save / preview
    LoadOptions, SaveOptions, PdfSaveOptions, PreviewOptions, PreviewMode,
)
from groupdocs.merger.domain.result import IDocumentInfo, IPageInfo
from groupdocs.merger.exceptions import (
    GroupDocsMergerException, FileCorruptedException,
    IncorrectPasswordException, PasswordRequiredException, FileTypeNotSupportedException,
)
from groupdocs.merger.logging import ConsoleLogger
```

## Load + Operate + Save (the core workflow)

`Merger` is the entry point. The flow is always: **open → one or more operations → `save()`**. Operations mutate the in-memory document, so you can chain several before a single `save`. Use `Merger` as a context manager so the native document handle is released.

```python
from groupdocs.merger import Merger

with Merger("document1.docx") as merger:
    merger.join("document2.docx")        # append a second DOCX
    merger.save("merged.docx")           # write the result
```

**Merger constructor.** `Merger(file_path)`, `Merger(stream)`, optionally with `load_options` and/or `MergerSettings`: `Merger(file_path, LoadOptions(...))`, `Merger(stream, LoadOptions(...), MergerSettings(...))`. Pass `LoadOptions(password=...)` to open a protected source.

**`merger.save(file_path_or_stream[, save_options])`** writes the current state to disk or a stream. Saving does not consume the `Merger` — you may continue operating and save again.

## Operations

### Merge / join documents

`join` appends another document to the one already loaded. The documents should share a format family (DOCX+DOCX, PDF+PDF, …). Pass a path or a binary stream; optional `*JoinOptions` tune the result.

```python
from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PageJoinOptions, WordJoinOptions, WordJoinMode

with Merger("source.docx") as merger:
    merger.join("appendix.docx")                                  # whole document
    merger.join("notes.docx", PageJoinOptions([1, 3]))            # only pages 1 and 3
    merger.save("combined.docx")

# Word-specific: continuous join, no section breaks
with Merger("a.docx") as merger:
    wj = WordJoinOptions()
    wj.mode = WordJoinMode.CONTINUOUS
    merger.join("b.docx", wj)
    merger.save("continuous.docx")
```

`ImageJoinOptions(FileType.PNG, ImageJoinMode.VERTICAL)` stacks images; `PdfJoinOptions` exposes `use_bookmarks` / `preserve_accessibility`.

### Split a document

`split` writes each output via a path-format template (`{0}` is substituted with the index). `SplitOptions` works for paged documents; `TextSplitOptions` splits plain text by lines or intervals.

```python
from groupdocs.merger import Merger
from groupdocs.merger.domain.options import SplitOptions, SplitMode

with Merger("multipage.pdf") as merger:
    # one output file per listed page
    merger.split(SplitOptions("page_{0}.pdf", [1, 3, 5]))

with Merger("multipage.pdf") as merger:
    # split into intervals
    merger.split(SplitOptions("part_{0}.pdf", [2, 4], split_mode=SplitMode.INTERVAL))
```

### Page operations

All page numbers are **1-based**. `RangeMode.ODD_PAGES` / `EVEN_PAGES` narrow a start/end range.

```python
from groupdocs.merger import Merger
from groupdocs.merger.domain.options import (
    ExtractOptions, RemoveOptions, SwapOptions, MoveOptions,
    RotateOptions, RotateMode, OrientationOptions, OrientationMode, RangeMode,
)

with Merger("doc.pdf") as merger:
    merger.extract_pages(ExtractOptions([1, 2, 3]))      # keep only these pages
    merger.save("first_three.pdf")

with Merger("doc.pdf") as merger:
    merger.remove_pages(RemoveOptions([2]))              # drop page 2
    merger.swap_pages(SwapOptions(1, 3))                 # swap pages 1 and 3
    merger.move_page(MoveOptions(4, 1))                  # move page 4 to position 1
    merger.rotate(RotateOptions(RotateMode.ROTATE90, [1]))
    merger.change_orientation(OrientationOptions(OrientationMode.LANDSCAPE, start_number=1, end_number=2))
    merger.save("reordered.pdf")

# extract a range, even pages only
ExtractOptions(start_number=1, end_number=10, mode=RangeMode.EVEN_PAGES)
```

### Password protection

```python
from groupdocs.merger import Merger
from groupdocs.merger.domain.options import (
    AddPasswordOptions, UpdatePasswordOptions, LoadOptions,
)

# Add a password
with Merger("doc.pdf") as merger:
    merger.add_password(AddPasswordOptions("secret"))
    merger.save("protected.pdf")

# Open a protected file, change or remove its password
with Merger("protected.pdf", LoadOptions(password="secret")) as merger:
    if merger.is_password_set():
        merger.update_password(UpdatePasswordOptions("new-secret"))
    merger.save("rekeyed.pdf")

with Merger("protected.pdf", LoadOptions(password="secret")) as merger:
    merger.remove_password()
    merger.save("unprotected.pdf")
```

### Page builder

`create_page_builder` / `apply_page_builder` assemble a new document from selected pages of multiple loaded documents.

### Page preview

`generate_preview(PreviewOptions(...))` renders pages to images (PNG / JPEG / BMP). Pass a plain Python `create_page_stream(page_number)` callable that returns a writable stream for each page — the binding wraps it as the .NET delegate automatically.

```python
from groupdocs.merger import Merger
from groupdocs.merger.domain.options import PreviewOptions, PreviewMode

def create_page_stream(page_number):
    return open(f"page-{page_number}.png", "wb")    # return a file/path stream

with Merger("doc.pdf") as merger:
    merger.generate_preview(PreviewOptions(create_page_stream, PreviewMode.PNG, [1, 2]))
```

The same page-stream callback pattern powers the stream-callback overloads of `split` — pass a `create_split_stream(number)` callable instead of a path-format template:

```python
from groupdocs.merger.domain.options import SplitOptions, SplitMode

def create_split_stream(number):
    return open(f"chunk-{number}.pdf", "wb")

with Merger("multipage.pdf") as merger:
    merger.split(SplitOptions(create_split_stream, [1, 2], SplitMode.PAGES))
```

> **Return a file/path stream, not `io.BytesIO()`, from these callbacks.** The engine writes into the stream you return, but in-memory `BytesIO` returned from a *callback* is not copied back to Python (unlike `save(BytesIO)`). Use `open(path, "wb")` (or any path-backed stream) so the rendered bytes land on disk.

### Document info (no full processing)

`get_document_info()` returns an `IDocumentInfo`: `page_count`, `size`, `type` (a `FileType`), and `pages` (a list of `IPageInfo` with `number`, `visible`, `width`, `height`).

```python
with Merger("doc.pdf") as merger:
    info = merger.get_document_info()
    print("pages:", info.page_count, "size:", info.size, "type:", info.type.file_format)
    for page in info.pages:
        print(f"  page {page.number}: {page.width}x{page.height}")
```

## Licensing

```python
from groupdocs.merger import License

# From file
License().set_license("path/to/license.lic")

# From stream
with open("license.lic", "rb") as f:
    License().set_license(f)
```

Or auto-apply: `export GROUPDOCS_LIC_PATH="path/to/license.lic"`

Metered licensing is also available:

```python
from groupdocs.merger import Metered

Metered().set_metered_key("public-key", "private-key")
print(Metered().get_consumption_quantity(), Metered().get_consumption_credit())
```

**Evaluation vs licensed.** Without a license the library still runs, but PDF output carries an evaluation watermark stamp and non-PDF targets show an equivalent evaluation mark; there is also a page/document count cap. Set `GROUPDOCS_LIC_PATH` (or call `License().set_license(...)`) and re-run to clear both. A 30-day full license is free: https://purchase.groupdocs.com/temporary-license

## API Reference

### Merger

| Method | Returns | Description |
|---|---|---|
| `Merger(file_path / stream [, load_options [, settings]])` | | Open by path or binary stream; optional `LoadOptions` and `MergerSettings`. Use as a context manager. |
| `join(file_path / stream [, join_options])` | `IMerger` | Append another document; optional `JoinOptions` / `PageJoinOptions` / `ImageJoinOptions` / `WordJoinOptions` / `PdfJoinOptions`. |
| `split(split_options)` | `IMerger` | Split into multiple files via `SplitOptions` or `TextSplitOptions` (path-format template with `{0}`). |
| `extract_pages(extract_options)` | `IMerger` | Keep only the pages named by `ExtractOptions`. |
| `remove_pages(remove_options)` | `IMerger` | Delete the pages named by `RemoveOptions`. |
| `swap_pages(swap_options)` | `IMerger` | Swap two pages (`SwapOptions(first, second)`). |
| `move_page(move_options)` | `IMerger` | Move a page to a new position (`MoveOptions(from, to)`). |
| `rotate(rotate_options)` | `IMerger` | Rotate pages (`RotateOptions(RotateMode.ROTATE90, [pages])`). |
| `change_orientation(orientation_options)` | `IMerger` | Set portrait/landscape (`OrientationOptions`). |
| `add_password(add_password_options)` | `IMerger` | Protect output with a password. |
| `is_password_set()` | `bool` | Whether the loaded document is protected. |
| `remove_password()` | `IMerger` | Strip protection. |
| `update_password(update_password_options)` | `IMerger` | Change the password. |
| `import_document(import_document_options)` | `IMerger` | Embed an OLE object / attachment (`Ole*Options`, `PdfAttachmentOptions`). |
| `create_page_builder([page_builder_options])` | `PageBuilder` | Start assembling a document from selected pages. |
| `apply_page_builder(page_builder)` | `None` | Apply a built page selection. |
| `generate_preview(preview_options)` | `None` | Render pages to images via a `create_page_stream(page_number)` callable (`PreviewMode.PNG`/`JPEG`/`BMP`). Return a file/path stream, not `BytesIO`. |
| `get_document_info()` | `IDocumentInfo` | `page_count`, `size`, `type`, `pages` (list of `IPageInfo`). |
| `save(file_path / stream [, save_options])` | `IMerger` | Write current state; optional `SaveOptions` / `PdfSaveOptions`. |
| `dispose()` | `None` | Release native resources (handled by `with`). |

### Options & enums

| Type | Notes |
|---|---|
| `JoinOptions(file_type)` / `PageJoinOptions(page_numbers, …)` | Whole-document or page-subset join. |
| `ImageJoinOptions(file_type, image_join_mode)` | `ImageJoinMode.HORIZONTAL` / `VERTICAL`. |
| `WordJoinOptions` / `PdfJoinOptions` | `WordJoinMode`, `WordJoinCompliance`; `use_bookmarks`, `preserve_accessibility`. |
| `SplitOptions(file_path_format, page_numbers, split_mode=…)` | `SplitMode.PAGES` / `INTERVAL`. |
| `TextSplitOptions(file_path_format, line_numbers, mode=…)` | `TextSplitMode.LINES` / `INTERVAL`. |
| `ExtractOptions` / `RemoveOptions` / `RotateOptions` / `OrientationOptions` | Accept `page_numbers=[…]` or `start_number`/`end_number` + `RangeMode`. |
| `SwapOptions(first_page_number, second_page_number)` | 1-based page numbers. |
| `MoveOptions(page_number_to_move, new_page_number)` | 1-based page numbers. |
| `RotateMode` | `ROTATE90`, `ROTATE180`, `ROTATE270`. |
| `OrientationMode` | `PORTRAIT`, `LANDSCAPE`. |
| `RangeMode` | `ALL_PAGES`, `ODD_PAGES`, `EVEN_PAGES`. |
| `AddPasswordOptions(password)` / `UpdatePasswordOptions(new_password)` | Document password management. |
| `PdfSecurityOptions(password)` | `owner_password`, `permissions` (`PdfSecurityPermissions`). |
| `LoadOptions(file_type, password, encoding, extension, …)` | Force type / decode protected or extension-less input. |
| `SaveOptions` / `PdfSaveOptions` | `PdfSaveOptions.accesibility_settings` for tagged PDF. |
| `PreviewOptions(create_page_stream, preview_mode, …)` | `PreviewMode.PNG` / `JPEG` / `BMP`. |

### License / Metered

`License().set_license(path_or_stream)` · `Metered().set_metered_key(public, private)` · `Metered().get_consumption_quantity()` · `Metered().get_consumption_credit()`

## Key Patterns

- **Properties**: use `snake_case` -- auto-mapped to .NET `PascalCase`
- **Context managers**: `with Merger(...) as m:` ensures the document handle is released
- **Chaining**: operations mutate in place; run several before one `save()`
- **1-based pages**: every page number argument starts at 1, not 0
- **Path templates**: `split` outputs use a `{0}` placeholder, e.g. `"page_{0}.pdf"`
- **Streams**: pass `open("file", "rb")` or `io.BytesIO(data)` where .NET expects a Stream; `BytesIO` is updated after `save(stream)`
- **Enums**: case-insensitive, lazy-loaded (e.g., `FileType.PDF`, `RotateMode.ROTATE90`)
- **Collections**: `for page in info.pages` and `len(...)` work on .NET collections
- **Exceptions**: catch `PasswordRequiredException` / `IncorrectPasswordException` / `FileCorruptedException` / `FileTypeNotSupportedException` (all subclass `GroupDocsMergerException`)

## Platform Requirements

| Platform | Requirements |
|---|---|
| Windows | None |
| Linux | `apt install libgdiplus libfontconfig1 ttf-mscorefonts-installer` |
| macOS | `brew install mono-libgdiplus` |

## Troubleshooting

**`PasswordRequiredException` / `IncorrectPasswordException`** -- the source is encrypted. Open it with `Merger(path, LoadOptions(password="..."))`.

**`FileTypeNotSupportedException` when joining** -- the two documents are different format families. Join documents of the same family, or convert first.

**`System.Drawing.Common is not supported`** -- install libgdiplus: `sudo apt install libgdiplus` (Linux) / `brew install mono-libgdiplus` (macOS)

**`Gdip` type initializer exception** -- outdated libgdiplus: `brew reinstall mono-libgdiplus` (macOS)

**Garbled text / missing fonts** -- install fonts: `sudo apt install ttf-mscorefonts-installer fontconfig && sudo fc-cache -f`

**`DllNotFoundException: libSkiaSharp`** -- stale system copy conflicts with bundled version. Rename it: `sudo mv /usr/local/lib/libSkiaSharp.dylib /usr/local/lib/libSkiaSharp.dylib.bak`

**`DOTNET_SYSTEM_GLOBALIZATION_INVARIANT` errors** -- do NOT set this. Install ICU: `sudo apt install libicu-dev`

**`TypeLoadException`** -- reinstall: `pip install --force-reinstall groupdocs-merger-net`

**Still stuck?** Post your question at https://forum.groupdocs.com/c/merger/ -- the development team responds directly.
