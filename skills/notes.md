## Skills
 - skills are curated instruction sets; essentially refined prompts and best practices stored as documents that ai agent reads before tackling a task.
 - They don't connect to external services

## MCP vs Skills
- MCP servers expand what the agent can access, while skills improve how the agent performs specific tasks.
- **NOTE** skills may take over the MCP job because you can have a script that does API calls and access external information.

## anthropics skills
- https://github.com/anthropics/skills/tree/main/skills
    - pdf skill: https://github.com/anthropics/skills/tree/main/skills/pdf

### how claude code run scripts in skills?
- Claude Code has access to a bash/shell tool that lets it execute commands directly in a terminal.
- basically, ai agent have access to shell tool that gives models the ability to work inside a complete terminal environment.
- https://developers.openai.com/api/docs/guides/tools-shell

## Notes
- To manage context efficiently: the full SKILL.md instructions only when the agent decides to use a skill.



## resources: 
- https://agentskills.io/home
- https://github.com/agentskills/agentskills
