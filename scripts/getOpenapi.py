from fastapi.openapi.utils import get_openapi
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

with open("openapi.json", "w") as f:
    json.dump(get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes
    ), f, indent=2)


# rm -rf ./FastAPI
# bru import openapi   --source http://127.0.0.1:8000/openapi.json   --output ./   --collection-name "FastAPI"
