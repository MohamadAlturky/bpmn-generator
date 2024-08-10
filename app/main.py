from fastapi import FastAPI
# from features.template.action.router.endpoint import router as template_router
# from features.generate.reports.router.endpoint import router as reports_router
# from features.generate.diagram.router.endpoint import router as diagram_router
# from features.generate.direct.router.endpoint import router as direct_router
from features.collaboration.generate_with_two.router.endpoint import router as collaboration_router
from features.collaboration.generate_report_with_two.router.endpoint import router as collaboration_report_router
from features.rephrasing.generate.router.endpoint import router as rephrasing_report_router
from features.questions.generate.router.endpoint import router as questions_router
from features.bpmn.generate.router.endpoint import router as bpmn_router
# from features.groq.endpoint import router as groq_router
# from features.groq.endpoint_collaboration import router as groq_with_collaboration_router
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

# app.include_router(template_router)
# app.include_router(reports_router)
# app.include_router(diagram_router)
# app.include_router(direct_router)
# app.include_router(groq_router)
# app.include_router(groq_with_collaboration_router)

app.include_router(collaboration_router)
app.include_router(collaboration_report_router)
app.include_router(rephrasing_report_router)
app.include_router(rephrasing_report_router)
app.include_router(questions_router)
app.include_router(bpmn_router)
