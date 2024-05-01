https://www.youtube.com/watch?v=sVcwVQRHIc8

## Query Translation
- Queries are ambigious can be poorly written and not return results wanted
- **Transform questions**- these work well with parralellized retrieval based on the question given
	- query rewriting- reframing query. writing from different perspective, so if the hit score on the retrieval is very poor, then it could wrte to an LLM with a prompt "rewrite this query into different perspectives so it may search better", returns maybe 5 differently worded queries that are similar and then multiple perspectives will be sent out to find the document through concurrent opensearch queries--- all answers are then collected in the prompt context so the answer can be found to the first question from the llm
	- break down questions- sub questions within it, break down by the question marks or periods, or ask the LLM to break it down into sub queries of what it thinks would be
	- abstraction- make the question more abstract 
	- **Parallelized retrieval**- do multiple retrievals and then perform rag on differetne 
		- Split the document database iinto multiple segments (certain criterias etc)--- maybe apps or specific area (workers, carers, timesheets, location rosters)
		- concurrent queries- search multiple areas independently and each segment handles a part of the query independently- so like subqueries from the query (if very long)- maybe good if there are multiple Question marks in the question or if it exceeds word length????
		- aggregataion of results- results aggreagated and mut consider relevance scores, ensuring most relevant documents are present irrespective of segment they came from
		- Better for queries that contain multiple questions that don't rely on each others answers (refer to chain of thought below)
	- **RAG Fusion**- generating multiple search queries based on user queries (similar to as above)
		- Related to more deep learning and how the document searching process can be a lot better
		- Good for specifying the doument better
		- need to look in more
	- **Decomposition**- similar to the query break down and parallelized retrieval so when there are multiuple questions in the one query
		- **Interleave retrieval with Chain-of-thought**- building up solutionms based on the chain of throught gathered from previous answers. Good for questions that rely on each other within the query
			- It answers the first question based on the document given 
			- that question and answer from the first prompt is then given as "additional info" into the second prompt along with the second query and context documentation given back by that retrieval and then given a response which would be more related to that first question
			- Continues this process with how ever many query questions there are, so rather than the queryies being broken down separately and then all the contexts are added together at the end
			- This concatenates each one with the context from bnefore, before getting more context, so it kind of blends in together easier
	- **Step-Back**- making the question more abstract
		- so if a query is too specific then it may not be best suited in finding a document, so making a prompt to make it a bit more abstract and broader so it can be found better
		- this could add more key words into the new prompt
		- "you need to paraphrase this question and make it more generic"
		- creating a more generic question which is easier to answer
		- give the normal context and then the step back context and it can then find the answer from both and combine both
		- could be good for if someone questions "how do i make a roster from the 23rd of march to the 28th of march for my client", can make it to be more abstract like "how to make a roster for a client"- which would be a lot easier fo opensearch to find
	- **HyDE**- 
		- simpele flow takes a document and embeddes it and then takes an embedded question and compares it to the embedded document
		- creates a hypothetical document based on general knoweldge and then uses that in tandem with the question and the context brought back by the search query to find the response
		- Good for helping with general knowledge, but not ideal when the knoweldge base is something super specific and general knoweldge from the outside world won't help

## Routing
- logical or semantic routing
- routing the decomposed question to the right source, which could be a different database (relevant data source)
- **Logical routing**- give LLM knoweldge of the various datasources and let LLM determine which one to send the question to- applies logic to it
	- give the llm the names of the datasources with information that can be a set of rules that describe what information could be in those data sources or not in the data sources
	- a classification that can produce a structured output which then will determine what functions get called (opensearch, database call etc)
	- for example have data sources- documents (opensearch), clientInfo (MySQL), notes (MongoDB) and the query can then determine what is best for the task- eg 'how do i create a client?' (documents- opensearch); 'how old is Jane Doe?' (clientInfo- MySQL)
	- can have the LLM use a **function schema** where the LLM which execute a function within the response- to return maybe JSON of the data source wanting to be used
- **Semantic routing**- embed the question and embed prompts, compute the similarity between the question and prompt and then choose a prompt based on the similarities of the question to the prompt
	- embedding the different prompts you could have and then embedding the question and seeing similarities between the embeddings and returning the highest score prompt with the query 