
## Instructlab
- On github: https://github.com/instructlab/instructlab
- On huggingface: https://huggingface.co/instructlab

Key Features:

- ilab Command-Line Interface (CLI): Allows users to interact with, train, and fine-tune LLMs using custom taxonomy data. The CLI supports various platforms including macOS, Fedora Linux, and Windows.
- Synthetic Data Generation: Enhances LLM training through the creation of synthetic datasets.
- Taxonomy Repository: A structured repository where users can submit and manage their contributions of skills and knowledge.

## Download model from hugging face:
```bash
#you need to get token first
#HF_TOKEN=<YOUR HUGGINGFACE TOKEN GOES HERE> ilab model download --repository=TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF --filename=mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf
ilab model download --repository=instructlab/granite-7b-lab-GGUF --filename=granite-7b-lab-Q4_K_M.gguf
```

