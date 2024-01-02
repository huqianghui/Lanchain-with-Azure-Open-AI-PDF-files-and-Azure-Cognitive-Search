Langchain 不同chain type

<img width="423" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/9ac4b37e-06fb-4d75-a140-1a51b334beec">

1.	Stuff
   
1.1 文档说明：Stuff | 🦜️🔗 Langchain

https://python.langchain.com/docs/modules/chains/document/stuff

 ![image](https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/f1fcff02-dc46-4ce7-b4ea-24c1bf2fd53c)

sample code:

https://github.com/langchain-ai/langchain/blob/85dae78548ed0c11db06e9154c7eb4236a1ee246/langchain/chains/qa_with_sources/stuff_prompt.py#L4

1.2	实际使用
需要定义固定的两个变量不是context or docs 而是summary：

<img width="423" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/ee56ff10-2af5-4e1d-baef-1994d996a2ad">

***可以理解为：由于token限制等原因，对document做了summary然后再回答问题。不知道是否会关键信息丢失，在实际使用中，没有遇到这个问题。***


2.	Refine
   
2.1 文档说明Refine | 🦜️🔗 Langchain
https://python.langchain.com/docs/modules/chains/document/refine

 ![image](https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/80c848ba-1b45-4f66-9de3-9fb19487a9b2)


sample code： 

https://github.com/langchain-ai/langchain/blob/85dae78548ed0c11db06e9154c7eb4236a1ee246/langchain/chains/qa_with_sources/refine_prompts.py

https://github.com/langchain-ai/langchain/blob/d85f57ef9cbbbd5e512e064fb81c531b28c6591c/langchain/chains/question_answering/__init__.py#L146

2.2	源码说明：

prompt变成了两个： 

1） question_prompt 

2） refine_prompt

其中refine_prompt 是必须有的， 有三个参数：
["question", "existing_answer", "context_str"]

question_prompt是可选的，是两个参数：
["question", "context_str"]

<img width="334" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/cc912764-c793-419d-b5fa-6abd3cd82bcf">

<img width="468" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/02e188a6-33bb-4d87-a300-bf3e581e17d8">

2.3	实际使用

<img width="836" alt="Screenshot 2024-01-02 at 11 01 40" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/593b1162-da46-4936-8785-52668837f822">

2.4	测试结果
当提供了两个prompt的时候，结果出现变化：

<img width="418" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/fd4ee385-2f48-4cb0-aa31-2652f912a55b">

用后续score低的资源，更新了这个问题。

<img width="400" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/739b956c-529f-4681-8b69-8ce37a9cbed3">

只留下refine_prompt:
<img width="453" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/4767def9-9bc9-494f-8f82-a61d6d289e9d">

3.	Map reduce
Map reduce | 🦜️🔗 Langchain
https://python.langchain.com/docs/modules/chains/document/map_reduce

 ![image](https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/002f2977-9b02-4f73-9e80-075905e76fb1)

sample code:

https://github.com/langchain-ai/langchain/blob/d85f57ef9cbbbd5e512e064fb81c531b28c6591c/langchain/chains/question_answering/map_reduce_prompt.py


4.	Map re-rank
4.1 文档说明Map re-rank | 🦜️🔗 Langchain

 ![image](https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/46189bc2-67d9-4815-8605-cfbf8df1c9ac)


sample code :

https://github.com/langchain-ai/langchain/blob/d85f57ef9cbbbd5e512e064fb81c531b28c6591c/langchain/chains/question_answering/map_rerank_prompt.py

<img width="441" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/aa9e7b15-eb7f-4c4a-8ca4-7f66af14d590">

4.2	实现

<img width="416" alt="image" src="https://github.com/huqianghui/Lanchain-with-Azure-Open-AI-PDF-files-and-Azure-Cognitive-Search/assets/7360524/e527daac-0d3b-4313-abaf-5b0b0001e240">


