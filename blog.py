import boto3
import botocore.config
import json
from datetime import datetime

def blog_generator(blogtopic:str)->str:
    prompt=f"""
    <s>[INST]Human:Write a 300 words blog about {blogtopic}
    Assistant:[/INST]

    """
    kwargs={
        "modelId": "us.meta.llama3-1-70b-instruct-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({"prompt":prompt,"max_gen_len":512,"temperature":0.5,"top_p":0.9}),

        }
    
    try:
        bedrock_client= boto3.client(service_name='bedrock-runtime',
        region_name="us-east-1",
        config=botocore.config.Config(
            read_timeout=500,
            retries={'max_attempts':3}
            )
        )
        response = bedrock_client.invoke_model(**kwargs)
        response_content = response.get('body').read()
        response_data=json.loads(response_content)
        print(response_data)
        blog_details = response_data['generation']
        return blog_details
    except Exception as e:
        print(f"Error in generating the blog:{e}")
        return " "



def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket,key=s3_key,Body=generate_blog)

    except Exception as e:
        print(f"Error in saving the blog to s3:{e}")
        return " "




def lambda_handler(event, context):
    event = json.loads(event['body'])
    blogtopic = event['blog_topic']

    generate_blog = blog_generator(blogtopic=blogtopic)
    
    if generate_blog:
        current_time=datetime.now().strftime("%H:%M:%S")
        s3_key=f"blog-output/{current_time}.txt"
        s3_bucket='aws_bedrock'
        save_blog_details_s3(s3_key,s3_bucket,generate_blog)
    else:
        print("Error in generating the blog")
        return response.response(400, "Error in generating the blog")

    return{
        'statusCode':200,
        'body':json.dumps('Blog generated successfully')
    }


