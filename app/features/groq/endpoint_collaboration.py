#########################################
## import libraries 📕📗📘📙📔📗📘📒📚##
#########################################

##🔗 from python
from http import HTTPStatus
from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from groq import Groq


from .utils import convert_bpmn_to_nodes_and_edges,parse_json
class Request(BaseModel):
    process_description: str



router = APIRouter(
    prefix="/groq"
)
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

#########################################
## this will be changed for each slice ##
#########################################
## responsibility: define the endpoint ##
#########################################

@router.post("/generate_with_collaboration")
def report(request:Request):
    client = Groq(
        api_key="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"
    )

    process_description = request.process_description

    # Initial prompt for the first agent
    initial_prompt = {
        "role": "user",
        "content": f"""
        As a person who wants to generate a BPMN diagram in a JSON format for the following process description, you are talking to a large language model which is an expert in BPMN. Ask him to help you.

        **Process description***
        {process_description}
        """
    }

    print("Initial Prompt:")
    print(initial_prompt["content"])
    print("\n" + "="*50 + "\n")

    # Function to send message and get response
    def send_message(messages, model="llama-3.1-70b-versatile"):
        response = client.chat.completions.create(
            messages=messages,
            model=model,
        )
        return response.choices[0].message.content

    # First round trip
    print("First Round Trip:")
    print("-"*30)

    # First agent to second agent
    first_agent_message = send_message([initial_prompt])
    print("First Agent:")
    print(first_agent_message)
    print("-"*30)

    # Second agent to first agent
    second_agent_message = send_message([{"role": "user", "content": first_agent_message}])
    print("Second Agent:")
    print(second_agent_message)
    print("-"*30)

    # First agent response
    first_agent_response = send_message([initial_prompt, {"role": "user", "content": second_agent_message}])
    print("First Agent Response:")
    print(first_agent_response)
    print("\n" + "="*50 + "\n")

    # Second round trip
    print("Second Round Trip:")
    print("-"*30)

    # First agent to second agent (continuing the conversation)
    first_agent_message_2 = send_message([
        initial_prompt,
        {"role": "assistant", "content": first_agent_message},
        {"role": "user", "content": second_agent_message},
        {"role": "assistant", "content": first_agent_response},
        {"role": "user", "content": "Can you refine or expand on the BPMN JSON based on our previous conversation?"}
    ])
    print("First Agent:")
    print(first_agent_message_2)
    print("-"*30)

    # Second agent to first agent
    second_agent_message_2 = send_message([{"role": "user", "content": first_agent_message_2}])
    print("Second Agent:")
    print(second_agent_message_2)
    print("-"*30)

    # Final first agent response
    final_response = send_message([
        initial_prompt,
        {"role": "assistant", "content": first_agent_message},
        {"role": "user", "content": second_agent_message},
        {"role": "assistant", "content": first_agent_response},
        {"role": "user", "content": "Can you refine or expand on the BPMN JSON based on our previous conversation?"},
        {"role": "assistant", "content": first_agent_message_2},
        {"role": "user", "content": second_agent_message_2 + """,
        Now you can convert the BPMN representation into a JSON format. The JSON should have the following example structure:
            ```json
            {
            "elements": [
                {
                "type": "StartEvent",
                "name": "Start Event",
                "id": "unique_id"
                },
                {
                "type": "Task",
                "name": "Task Name",
                "id": "unique_id"
                },
                {
                "type": "Gateway",
                "name": "Gateway Type",
                "id": "unique_id"
                },
                {
                "type": "EndEvent",
                "name": "End Event",
                "id": "unique_id"
                },
                {
                "type": "SequenceFlow",
                "sourceRef": "source_id",
                "targetRef": "target_id"
                }
            ]
            }
            ```
            Each element should have a unique identifier (id).
            Use SequenceFlow to represent the arrows showing the flow between elements, with sourceRef and targetRef pointing to the id of the source and target elements, respectively.
        """}
    ])
    print("Final First Agent Response:")
    print(final_response)


    
    
    bpmn_json = parse_json(final_response)

    nodes, edges = convert_bpmn_to_nodes_and_edges(bpmn_json)
    return {"nodes":nodes, "edges":edges}

