
## subagents 
- reference:
    - https://code.claude.com/docs/en/sub-agents#
- Subagents are specialized AI assistants that handle specific types of tasks. 
- Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions.
- Subagents work within a single session
- benefits:
    - Preserve context by keeping exploration and implementation out of your main conversation
    - Enforce constraints by limiting which tools a subagent can use
    - Reuse configurations across projects with user-level subagents
    - Specialize behavior with focused system prompts for specific domains
    - Control costs by routing tasks to faster, cheaper models like Haiku
- Claude uses each subagent’s description to decide when to delegate tasks. 
    - When you create a subagent, write a clear description so Claude knows when to use it.

## agent teams
- reference:
    - https://code.claude.com/docs/en/agent-teams
- Agent teams let you coordinate multiple Claude Code instances working together.
- One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results
- Teammates work independently, each in its own context window, and communicate directly with each other
- Unlike subagents, which run within a single session and can only report back to the main agent, you can:
    - interact with individual teammates directly without going through the lead.
> NOTE: Agent teams add coordination overhead and use significantly more tokens than a single session
- control agent team:
    - Tell the lead what you want in natural language. 
        - It handles team coordination, task assignment, and delegation based on your instructions.


### Notes:
- team agents work best when teammates can operate independently.
- For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.

| Feature | Subagents | Agent Teams |
|---|---|---|
| **Context** | Own context window; results return to the caller | Own context window; fully independent |
| **Communication** | Report results back to the main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |


