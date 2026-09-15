# Integration scope

FastAPI hosting without a database, followed by an optional Genropy database profile.

Use the existing gramlot.contrib.fastapi adapter. Keep Genropy database integration optional and separate from the plain FastAPI profile.

The current artifact is a package scaffold. Hosting, request handling and
database integration have not been implemented here. Application examples
will use Python-authored Gramlot pages and explicit host configuration.
