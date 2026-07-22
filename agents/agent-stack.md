	# Agent Stack: Clients & Model Runtimes

A guide to the two layers you choose when building an LLM agent: the **client/SDK** (how your code talks to a model) and the **model runtime** (what actually serves the model).

---

## 1. Client / SDK Options

The library your application code uses to send requests and run the agent loop.

| Client | Layer | Best for | Notes |
|---|---|---|---|
| **OpenAI SDK** (`openai`) | Thin client | Direct control, local runtimes | De facto standard. Works with any OpenAI-compatible endpoint by changing `base_url`. |
| **Anthropic SDK** (`anthropic`) | Thin client | Claude models, reliable tool calling | Native API, richer features than the compatibility shim. |
| **Google GenAI SDK** (`google-genai`) | Thin client | Gemini models | Long context, native API. |
| **LangChain** | Framework | Most tutorials, large ecosystem | Heavy abstractions; hides the agent loop. Most-used, also most-criticized. |
| **LangGraph** | Framework | Production agents, explicit graphs | Where serious LangChain users go now. Memory, checkpoints, streaming built in. |
| **LlamaIndex** | Framework | RAG-heavy agents | Strong for retrieval + indexing. |
| **Pydantic AI** | Framework | Type-safe, clean agents | Newer, rising fast. Lighter than LangChain. |

**Rule of thumb:**
- Want full visibility + minimal deps → **bare SDK** (OpenAI/Anthropic).
- Want memory/streaming/graphs without plumbing → **LangGraph** or **Pydantic AI**.
- Want most copy-paste help available → **LangChain**.

---

## 2. Model Runtime Options

What actually loads weights and serves inference. Most expose an **OpenAI-compatible API**, so the client code stays the same.

### Local runtimes (run on your hardware)

| Runtime       | Best for                | Notes                                                                |
| ------------- | ----------------------- | -------------------------------------------------------------------- |
| **Ollama**    | Easiest local start     | One command to pull + run. Ships OpenAI-compatible API on `:11434`.  |
| **llama.cpp** | Max control / low level | The engine Ollama wraps. `llama-server` gives OpenAI-compatible API. |
| **LM Studio** | Desktop GUI             | Model browser + local server.                                        |
| **vLLM**      | GPU serving, many users | Production-grade, high throughput.                                   |
| **llamafile** | Zero install            | Model + runtime in a single executable.                              |
| **Jan**       | Offline desktop app     | Open-source, OpenAI-compatible server.                               |
| **GPT4All**   | CPU-only, simple        | Runs without GPU.                                                    |
| **KoboldCpp** | Long context / creative | llama.cpp fork.                                                      |

### Cloud providers (no local hardware)

| Provider | Best for | Notes |
|---|---|---|
| **Anthropic (Claude)** | Reliable agents, tool calling | Native + OpenAI-compatible. |
| **OpenAI** | Largest ecosystem | Native API your code already targets. |
| **Google Gemini** | Long context | Competitive pricing. |
| **Groq** | Speed | Very fast inference of open models. OpenAI-compatible. |
| **Together / Fireworks / DeepInfra** | Cheap open models | Hosted Llama/Qwen/etc. OpenAI-compatible. |
| **OpenRouter** | One API, many models | Routes to many providers. |

---

## 3. Why Swapping Is Easy

Most runtimes speak the **OpenAI-compatible API**. Switching providers = change 3 values, agent loop untouched:

```python
from openai import OpenAI

# Ollama (local)
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# vLLM (local GPU)
client = OpenAI(base_url="http://localhost:8000/v1", api_key="x")

# Groq (cloud)
client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key="gsk_...")

# Same call everywhere:
resp = client.chat.completions.create(model="...", messages=[...], tools=[...])
```

---

## 4. Architecture

The stack is layered. Each layer is swappable without touching the others.

```
┌─────────────────────────────────────────────────────────────┐
│                      YOUR APPLICATION                         │
│              (CLI, web app, script, service)                 │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       AGENT LOOP                             │
│   1. send messages + tool schemas to model                  │
│   2. model returns answer OR tool_calls                     │
│   3. if tool_call → run tool → append result → loop         │
│   4. if answer → return, exit                               │
│                                                             │
│   (you write this, OR a framework runs it for you)          │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     CLIENT / SDK                            │
│        OpenAI SDK · Anthropic SDK · LangGraph · ...         │
│         (formats requests, parses responses)                │
└───────────────────────────┬─────────────────────────────────┘
                            │   HTTP (OpenAI-compatible JSON)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     MODEL RUNTIME                           │
│   LOCAL:  Ollama · llama.cpp · vLLM · LM Studio             │
│   CLOUD:  OpenAI · Anthropic · Groq · OpenRouter           │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                        MODEL                               │
│         qwen2.5 · llama3.1 · gpt-4 · claude · ...           │
└─────────────────────────────────────────────────────────────┘

       TOOLS  ◄──── called by the agent loop ────►  get_weather()
                                                     search_web()
                                                     run_sql()
```

### Data flow (one turn)

```
User question
   │
   ▼
Agent loop ──► Client SDK ──► Runtime ──► Model
                                            │
                            "call get_weather(city=Tokyo)"
                                            │
   ┌────────────────────────────────────────┘
   ▼
Agent runs get_weather("Tokyo") → "22C, clear"
   │
   ▼
Append result, loop again ──► Model ──► "Tokyo is 22C and clear."
                                            │
                                            ▼
                                      Final answer to user
```

---

## 5. Picking a Stack

| Goal | Client | Runtime |
|---|---|---|
| Learn / prototype locally | OpenAI SDK | Ollama |
| Full control, understand every step | OpenAI SDK | llama.cpp or Ollama |
| Production agent, self-hosted GPU | LangGraph / Pydantic AI | vLLM |
| Most reliable agent, no hardware | Anthropic SDK | Anthropic (Claude) |
| Cheap + fast open models, no hardware | OpenAI SDK | Groq or OpenRouter |
| RAG-heavy app | LlamaIndex | any |

**Key takeaway:** the OpenAI-compatible API decouples client from runtime. Develop against Ollama locally, switch `base_url` to a cloud provider for production, ship the same agent code.

## Techniques for domain specific agents:

Domain expertise rarely comes from picking a special model. It comes from how you inject domain knowledge into a general model.

| Level | Technique                                 | When it's enough                                                                                                          |
| ----- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1     | **System prompt + few-shot examples**     | Domain fits in a few pages of instructions (tone, terminology, procedures)                                                |
| 2     | **RAG** (retrieve domain docs per query)  | Knowledge is large, changes often, or must be citable (manuals, regulations, internal wikis)                              |
| 3     | **Tools** (calculators, DB queries, APIs) | Expertise = doing things correctly, not just knowing facts                                                                |
| 4     | **Fine-tuning** (LoRA on an open model)   | Model must internalize style/jargon/reasoning patterns that prompting can't capture, or you need a small cheap specialist |
| 5     | **Distillation / domain pretraining**     | You're at serious scale; teacher model generates domain data to train a small student                                     |
