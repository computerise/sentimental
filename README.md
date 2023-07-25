# sentimental

## Summary

The qualitative analysis component of a [Value Investing](https://www.investopedia.com/terms/v/valueinvesting.asp) approach. Apply natural language models to perform sentiment analysis on publicly-traded securities.

## Method

1. Employ an open source [Large Language Model (LLM)](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/) like [LLaMA2](https://github.com/facebookresearch/llama) to review articles from business and financial reporters.

2. Using the model, score the sentiment in historical reports and articles towards various [quantitatively-filtered](https://github.com/computerise/stonks/) companies and compare the sentiment to historical stock performance.

3. Sources with the highest correlation between sentiment score and share price over time become **trusted sources**; the remainder become **candidate sources**.

4. Apply the algorithm to recent articles and reports from all sources and to obtain current sentiment towards the company stocks.

5. Iteratively reassess the source lists based on actual performance of the stocks by promoting candidate sources that outperformed trusted sources.

6. The sentiment scores, in conjunction with a quantitative evaluation of each company are used to assess the likelihood of stocks being over- or under-valued by the market.

7. Profit?

8. Repeat steps 4-8.
