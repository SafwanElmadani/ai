
## Model labels (base, instruct, chat):
- Base: Text completion - i,e. feed the model uncompleted text and it will try to predict the next words.
    - Base models are foundational models, which do not respond in QA formet.
- Instruct: Asking the LLM a question or task (single turn) - e.g. ask the model to code a snake game and it will 'answer' with a response.
    - Instruct models are models, which were finetuned on QA.
- Chat: Multi-turn conversion - The model is finetuned for conversations where user and LLM respond to each other back and forth.
    - Chat models are models, which were finetuned on multiturn dialogue.

Though there isn't anything stopping you from using instruct and base models for chatting except you will just get worse performance since those versions aren't finetuned for that purpose.

