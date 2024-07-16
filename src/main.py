from fastapi import FastAPI
from features.template.action.router.endpoint import router as template_router
from features.pools.extract.router.endpoint import router as pools_extraction_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(template_router)
app.include_router(pools_extraction_router)
