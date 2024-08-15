from groq import Groq

client = Groq(
api_key="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"
)


process_description = "Consider a process for purchasing items from an online shop. The user starts an order by logging in to their account. Then, the user simultaneously selects the items to purchase and sets a payment method. Afterward, the user either pays or completes an installment agreement. Since the reward value depends on the purchase value, After selecting the items, the user chooses between multiple options for a free reward. this step is done after selecting the items, but it is independent of the payment activities. Finally, the items are delivered. The user has the right to return items for exchange. Every time items are returned, a new delivery is made."

nodes= [
    {
      "id": "e63919d3-70b6-486e-b254-a2ff633e722e",
      "name": "User",
      "type": "pool"
    },
    {
      "id": "118747bb-dc2d-46e0-8dfa-93f2d2202534",
      "name": "Login",
      "type": "UserTask"
    },
    {
      "id": "f161bf3f-ea91-4c8c-bd62-f7044128a6f1",
      "name": "Select Items",
      "type": "UserTask"
    },
    {
      "id": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "name": "Set Payment Method",
      "type": "UserTask"
    },
    {
      "id": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "name": "Choose Reward",
      "type": "UserTask"
    },
    {
      "id": "8f64a1e4-2a02-4056-845a-5d19586d21be",
      "name": "Pay",
      "type": "UserTask"
    },
    {
      "id": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "name": "Return Items",
      "type": "UserTask"
    },
    {
      "id": "41a2ea16-f56c-437e-9708-e2aaa6ed0212",
      "name": "Shop",
      "type": "pool"
    },
    {
      "id": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "name": "Deliver Items",
      "type": "ServiceTask"
    },
    {
      "id": "1eaea246-0a52-4b89-ba70-c57673207540",
      "name": "Process Installment Agreement",
      "type": "UserTask"
    },
    {
      "id": "d0e41dfd-18ee-44cd-9fb8-c0978999524f",
      "name": "Installment Agreement",
      "type": "ServiceTask"
    }
  ]


