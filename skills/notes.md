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
- view SKILL.md            ← instructions loaded into context
  bash: python script.py   ← script EXECUTES, but its source code is NOT in context
  stdout/stderr returned   ← only the OUTPUT enters context
  - scripts are not loaded into the context. 
  - Only if Claude explicitly reads them, which it would do if:
    - It needs to debug the script and reads it with view
    - The SKILL.md instructs Claude to inspect the script first
    - You ask Claude to explain or modify the script



## resources: 
- https://agentskills.io/home
- https://github.com/agentskills/agentskills
- [what are skills](https://support.claude.com/en/articles/12512176-what-are-skills)

## file structure 

skill-name/
├── SKILL.md              ← required, instructions go here
├── scripts/              ← executable code for repetitive tasks
├── references/           ← docs loaded into context as needed
└── assets/               ← templates, icons, fonts used in output

## claude custom skills
- create a directory containing minimum of:
    - SKILL.md
        - which is the core of the Skill
        - This file must start with a **YAML frontmatterJ** to hold name and description fields, which are required.
        - Required metadata fields:
            - name
            - description
        - Optional metadata fields
            - dependencies
    - Add resources
        - resources can be referenced in the Skill.md
    - Add scripts


## Package your skill
- Ensure the folder name matches your Skill's name
- Create a ZIP file of the folder.
- The ZIP should contain the Skill folder as its root (not a subfolder).
### Correct structure:
my-Skill.zip
  └── my-Skill/
      ├── Skill.md
      └── resources/

# Agent Skills Standers

## https://agentskills.io/what-are-skills

## structure
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources

## How skills work
**Skills use `progressive disclosure` to manage context efficiently:**
1. Discovery: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.
2. Activation: When a task matches a skill’s description, the agent reads the full SKILL.md instructions into context.
3. Execution: The agent follows the instructions, optionally loading referenced files or executing bundled code as needed.

## SKILL.md
- Every skill starts with a SKILL.md file containing YAML frontmatter and Markdown instructions:
```md
    ---
    name: pdf-processing
    description: Extract text and tables from PDF files, fill forms, merge documents.
    ---
    
    # PDF Processing
    
    ## When to use this skill
    Use this skill when the user needs to work with PDF files...
    
    ## How to extract text
    1. Use pdfplumber for text extraction...
    
    ## How to fill forms
```
- The following frontmatter is required at the top of SKILL.md:
    - name: A short identifier
    - description: When to use this skill

## specification (https://agentskills.io/specification)

### Directory structure
- A skill is a directory containing at minimum a SKILL.md file:
```md
skill-name/
└── SKILL.md          # Required
```
### SKILL.md format
- The SKILL.md file must contain `YAML frontmatter` followed by Markdown content.
```md
    ---
    name: pdf-processing
    description: Extract text and tables from PDF files, fill forms, merge documents.
    license: Apache-2.0
    metadata:
      author: example-org
      version: "1.0"
    ---
```
| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen. |
| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.). |
| `metadata` | No | Arbitrary key-value mapping for additional metadata. |
| `allowed-tools` | No | Space-delimited list of pre-approved tools the skill may use. (Experimental) |

- name field
  - The required name field:
     - Must be 1-64 characters
     - May only contain unicode lowercase alphanumeric characters and hyphens (a-z and -)
     - Must not start or end with -
     - Must not contain consecutive hyphens (--)
     - **Must match the parent directory name**

- description field
  - The required description field:
     - Must be 1-1024 characters
     - Should describe both what the skill does and when to use it
     - Should include specific keywords that help agents identify relevant tasks
```md
    compatibility: Requires git, docker, jq, and access to the internet
    
    metadata:
      author: example-org
      version: "1.0"
    
    allowed-tools: Bash(git:*) Bash(jq:*) Read
```

### Body content
- The Markdown body after the frontmatter contains the skill instructions. 
- There are no format restrictions. Write whatever helps agents perform the task effectively. 
- Recommended sections:
  - Step-by-step instructions
  - Examples of inputs and outputs
  - Common edge cases
- Note that the agent will load this entire file once it’s decided to activate a skill. 
    - Consider splitting longer SKILL.md content into referenced files.

### Optional directories
- scripts/
    - Contains executable code that agents can run. Scripts should:
      - Be self-contained or clearly document dependencies
      - Include helpful error messages
      - Handle edge cases gracefully
    - Supported languages depend on the agent implementation. Common options include Python, Bash, and JavaScript.

- references/
    - Contains additional documentation that agents can read when needed:
      - REFERENCE.md - Detailed technical reference
      - FORMS.md - Form templates or structured data formats
      - Domain-specific files (finance.md, legal.md, etc.)
    - Keep individual reference files focused. Agents load these on demand, so smaller files mean less use of context.

- assets/
    - Contains static resources:
      - Templates (document templates, configuration templates)
      - Images (diagrams, examples)
      - Data files (lookup tables, schemas)

### File references
- When referencing other files in your skill, use relative paths from the skill root:
```md
    See [the reference guide](references/REFERENCE.md) for details.
    Run the extraction script:
    scripts/extract.py
```
- Keep file references one level deep from SKILL.md. Avoid deeply nested reference chains.

### Validation
- Use the skills-ref reference library to validate your skills:
    - https://github.com/agentskills/agentskills/tree/main/skills-ref
    - `skills-ref validate ./my-skill`
---
## using scripts in skills:
    - https://agentskills.io/skill-creation/using-scripts
###  One-off commands
- like python or nodejs tools
    - you can reference them directly in your SKILL.md
```md
uvx ruff@0.8.0 check .
uvx black@24.10.0 .
```
### Referencing scripts from SKILL.md
- Use relative paths from the skill directory root to reference bundled files. 
- The agent resolves these paths automatically — no absolute paths needed. 
- List available scripts in your SKILL.md so the agent knows they exist:
```md
    <!-- SKILL.md -->
    ## Available scripts
    - **`scripts/validate.sh`** — Validates configuration files
    - **`scripts/process.py`** — Processes input data
```
- Then instruct the agent to run them in the SKILL.md:
    ```md
      ## Workflow
      1. Run the validation script:
         ```bash
         bash scripts/validate.sh "$INPUT_FILE"
         ``` 
      2. Process the results:
         ```bash
         python3 scripts/process.py --input results.json
         ```
    ```

### Self-contained scripts
- When you need reusable logic, bundle a script in scripts/ that declares its own dependencies inline 

### Designing scripts for agentic use
- When an agent runs your script, it reads **stdout** and **stderr** to decide what to do next. A few design choices make scripts dramatically easier for agents to use.
    - Avoid interactive prompts
        - Accept all input via command-line flags, environment variables, or stdin
    - Document usage with --help
        - --help output is the primary way an agent learns your script’s interface. Include a brief description, available flags
    - Write helpful error messages
    - Use structured output
        - Prefer structured formats — JSON, CSV, TSV — over free-form text. 
        - Structured formats can be consumed by both the agent and standard tools (jq, cut, awk), making your script composable in pipelines.
    - https://agentskills.io/skill-creation/using-scripts#further-considerations


## Good reading:
- https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

