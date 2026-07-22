
## GGUF and safetensor
- Both are file formats for storing model weights, but they target different worlds.
## Safetensor
- **Safetensors** is Hugging Face's format for storing raw tensors safely.
- It replaced pickle-based PyTorch checkpoints (.bin/.pt)
- safetensors is just a JSON header plus raw tensor bytes.

## Notes:
- **tensor** a tensor is just a multi-dimensional array of numbers.
- **pytorch**
	- PyTorch is an open-source library for building and running neural networks, originally developed at Meta.
	- it's the dominant framework in ML research and much of industry. When people "train a model" or "run a model," PyTorch is very often the software actually doing the math underneath.
	- Hugging Face's transformers library is built on top of PyTorch, and safetensors files are how PyTorch-ecosystem weights get stored and shared.
	- llama.cpp, by _contrast_, deliberately avoids PyTorch entirely; it reimplements inference in plain C/C++ so you can run models (from GGUF files) without the whole Python/CUDA stack.
## GGUF 
- **GGUF** is the format used by llama.cpp and everything built on it (Ollama, LM Studio, koboldcpp, etc.).
- It's a single self-contained file: weights plus metadata like the tokenizer, chat template, and architecture parameters, so a runtime can load one file and just work.
- Its defining feature is support for llama.cpp's quantization schemes (Q4_K_M, Q5_K_S, Q8_0, and so on), which shrink models to a fraction of their FP16 size so they run on CPUs and modest GPUs.

## In practice:
- Fine-tuning, serving with vLLM/transformers, GPU inference at full precision: safetensors
- Running locally with Ollama/llama.cpp/LM Studio, especially quantized on limited hardware: GGUF