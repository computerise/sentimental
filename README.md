# sentimental

## Summary

The qualitative analysis component of a Value Investing approach. Apply natural language models to perform sentiment analysis on publicly-traded securities.

## Method

1) Train the algorithm on financial and business language from a wide array of financial journalists and reports, or use an open source Large Language Model (LLM) like LLaMA2.

2) Using the model, score the sentiment in historical reports and articles towards various [quantitatively-filtered](https://github.com/computerise/stonks/) companies and compare the sentiment to historical stock performance.

3) Sources with the highest correlation between sentiment score and share price over time become **trusted sources**; the remainder become **candidate sources**.

4) Apply the algorithm to recent articles and reports from all sources and to obtain current sentiment towards the company stocks.

5) Iteratively reassess the source lists based on actual performance of the stocks by promoting candidate sources that outperformed trusted sources.

6) Profit?

7) Repeat steps 4-7.
