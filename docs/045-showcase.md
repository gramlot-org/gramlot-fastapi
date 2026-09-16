# gramlot.showcase

Document ID: **GF-045**.

[Concise counterpart](https://github.com/gramlot-org/gramlot-fastapi/blob/main/docs_llm/045-showcase.md).

<a id="gf-045-005"></a>

## 005 · Run the first host

Block ID: **GF-045-005**.

From an installed development checkout, run:

```sh
python examples/showcase/serve.py
```

Open <http://127.0.0.1:8075/>. FastAPI serves the experimental shared Gramlot
runtime and one Python-authored SPA. No database, Node build or optional database
adapter is required. The showcase source lives in `examples/showcase/pages/index.py`.
The existing SQLAlchemy, Genropy and plain examples are unchanged.

<a id="gf-045-010"></a>

## 010 · Shared experience

Block ID: **GF-045-010**.

The showcase is the growing common example collection intended for every host.
This first implementation is in FastAPI only. The actual Gramlot `borderContainer`
has a logo/header, a left `storeTree`, a central `stackContainer` and a footer.
Navigation binds to `showcase.selected`; switching pages keeps the same Data Bag
and does not navigate to a new server page. The initial collection contains live
name binding, counter actions and a quantity-times-price formula.

**Show source** opens a shared Gramlot palette with the exact current example
method, read through Python `inspect.getsource`. Its stack follows the selected
example. It is a read-only view of author code, not an editor or a generated
pseudocode sample. The shared inspector launcher remains at the bottom right;
its icon or `Ctrl+Shift+D` opens live Data and Source inspection.

The visual shell uses the existing Gramlot logo with navy, gold and light surfaces.
The sidebar distinguishes the shared showcase from host-specific examples. It
does not claim that optional database examples are mounted in this process.

<a id="gf-045-015"></a>

## 015 · Ownership and future ports

Block ID: **GF-045-015**.

`serve.py` owns FastAPI hosting. The `Page` declarations import no host or database
framework; shell methods and individual example methods remain separate. CSS is
presentation only. All state, selection, calculations, actions and the source
palette use Gramlot declarations, Data Bags, bindings and shared components. No
application JavaScript, manual DOM wiring, custom fetch or parallel state is added.
No new framework implementation is copied from the PoC.

The declarations are temporarily housed in this example directory. Before adding
other hosts, extract the common collection and visual assets into a reviewed,
host-independent Gramlot-owned distribution. Other adapters must not depend on
`gramlot_fastapi` for the shared app, and permanent drifting copies are not the
intended ownership model. Python and any approved JavaScript authoring variant
must preserve example IDs, Data paths and observable behavior. Bakery, Polls,
Microblog and other host applications remain separate examples.

The current preview uses the installed experimental runtime. Package versions and
browser APIs remain provisional; this is not acceptance of the PoC as core.

<a id="gf-045-020"></a>

## 020 · Verification

Block ID: **GF-045-020**.

`tests/test_showcase.py` checks actual HTTP recipe delivery, the navigation and
page-selection contract, layout regions, real displayed source and independent
request initialization. Run the repository gate with `python scripts/check.py`.
For browser acceptance, edit the name, change the counter, switch away and back,
change both formula inputs, inspect the current source, and open Data/Source in
the shared inspector. These interactions require a real browser; Python recipe
tests alone do not prove them.

Local browser verification on 2026-09-16 passed: changing Ada to Giovanni updated
the greeting, switching pages retained the name, Increase changed the counter to
1, and quantity 5 with unit price 15 produced total 75. Show source opened the
actual counter_page method, and the shared Inspector opened live Data with its
Source tab available. Border layout, logo and bottom controls were visually checked.
