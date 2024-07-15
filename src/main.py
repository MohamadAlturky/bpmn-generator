from fastapi import FastAPI
from features.template.action.router.endpoint import router as template_router
from features.pools.extract.router.endpoint import router as pools_extraction_router

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(template_router)
app.include_router(pools_extraction_router)