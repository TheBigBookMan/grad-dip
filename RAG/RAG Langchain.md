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
- **RAG Fusion**- 