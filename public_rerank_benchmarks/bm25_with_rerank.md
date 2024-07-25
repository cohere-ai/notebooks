| Model | First Stage| BEIR Evaluation (14 Datasets)| Code Evaluation (6 Datasets)| Long Context Evaluation (7 Datasets)| Multilingual (18 Datasets)| Semi-Structured Data Evaluation (5 Datasets)
| -------- | -------- | -------- | -------- | -------- | -------- |  -------- | 
|N/A|BM25|43.7|34.0|54.6|36.5|47.5|
|Rerank v2|BM25|49.4|37.6|63.1|59.6|59.7|
|Rerank v3|BM25|53.1|51.7|69.0|62.8|60.3|

Note: For Multilingual, both we used `embed-multilingual-v3.0`,  `rerank-multilingual-v2.0`, and `rerank-multilingual-v3.0`. All other evaluations were done with the english model variants