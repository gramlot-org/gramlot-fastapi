# gramlot.showcase

Document ID: **GF-045**.

[Expanded counterpart](../docs/045-showcase.md).

<a id="gf-045-005"></a>

## 005 · Run the first host

Block ID: **GF-045-005**.

Run `python examples/showcase/serve.py`; open <http://127.0.0.1:8075/>.
Experimental installed Gramlot runtime, Python declarations, no DB or Node build.
Existing plain, SQLAlchemy and Genropy examples remain unchanged.

<a id="gf-045-010"></a>

## 010 · Shared experience

Block ID: **GF-045-010**.

First host: FastAPI only. Common growing collection: welcome/name binding,
counter/actions, quantity-times-price formula. Actual `borderContainer` contains
logo/header, left `storeTree`, center `stackContainer`, footer Show source and
bottom-right shared inspector. Selection uses `showcase.selected`; Data persists
across page switches without navigation. A Gramlot palette shows the current
method's real Python source via `inspect.getsource`; it follows selection.
Inspector shows live Data/Source and supports `Ctrl+Shift+D`. Navy/gold/light UI.
Host-specific examples stay separate and are not implicitly mounted here.

<a id="gf-045-015"></a>

## 015 · Ownership and future ports

Block ID: **GF-045-015**.

`serve.py` is FastAPI-specific; `pages/index.py` imports no host or database.
Small class methods separate shell/examples. CSS is presentation. UI/state/actions
use existing Gramlot; no copied core, custom JS/DOM/fetch or parallel state.
Before other ports, extract shared declarations/assets from this temporary example
location into a reviewed Gramlot-owned distribution. Do not depend on FastAPI
from other adapters or maintain drifting copies. Preserve IDs, Data paths and
behavior across Python/approved JS variants. Bakery/Polls/Microblog remain separate.
Experimental runtime APIs are provisional, not accepted core contracts.

<a id="gf-045-020"></a>

## 020 · Verification

Block ID: **GF-045-020**.

`tests/test_showcase.py`: HTTP recipe, shared navigation/layout, real source,
request isolation. Gate: `python scripts/check.py`. Browser acceptance separately
checks bindings/actions/formula, navigation persistence, source and inspector.

Local browser verification on 2026-09-16 passed: changing Ada to Giovanni updated
the greeting, switching pages retained the name, Increase changed the counter to
1, and quantity 5 with unit price 15 produced total 75. Show source opened the
actual counter_page method, and the shared Inspector opened live Data with its
Source tab available. Border layout, logo and bottom controls were visually checked.
