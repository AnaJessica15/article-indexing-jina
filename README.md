# Artice Indexing and Text Summarization with Jina AI

- Give a keyword and the summary length, and the headlines of the articles are searched based on that keyword and the top 5 article links are brought up by Jina AI neural search.

- The topmost link is summarized by the pretrained model(t5) from Huggingface, and it returns an extractive summary of the article.

- Application: Top 5 articles and an extractive summary is generated for the respective keyword given by the user.

- Custom Dataset, scrapped using BeautifulSoup and JinaAI: Article_dataset - Sheet1.csv

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

## Running

To test the application run the following commands on your terminal:

**Running the application locally:**


```
pip install -r requirements.txt
```
```
python app.py
```

![epitome1](https://user-images.githubusercontent.com/82106569/141131137-747badd0-51c4-4bd4-b528-a23608bbf955.jpeg)

![ss3](https://user-images.githubusercontent.com/82106569/141131226-8d4a34e7-41ff-483d-b399-65ad2801cc3a.png)

![s5](https://user-images.githubusercontent.com/82106569/141138781-4b63200f-c9b5-4ee3-9164-0c8a445bb8e0.png)


