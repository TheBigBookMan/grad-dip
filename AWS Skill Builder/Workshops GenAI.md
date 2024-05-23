## Sagemaker
- Working on models straight off the shelf
- sagemaker offers more finetuned models than bedrock
- a lot easier for doing the sentiment model and keeping notes, tracking etc and practicing it all
- good for these model pipelines
- can store multiple modals based on different weight trainings etc
- important to have a data training pipeline AND an inference pipeline
- Sagemaker Python SDK is better than Boto3 for using sagemaker in python
- canvas for no-code low-code
- studio is for more notebooks- more for data analystics then???
	- Good for labeling data as well
	- preparing data
	- data training for models
-![[Pasted image 20240516111751.png]]

## Bedrock
- gen ai is nondeterminitic and responses will most likely be different most of the time
- no real explanation for why
- proprietry models are usually economical for small-medium usage, hard to fine tune (Claude, Cohere, Titan)
- Open source models good for fine-tuning (Mixtral, Llam2, flacon)
- maybe using some models through sagemaker is better as there are more range on sagemaker for the sentiment analyser for multi context
- prompt engineering-
	- good to write down results for prompts for specific use cases/models etc
	- have to be super specific and very clearly write what you want it to achieve
	- important to assign the chatbot an identity as this could make it perform better
	- Use XML tags for tagging--- look into more
	- use example (in-context learning) for providing a good way to show it the best way of responding
	- importance of the system prompt
	- be clear and direct
		- "Only return positive or negative"
	- assign roles
		- "You are a high level AI assistant designe to classify text into negative or positive"
		- privide a context
	- separate data and instructions
		- ![[Pasted image 20240523133758.png]]
	- fe-showt prompting
		- ![[Pasted image 20240523133829.png]]
	- Dealing with hallucinations
		- ![[Pasted image 20240523133859.png]]
- Agents
	- uses the power of LLMs to orchestrate tasks
	- create a JSON/YAML with API instructions that will determine what actions the query will take
- Security-
	- 


![[Pasted image 20240523103754.png]]