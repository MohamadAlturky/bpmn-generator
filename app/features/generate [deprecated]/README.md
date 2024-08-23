# template slice

> this is a demo to how to create features in our system.

## template slice features

- action : this action takes a request and do sth.

## there is 6 modules in every slice

- contarct : contains the response and response body class.
- validator : validates this request.
- model : contains the classes that the llm will use them to generate the response.
- mapping : contains the mapper between the contracts and the models.
- router : defines the endpoint for this feature.
- service : runs the business logic of the feature.
