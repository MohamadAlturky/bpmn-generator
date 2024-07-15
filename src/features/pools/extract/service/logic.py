#########################################
## import libraries 📕📗📘📙📔📗📘📒📚##
#########################################

##🔗 from python
import os
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

##🔗 from application core
from core.res.result import Result
from core.settings import env
##🔗 from the same slice
from ..models.types import ProcessDescription, PoolsAndSwimlanes
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : ProcessDescription):
        load_dotenv(override=True)

        llm = Ollama(model=os.getenv(env.DEFAULT_MODEL_NAME), base_url=os.getenv(env.OLLAMA_HOST))

        agent = Agent(
            role="business process analyst",
            goal="Extract pools and swimlanes from the given process description {process_description} and organize them for BPMN diagram generation.",
            backstory="As a business process analyst, you analyze process descriptions to extract and organize elements needed for creating BPMN diagrams.",
            allow_delegation=False,
            verbose=True,
            llm=llm
        )

        task = Task(
            description=(
                "Extract the pools and swimlanes from the given process description {process_description}. "
                "Each pool should represent a major participant (e.g., organization or system), "
                "and each swimlane should represent specific roles or departments within these pools. "
                "List each pool and its corresponding swimlanes, and for each swimlane, provide a sequence of activities. "
                "Ensure each activity is clearly associated with its respective pool and swimlane."
            ),
            expected_output=(
                "A structured list of pools and swimlanes with their respective activities, formatted for BPMN diagram creation."
            ),
            output_pydantic=PoolsAndSwimlanes,
            agent=agent,
        )

        executor = Crew(
            agents=[agent],
            tasks=[task],
            verbose=2
        )
        inputs = {
            "process_description": request.content
        }

        result : PoolsAndSwimlanes = executor.kickoff(inputs)
        
        return Result.success(PoolsAndSwimlanes(pools=result.pools))