
## Model Context Protocol (MCP)
- It's a protocol that gives LLMs access to external resources. LLMs can integrate and share data with external tools, systems and data sources. 
- It's like an API for LLMS.
- MCP uses server-client architecture

## MCP server:
- An MCP server is like a smart adapter for a tool or app. It knows how to take a request from an AI (like “Get today’s sales report”) and translate it into the commands that tool understands.
- For example:
    - A GitHub MCP server might turn “list my open pull requests” into a GitHub API call.
    - A File MCP server might take “save this summary as a text file” and write it to your desktop.
    - A YouTube MCP server could transcribe video links on demand.
- Tell the AI what they can do (tool discovery)
- Interpret and run commands

## MCP Clients
On the other side, an MCP client lives inside the AI assistant or app (like Claude or Cursor). When the AI wants to use a tool, it goes through this client to talk to the matching server.
- Cursor can use a client to interact with your local development environment.
- The client handles all the back-and-forth — sending requests, receiving results, and passing them to the AI.
- Client for testing the server:
    - https://github.com/modelcont`extprotocol/inspector

## The MCP Protocol
The MCP protocol is what keeps everything in sync. It defines how the client and server communicate — what the messages look like, how actions are described, and how results are returned

## SDKs
- https://github.com/modelcontextprotocol

## Docs
- https://modelcontextprotocol.io/introduction

## MCP (Model Context Protocol) defines these transports:

1. stdio — Server runs as a local subprocess; client and server exchange JSON-RPC messages over stdin/stdout. Used
for local tools (e.g., a local filesystem or git MCP server).
2. Streamable HTTP — The current standard remote transport. A single HTTP endpoint handles JSON-RPC requests; the server can optionally upgrade responses to Server-Sent Events to stream multiple messages or push notifications back. Replaced the older HTTP+SSE transport.
3. HTTP + SSE (legacy) — The original remote transport: a POST endpoint for client→server messages plus a separate SSE endpoint for server→client messages. Deprecated in favor of Streamable HTTP but still supported by some implementations for backward compatibility.


## MCP Architecture
MCP (Model Context Protocol) is an open protocol standardizing how LLM apps connect to external tools and data. Think "USB-C for AI": one protocol, many integrations.
## Three roles
Host — the application the user runs. Owns the LLM, manages clients, enforces permissions.
Client — lives inside the host. One client per server, 1:1. Handles the connection and protocol bookkeeping.
Server — the integration. Exposes capabilities (tools, data, prompts) for one service. Runs as a separate process or remote endpoint.
Key point: host can hold many clients, each wired to one server. Servers do not talk to each other.

## Transports
How client and server exchange bytes:
**stdio** — server is a local subprocess; client writes JSON-RPC on stdin, reads stdout. Used by sct-mcp over SSH. No port, no auth layer beyond the shell.
**Streamable HTTP** — server is a remote endpoint over HTTP, uses Server-Sent Events for streaming. For hosted/networked servers. Auth via OAuth.
__Wire format both ways: JSON-RPC 2.0 (requests, responses, notifications).__

## Server primitives (what a server exposes)

| Primitive | Who controls | Purpose                                                                               |
| --------- | ------------ | ------------------------------------------------------------------------------------- |
| Tools     | model-driven | Functions the LLM can call (e.g. `sct_run`). Have side effects.                       |
| Resources | app-driven   | Read-only data the host loads into context (files, DB rows, docs). Identified by URI. |
| Prompts   | user-driven  | Pre-written templates/workflows the user invokes (e.g. slash commands).               |
## Lifecycle
initialize — client and server exchange protocolVersion and capabilities. Negotiation.
initialized notification — handshake done.
Operation — tools/list, tools/call, resources/read, etc.
Shutdown — transport closes.


## stdio
Client (inside host) launches the server as a child process. The pipes are the channel: