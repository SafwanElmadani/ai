watsonx.ai platform: https://dataplatform.cloud.ibm.com/wx/home?context=wx
from here:
- click on project
- switch tab to assets.
- then click on new tasks.
Log in to IBMCloud: https://cloud.ibm.com/login

get apikey: https://cloud.ibm.com/iam/apikeys


watson assistant: go to ibm cloud https://cloud.ibm.com/login and launch ibm assistant service from the Resource list under AL/ML subgroup.
demo watch: https://www.ibm.com/products/watson-assistant/demos/lendyr/demo.html?page=generative-ai-tour&section=generative-ai&panel=generative-conversational-search
embedding the chat in a web page: https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-deploy-web-chat




good overall pic: https://w3.ibm.com/services/lighthouse/videos/115092

watsonx platform (what goes into it) very useful: https://ibm.seismic.com/app?ContentId=84ed761e-82b9-4fd5-bbd7-58750f13849f#/doccenter/5477419a-9474-4c51-94af-b442e9169fab/doc/%252Fdd98c5a3df-6b7c-1d77-6f07-d12e63954c78%252FdfOTRiYmU4NTQtNWY4NC03Y2QyLWZjYWUtOGIxYmFmZjkyZThk%252CPT0%253D%252CUHJvZHVjdC9Tb2x1dGlvbiBCcmllZiBvciBHdWlkZQ%253D%253D%252Flfd5f543ea-ec03-433a-be31-833089d7bdd6/grid/
[Click this link and skip to 9:45 mins into the video and watch until 29:30](https://ibm.seismic.com/app?ContentId=84ed761e-82b9-4fd5-bbd7-58750f13849f)



![[Pasted image 20230730232352.png]]




![[Pasted image 20230731082745.png]]



![[Pasted image 20230731130005.png]]


What are we trying to do? classification 
We need to label out data?
connect watson assistant WA with other models: https://github.com/watson-developer-cloud/assistant-toolkit/tree/master/integrations/extensions/starter-kits/neuralseek
As I understand it, what NeuralSeek does is:
1. Takes in the query _and_ the full conversation context
2. Searches for relevant documents in Watson Discovery
3. Feeds those documents plus the context and the query to GPT3 to get an answer
4. Returns the answer along with the link to the top document and a confidence score








-------
This is a typical flow for answering questions with an LLM from documents. I am sharing it in the main channel for other hackathon participants who may find it usefu


![[Pasted image 20230806180635.png]]


Connect watsonx to the assistant: https://github.com/watson-developer-cloud/assistant-toolkit/tree/master/integrations/extensions/starter-kits/language-model-watsonx
deployment: https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-web-chat-overview

assistant integration: https://github.com/watson-developer-cloud/assistant-toolkit/tree/master/integrations/webchat/examples
