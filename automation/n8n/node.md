## Node types:
- triggers 
    - schedule
    - form
    - chat
    - webhook
- actions
    - prebuilt integration of apps and services
        - openweather api
        - google
        - youtube
- universal adapter (HTTP request node)
    - connect on any api when its not on the prebuilt list
- logic nodes
    - filter
    - branch
    - merge
    - loop
- Ai agents
    - connect to an Ai agent
    - has memory
    - and connect to tools



## Q&A 
- how the llm know if it has access to a tool or not in n8n?
    - It uses Langchain's Tool Calling under the hood.
    - Simply put, it injects how to call the tools and the tool's name/description into the LLM's prompt, so you don't have to add that yourself. 
