

## running mcp with inspector:
- if the script doesn't use `mcp.run()` in the python script  
    - then in inspector run: 
        - command: uv
        - args: --directory /home/safwan/wd_ssd/ai/mcp/first_mcp run --active mcp run simple_mcp.py
- if the script uses `mcp.run()`, then in inspector use:
    - command: uv
    - args: --directory /home/safwan/wd_ssd/ai/mcp/first_mcp run --active weather.py


## notes:
- it's best to drop the --active, and use the .venv managed by `uv`.
- then, to run installed packages use: `uv run <packge-name or script.py>`
- Chat with model and access the tools:
    - `uv run mcp-cli chat --server weather --provider ollama --model llama3.2`

