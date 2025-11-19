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


- cloudflare access
CF-Access-Client-Id: fd51718dfd3e8e374f7fd81db575171a.access
CF-Access-Client-Secret: 0c6841b22d27bca77ea3116150aaa2c5e81d9694988bca878210e5c2ce546188

 curl -X POST \
  "https://n8n.safwanelmadani.com/webhook-test/47d1f6b2-a91d-422c-bcf7-52a904852308" \
  -H "Content-Type: application/json" \
  -H "CF-Access-Client-Id: fd51718dfd3e8e374f7fd81db575171a.access" \
  -H "CF-Access-Client-Secret: 0c6841b22d27bca77ea3116150aaa2c5e81d9694988bca878210e5c2ce546188" \
  -d '{"msg":"hello"}'
