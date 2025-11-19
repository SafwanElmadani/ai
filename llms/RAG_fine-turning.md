

## RAG vs Fine tuning

### retrieval augmented generation (RAG):
- Connects the LLM to an external, up-to-date knowledge base (e.g., your company's documents or a live database) at query time.

## fine tuning:
- Further trains a pre-trained LLM on a small, high-quality, task-specific dataset, modifying the model's internal weights and parameters.

## key differences
- Rag for knowledge, fine tuning for getting it to learn patterns 
- fine tuning is for training the model on specific tasks, whereas RAG is about providing specific information for the model to draw from when answering questions 
- RAG is the default answer. Primarily because fine tuning is time consuming and expensive. You'll also need high quality data for fine tuning. 
