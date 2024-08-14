from fastapi import FastAPI
from features.collaboration.generate_with_two.router.endpoint import router as collaboration_router
from features.collaboration.generate_report_with_two.router.endpoint import router as collaboration_report_router
from features.rephrasing.generate.router.endpoint import router as rephrasing_report_router
from features.questions.generate.router.endpoint import router as questions_router
from features.bpmn.generate.router.endpoint import router as bpmn_router
from features.bpmn.generateV2.router.endpoint import router as bpmn_router_v2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

origins = [
    "http://localhost:3000",
    "http://172.29.3.110:3000",
    "http://bpmn.hiast.edu.sy",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(collaboration_router)
app.include_router(collaboration_report_router)
app.include_router(rephrasing_report_router)
app.include_router(questions_router)
app.include_router(bpmn_router)
app.include_router(bpmn_router_v2)
