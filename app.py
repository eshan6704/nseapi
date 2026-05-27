from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from app.router.router import router

# -------------------------------------------------------
# FastAPI app
# -------------------------------------------------------
app = FastAPI(title="Stock / Index Backend")

# -------------------------------------------------------
# Middleware
# -------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# -------------------------------------------------------
# API Routes
# -------------------------------------------------------
app.include_router(router)

# -------------------------------------------------------
# Serve frontend
# -------------------------------------------------------
_FRONTEND = Path(__file__).resolve().parent.parent / "index.html"

@app.get("/")
def root(response: Response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    return FileResponse(_FRONTEND, media_type="text/html")
