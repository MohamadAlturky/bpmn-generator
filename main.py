from groq import Groq

client = Groq(
api_key="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"
)


process_description = "Consider a process for purchasing items from an online shop. The user starts an order by logging in to their account. Then, the user simultaneously selects the items to purchase and sets a payment method. Afterward, the user either pays or completes an installment agreement. Since the reward value depends on the purchase value, After selecting the items, the user chooses between multiple options for a free reward. this step is done after selecting the items, but it is independent of the payment activities. Finally, the items are delivered. The user has the right to return items for exchange. Every time items are returned, a new delivery is made."
process_description = """
*Final Report: Process Description for Online Shop Purchase** **Main Steps:** 
1. Login to account 
2.Select items to purchase and set payment method (parallel activities) 
3. Choose free reward (dependent on purchase value, independent of payment activities) 
4. Pay or complete installment agreement 
5. Deliver items 
6. Return items for exchange (optional) 
7. New delivery (optional)
**Gateways:** 
1. Decision gateway: User decides to pay or complete installment agreement 
2. Decision gateway: User decides to return items for exchange 
**Activities:** 
1. Login to account * Input: User credentials * 
Output: Successful login * 
Description: The user logs in to their account using their credentials. 2. Select items to purchase * Input: Available items, user's purchase history * Output:
Selected items * Description: The user browses the online shop and selects the items they wish to
purchase. 3. Set payment method * Input: Available payment options, user's payment history * Output:
Chosen payment method * Description: The user selects a payment method from the available options.
4. Choose free reward * Input: Selected items, reward options * Output: Chosen reward * Description:
The user selects a free reward based on the purchase value. 5. Pay * Input: Chosen payment method,
payment details * Output: Payment confirmation * Description: The user completes the payment using
the chosen payment method. 6. Complete installment agreement * Input: Chosen payment method,
payment plan * Output: Installment agreement confirmation * Description: The user completes the
installment agreement and sets up a payment plan. 7. Deliver items * Input: Payment confirmation,
delivery details * Output: Delivered items * Description: The online shop delivers the purchased items to
the user. 8. Return items for exchange * Input: Delivered items, return reason * Output: Returned items
* Description: The user returns items for exchange, providing a reason for the return. 9. New delivery *
Input: Returned items, new delivery details * Output: New delivered items * Description: The online
shop delivers new items to the user as a replacement for the returned items. **Lane Assignments:** *
User (customer): Login to account, Select items to purchase, Choose free reward, Return items for
exchange * Online Shop (system): Set payment method, Deliver items, New delivery * Payment
Gateway (system): Pay, Complete installment agreement **Additional Notes:** * The process assumes
that the user has already registered with the online shop and has a valid account. * The payment
gateway may have additional steps or validation requirements that are not shown in this process. * The
return and exchange process may have specific business rules or limitations that need to be
considered, such as a time limit for returns or restrictions on certain items. * The online shop may have
different delivery options, such as standard or express shipping, which could affect the delivery
process. This report provides a comprehensive description of the online shop purchase process,
including main steps, gateways, activities, inputs, outputs, and descriptions for each activity. The lane
assignments and additional notes provide further context and clarity for the process.

"""
# Initial prompt for the first agent
initial_prompt = {
    "role": "user",
    "content": f"""
        I want you to create a Business Process Model and Notation (BPMN) model for the process described 
        below. Return the model in the following format: task nodes as words, parallel gateways as AND, exclusive 
        gateways as XOR, and arcs as ->. You should number the gateways. You may also label the outgoing arcs of 
        an exclusive gateway to denote the decision criterion, like XOR Gateway -> (condition 1) Task. Additionally, 
        provide a mapping of actors to activities, in the format actor: [activity1, ...]

        **Process description***
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
