

## how to know if an LLM is capable to calling functions?
- https://blog.christoolivier.com/p/llms-and-functiontool-calling
- No part of the LLM executes the function call. The LLM only determines which function to call and with what arguments
- The actual execution is handled by the external application code that uses the LLM
-  then sends the results back to the LLM to formulate a final user-facing response
- the LLM has to support this feature.
- Ollama calls it format json
- OpenAI calls it function calling
- Basically, it's a feature to get consistant output from the model and then using that output to call a function.
    - "It’s important to emphasize that when using function calling, the LLM itself does not execute the function. Instead, it identifies the appropriate function, gathers all required parameters, and provides the information in a structured JSON format. This JSON output can then be easily deserialized into a function call in Python (or any other programming language) "

### function call leaderboard
- https://gorilla.cs.berkeley.edu/leaderboard.html

## base model vs instruct model
- The instruct model is fine tuned to follow instructions so it can do tasks and answer questions in a natural way. The base model doesn’t do that.

## Q&A 
- how the llm know if it has access to a tool or not n8n?
    - It uses Langchain's Tool Calling under the hood.
- Multi-turn?
- temperature

## models with tool calling 
- qwen3
- gemma 3 and phi4
- Granite3.2:8b, granite3.3:8b, gemma3:12b-it-qat
