from fastapi import FastAPI
from features.template.action.router.endpoint import router as template_router
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(template_router)