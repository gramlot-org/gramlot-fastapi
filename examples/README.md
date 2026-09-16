# Examples

`gramlot_fastapi._examples/genropy` contains packaged Python-authored Gramlot pages for an initialized Genropy
`GnrApp`. Start them from an environment that provides the legacy application:

```python
from gnr.app.gnrapp import GnrApp
from gramlot_fastapi.genropy import create_genropy_application

app = create_genropy_application(
    "src/gramlot_fastapi/_examples/genropy",
    genropy_application=GnrApp("my_instance"),
)
```

The pages expect the sample `invc` model described in their README. Plain
FastAPI hosting does not initialize Genropy and does not expose these pages.
