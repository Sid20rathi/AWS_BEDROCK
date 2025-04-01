import json
import boto3

prompt_data ="""
Act as a Shakespeare and write a poem on machine learning 

"""

bedrock_client= boto3.client(service_name='bedrock-runtime',
region_name="us-east-1"
)
kwargs={
 "modelId": "us.meta.llama3-1-70b-instruct-v1:0",
 "contentType": "application/json",
 "accept": "application/json",
 "body": json.dumps({"prompt":prompt_data,"max_gen_len":512,"temperature":0.5,"top_p":0.9}),

}






response = bedrock_client.invoke_model(**kwargs)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("generation")
print(response_text)