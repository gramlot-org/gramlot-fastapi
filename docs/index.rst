Gramlot FastAPI
===============

Python-first Gramlot interfaces hosted by FastAPI.
This documentation describes an **experimental POC** under review and consolidation.
Examples use ``gramlot-poc`` and will evolve with Gramlot.

Start with :doc:`getting-started` for installation, :doc:`first-page` for your
first page, or :doc:`010-architecture` for the server and database boundaries.

For database access, see :doc:`035-sqlalchemy`: the core contains a read-only SQLite
reader connected to FastAPI through a provisional optional database profile.

`Browse the source code <https://github.com/gramlot-org/gramlot-fastapi/tree/main/src/gramlot_fastapi>`_
· `Concise documentation for LLMs <https://github.com/gramlot-org/gramlot-fastapi/tree/main/docs_llm>`_

.. toctree::
   :maxdepth: 1
   :caption: Start here

   005-overview
   getting-started
   first-page

.. toctree::
   :maxdepth: 1
   :caption: Integration

   guide
   025-inspector
   045-showcase
   035-sqlalchemy
   reference
   010-architecture
   040-server-and-database-integration

.. toctree::
   :maxdepth: 1
   :caption: Contributing and POC records

   015-documentation
   030-readthedocs
   020-release
