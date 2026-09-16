# FastAPI inspector

[Expanded counterpart and screenshots](../docs/inspector.md).

## 1. Run the example

From a checkout with the preview installed: `gramlot-fastapi serve examples/plain`.
Open http://127.0.0.1:8000/page/inspector/.
Source: `examples/plain/pages/inspector.py`. Both screenshots use this plain
FastAPI page, without a database. APIs are experimental.

## 2. Explore and edit Data

Magnifying glass or Ctrl+Shift+D. Select Data, then message. Edit the Properties
value and leave the row. Screenshot value: Edited through the FastAPI inspector.
The text field and text display share the binding; no database operation occurs.

## 3. Explore and edit Source

Select Source, expand div_0, select h1_0, edit its value and leave the row.
Screenshot heading: FastAPI: live Source edit.
Source is the live UI declaration tree generated from Python.

## 4. Lifetime and boundaries

Edits affect the running page; no Python rewrite or automatic persistence.
Reload/controllers may replace edits; bindings can react to them.
`source_inspection = False` disables the inspector in startup configuration;
it is not server authorization. See SQLAlchemy status and architecture.