edges= [
    {
      "id": "125f02da-6971-47fe-85f6-10736ca40f54",
      "source": "118747bb-dc2d-46e0-8dfa-93f2d2202534",
      "target": "f161bf3f-ea91-4c8c-bd62-f7044128a6f1"
    },
    {
      "id": "c51c866d-ffdd-480a-9e67-030eb6937f20",
      "source": "f161bf3f-ea91-4c8c-bd62-f7044128a6f1",
      "target": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb"
    },
    {
      "id": "a67c3cc4-59fc-421e-9059-1358d7d2c904",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "8f64a1e4-2a02-4056-845a-5d19586d21be"
    },
    {
      "id": "8fde2d96-cace-41ce-9f7b-58cf6c57d104",
      "source": "8f64a1e4-2a02-4056-845a-5d19586d21be",
      "target": "40713bd3-b3c3-4fe6-95e1-4378bf09663e"
    },
    {
      "id": "a210a00a-0d40-4ac0-a381-2787c6746972",
      "source": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "b2527cff-f496-4f9b-bbf4-135303057762",
      "source": "8f64a1e4-2a02-4056-845a-5d19586d21be",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "c7283cae-4679-4bd8-8328-db7945ce4177",
      "source": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "target": "44e57b48-b51b-4b8e-9307-77f91162fa16"
    },
    {
      "id": "72fc219a-a12f-4d9e-a43f-16004405a86b",
      "source": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "1ef6ccc3-637c-43c5-82d7-5c0c6bce4eef",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "40713bd3-b3c3-4fe6-95e1-4378bf09663e"
    },
    {
      "id": "39772c11-875e-487d-8a85-092185ac89ad",
      "source": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "target": "8f64a1e4-2a02-4056-845a-5d19586d21be"
    },
    {
      "id": "b9e47739-fc6d-45fc-bbc0-c7d630587dd5",
      "source": "8f64a1e4-2a02-4056-845a-5d19586d21be",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "add22862-75b7-4932-baac-a46ce120cc67",
      "source": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "49f53ad7-78c2-417d-9f9f-dc0450fd025c",
      "source": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "target": "44e57b48-b51b-4b8e-9307-77f91162fa16"
    },
    {
      "id": "6e9c9fe3-acbb-4c2b-9033-552b77d3d93a",
      "source": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "52e140ef-c20a-4e5c-8e64-faa594eed313",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "d0e41dfd-18ee-44cd-9fb8-c0978999524f"
    },
    {
      "id": "85a0a576-a644-4ab8-a9db-1c59a988065f",
      "source": "d0e41dfd-18ee-44cd-9fb8-c0978999524f",
      "target": "40713bd3-b3c3-4fe6-95e1-4378bf09663e"
    },
    {
      "id": "18352fdb-25e4-4ce8-a392-384e09b57359",
      "source": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "75b5a53c-f007-4920-9eaa-4beb75947620",
      "source": "d0e41dfd-18ee-44cd-9fb8-c0978999524f",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "40832aa4-a4ef-4b9d-bce9-0b1f7941ad1d",
      "source": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "target": "44e57b48-b51b-4b8e-9307-77f91162fa16"
    },
    {
      "id": "01c579c9-3cb5-4a79-bebf-43b24d2df20f",
      "source": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "8316adad-bd2a-47ee-a3f3-9bde544680b9",
      "source": "f161bf3f-ea91-4c8c-bd62-f7044128a6f1",
      "target": "40713bd3-b3c3-4fe6-95e1-4378bf09663e"
    },
    {
      "id": "f732571f-ab69-4133-a019-5bf993f4acc3",
      "source": "40713bd3-b3c3-4fe6-95e1-4378bf09663e",
      "target": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb"
    },
    {
      "id": "d8dbf367-26e6-45a5-9e8a-03bafff4996a",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "8f64a1e4-2a02-4056-845a-5d19586d21be"
    },
    {
      "id": "5dcc3dc6-9064-4219-ace5-576d39a383c7",
      "source": "8f64a1e4-2a02-4056-845a-5d19586d21be",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "9e792f70-7f31-423c-90c7-37793978001e",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "0d2a7448-7f83-42d8-bafb-13f696e540a8",
      "source": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "target": "44e57b48-b51b-4b8e-9307-77f91162fa16"
    },
    {
      "id": "af8e76e5-fa3f-46be-91ad-f2845de9e837",
      "source": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "370aef96-93e5-4698-a180-81bb0f16c8c9",
      "source": "8306380f-3f6c-48a2-ab67-0b1a735e2ecb",
      "target": "d0e41dfd-18ee-44cd-9fb8-c0978999524f"
    },
    {
      "id": "d34756bf-1677-40a9-a7a2-39f010cba2ef",
      "source": "d0e41dfd-18ee-44cd-9fb8-c0978999524f",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    },
    {
      "id": "938e6d9e-c1b8-4778-89ee-0c22b3f795e9",
      "source": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f",
      "target": "44e57b48-b51b-4b8e-9307-77f91162fa16"
    },
    {
      "id": "5a51632c-3d36-4722-99f9-79fde40990b5",
      "source": "44e57b48-b51b-4b8e-9307-77f91162fa16",
      "target": "efda8f8f-ef9e-4b96-a1f9-e8ff37bef06f"
    }
  ]

