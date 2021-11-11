# Artice Indexing and Text Summarization with Jina AI
Legit info in a nutshell !

- Give a keyword and the summary length, and the headlines of the articles are searched based on that keyword and the top 5 article links are brought up by Jina AI neural search.

- The topmost link is summarized by the pretrained model(t5) from Huggingface, and it returns an extractive summary of the article.

- Application: Top 5 articles and an extractive summary is generated for the respective keyword given by the user.

- Custom Dataset, scrapped using BeautifulSoup and Selenium: Article_dataset - Sheet1.csv

Article Topics:

    - AWS
        IAM Cred Report
        S3 101
        Database 101
        AWS Compliance and Security
        Shared Responsibility model
        AWS WAF and Shield
        AWS Inspector vs AWS Trusted Advisor
        Cloudwatch vs AWS Config
        Trusted Advisor 
        S3 CLI
        EFS
        Lambda
        EC2
        RDS
        Postgres, Aurora, DynamoDB, MySQL
        Autoscaling
        Cloudwatch
        S3 versioning
        Creating S3 bucket
        Creating a website on S3
        Service Health Dashboard
        Personal Health Dashboard
        S3 vs EBS vs EFS
        Global accelerator
        Consolidated Billing & AWS Organizations   
        Identity Access Management(IAM)
        EC2 101
    - Azure
    - GCP
    - Maching Learning (Intro)
    - Deep Learning(Intro)


## Links:

https://medium.com/jina-ai/multimodal-search-demo-in-detail-b2c21a5a21a1

https://github.com/google/sentencepiece#installation

https://huggingface.co/transformers/model_doc/xlnet.html

https://pypi.org/project/newspaper3k/

https://huggingface.co/sshleifer/distilbart-cnn-12-6

https://huggingface.co/t5-base

## Technology Stack

| Technology  | 
|-------------|
| HTML5       |
| CSS3        | 
| Python      | 
| Transformers|                                          
| Jina|               
| Pandas|  
| Numpy|
|newspaper3k  |
|sentencepiece|
|Selenium|
|BeautifulSoup|
|torch|

## Running

To test the application run the following commands on your terminal:

**Running the application locally:**


```
pip install -r requirements.txt
```

```
python app.py
```

![s7](https://user-images.githubusercontent.com/82106569/141140456-5b0b3117-5146-4f31-846f-94976d4c2525.png)

![s6](https://user-images.githubusercontent.com/82106569/141140551-a5fc449c-7d41-4c8f-8155-0ec734f866cc.png)


