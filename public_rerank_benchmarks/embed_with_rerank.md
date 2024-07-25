| Model | First Stage| BEIR Evaluation (14 Datasets)| Code Evaluation (6 Datasets)| Long Context Evaluation (7 Datasets)| Multilingual (18 Datasets)| Semi-Structured Data Evaluation (5 Datasets)
| -------- | -------- | -------- | -------- | -------- | -------- |  -------- | 
|N/A|embed-v3.0|52.6|65.0|56.8|63.7|47.8
|Rerank v2|embed-v3.0|50.4|50.1|62.8|66.5|62.8
|Rerank v3|embed-v3.0|54.8|64.5|69.3|70.9|62.7

Note: For Multilingual, both we used `embed-multilingual-v3.0`, `rerank-multilingual-v2.0`, and `rerank-multilingual-v3.0`. All other evaluations were done with the english model variants