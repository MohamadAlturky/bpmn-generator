from groq import Groq

client = Groq(
    api_key="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"
)

process_description = "Consider a process for purchasing items from an online shop. The user starts an order by logging in to their account. Then, the user simultaneously selects the items to purchase and sets a payment method. Afterward, the user either pays or completes an installment agreement. Since the reward value depends on the purchase value, After selecting the items, the user chooses between multiple options for a free reward. this step is done after selecting the items, but it is independent of the payment activities. Finally, the items are delivered. The user has the right to return items for exchange. Every time items are returned, a new delivery is made."

initial_prompt = {
    "role": "user",
    "content": f"""
                Here are the instructions to extract all activities specified in a process description:

                **Step 1: Read and Understand the Process Description**

                * Carefully read the process description to understand the overall process flow and the context of the activities mentioned.
                * Take note of any specific keywords or phrases that indicate actions, tasks, or steps, such as "perform," "conduct," "carry out," or "complete."

                **Step 2: Identify Activity Keywords and Phrases**

                * From the process description, identify the keywords and phrases that indicate activities. These may include:
                        + Verbs: "create," "review," "approve," "send," "receive," etc.
                        + Action words: "perform," "conduct," "carry out," "complete," etc.
                        + Task-oriented phrases: "review and approval," "data entry," "processing," etc.

                **Step 3: Extract Activities from Sentences**

                * Break down the process description into individual sentences or phrases.
                * For each sentence or phrase, extract the activity by identifying the verb or action word that indicates the task or action being performed.
                * Write down the extracted activity in a concise and descriptive format, using the verb or action word as the starting point.

                **Step 4: Refine and Standardize Activity Descriptions**

                * Review the extracted activities and refine them to ensure they are concise, clear, and consistent.
                * Standardize the activity descriptions by using a consistent format, such as:
                        + Verb + noun (e.g., "Create report")
                        + Verb + adjective + noun (e.g., "Conduct thorough review")
                        + Verb + preposition + noun (e.g., "Send to manager")

                **Step 5: Generate All Possible Traces**

                * After identifying and standardizing the activities, generate all possible traces of the process.
                * Consider the order in which activities must occur, including parallel activities that can occur simultaneously and choices that lead to different paths.
                * Use a systematic approach, such as a decision tree or flowchart, to enumerate all potential sequences of activities.

                **Example Trace Generation**:

                If the process involves three activities A, B, and C, where A and B can occur in parallel, and C must follow both A and B, the possible traces would be:

                1. A -> B -> C
                2. B -> A -> C

                Apply this logic to the process description provided to generate all potential sequences.

                **Process Description**:
                {process_description}
                """
}

def send_message(messages, model="llama-3.1-70b-versatile"):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return response.choices[0].message.content

first_agent_message = send_message([initial_prompt])

print(first_agent_message)