bpmn_criteria = [
    {
        "criterion": "Syntax Compliance",
        "checks": [
            "Are all BPMN elements (tasks, gateways, events) correctly placed and labeled according to BPMN specifications?",
            "Are sequence flows used correctly to connect elements?"
        ]
    },
    {
        "criterion": "Semantic Accuracy",
        "checks": [
            "Do the elements and flows accurately represent the intended business process?",
            "Are the connections and relationships between elements correctly interpreted?"
        ]
    },
    {
        "criterion": "Process Logic",
        "checks": [
            "Does the sequence of activities and decisions follow the expected business logic?",
            "Are there any missing or redundant activities or decision points?"
        ]
    },
    {
        "criterion": "Boundary Events",
        "checks": [
            "Are boundary events (attached to activities) correctly used to handle exceptions or triggers?"
        ]
    },
    {
        "criterion": "Gateways Usage",
        "checks": [
            "Are exclusive, inclusive, parallel, and complex gateways used appropriately to model decision points and converging/diverging paths?"
        ]
    },
    {
        "criterion": "Data Objects and Data Associations",
        "checks": [
            "Are data objects and data associations correctly used to represent data flow and dependencies?"
        ]
    },
    {
        "criterion": "Message Flows",
        "checks": [
            "If applicable, are message flows correctly used to model interactions between different process participants?"
        ]
    },
    {
        "criterion": "Pool and Lane Usage",
        "checks": [
            "Are pools and lanes (if multiple participants are involved) correctly defined and used to show process ownership and responsibilities?"
        ]
    },
    {
        "criterion": "Event Handling",
        "checks": [
            "Are start, intermediate, and end events used appropriately to signify process triggers, milestones, and completion points?"
        ]
    },
    {
        "criterion": "Error Handling",
        "checks": [
            "Is error handling properly integrated using error events or other appropriate mechanisms?"
        ]
    },
    {
        "criterion": "Sub-processes",
        "checks": [
            "Are sub-processes used where necessary to encapsulate detailed processes or reusable components?"
        ]
    },
    {
        "criterion": "Annotations and Documentation",
        "checks": [
            "Are annotations used to provide additional context or explanations where needed?"
        ]
    },
    {
        "criterion": "Compliance with Standards",
        "checks": [
            "Does the BPMN diagram comply with organizational or industry standards (if applicable)?"
        ]
    },
    {
        "criterion": "Review for Completeness",
        "checks": [
            "Does the diagram capture the entire process scope without any significant gaps?"
        ]
    },
    {
        "criterion": "Validation Against Requirements",
        "checks": [
            "Does the BPMN diagram meet the specified requirements and objectives of the business process it represents?"
        ]
    }
]

# initial_prompt = {
#     "role": "user",
#     "content":
# f"""
#  here's a list of criteria to check if a BPMN (Business Process Model and Notation) diagram is correct:
#  {some_criteria}
#  evaluate on this Process Description:
#  {process_description}
 
#  this is the bpmn elements:
#  {nodes}
 
#  this is the bpmn connections:
#  {edges}
 
# """
# }



        # **Process description***
        # {process_description}

def send_message(messages, model="llama-3.1-70b-versatile"):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return response.choices[0].message.content



for criterion in bpmn_criteria:
    some_criteria = f"{criterion['criterion']}: {' '.join(criterion['checks'])}"
    
    prompt = {
        "role": "user",
        "content": f"""
        Here's a list of criteria to check if a BPMN (Business Process Model and Notation) diagram is correct:
        {some_criteria}
        
        Evaluate on this Process Description:
        {process_description}
        
        This is the BPMN elements:
        {nodes}
        
        This is the BPMN connections:
        {edges}
        
        NOTE:
        if the BPMN element is a part of a pool this is represented in the element as parentId = "pool Id"
        """
    }
    
    response = send_message([prompt])
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")
    print()
    print()
    print()
    print()
    print(response)
    print()
    print()
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print()
    print()
    print()
    print()
    print()
    fix_prompt="""
    provide the actions that have to be done to fix the errors if there is any error
    the actions that can be done:
    - NO_ACTION_NEEDED()
    - ADD_NODE(node)
    - REMOVE_NODE(node)
    - EDIT_NODE(old_node,new_node)
    - ADD_EDGE(edge)
    - REMOVE_EDGE(edge)
    - EDIT_EDGE(old_edge,new_edge)
    """
    fix_response = send_message([prompt,{"role":"assistant","content":response},{"role":"user","content":fix_prompt}])
    
    print()
    print()
    print()
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print("***************************************")
    print()
    print()
    print()
    print()
    print(fix_response)
    print()
    print()
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")
    print("---------------------------------------")
    print()
    print()
    print()
    print()
    print()
    