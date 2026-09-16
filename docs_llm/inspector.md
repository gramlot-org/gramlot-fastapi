# Inspector and page experiments

[Expanded counterpart and screenshots](../docs/inspector.md).

## 1. Purpose and preview status

Shared Gramlot browser inspector; FastAPI delivers it. Preview descriptions express
intended behavior for API/design evaluation; bugs and incomplete cases may exist.
Screenshots are from Django Bakery, not a FastAPI admin demonstration.

## 2. Open the inspector and explore Data

Magnifying glass or Ctrl+Shift+D when enabled. Data shows page-state Bags.
Expand/select nodes; edit supported Properties values and leave the row to commit.
Bound UI should react. Screenshot: editing detail.title changes the detail heading;
it does not constitute a database write.

## 3. Explore and edit Source

Source is the live declaration tree, not Python source. Edit supported node values
or attributes to experiment. Screenshot: edited heading. Edits do not rewrite
files or automatically persist records; reload/controllers can replace them.
Bindings may trigger application services, so use disposable preview data.
`source_inspection = False` disables the inspector in FastAPI page startup;
it is not server authorization.

## 4. Forms, validation and admin scope

SPA admin/model-derived forms/validation are related Django experiments.
FastAPI has page/service hosting, not an equivalent packaged admin or ORM form
generator. Shared field declarations do not establish model mapping/persistence.
Client feedback, service validation, DB constraints and permissions remain distinct.
See architecture and the proposed standard DB interface; no portable admin contract
is promised by this POC.
