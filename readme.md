# AWS Bedrock Text Generation

This project demonstrates how to use AWS Bedrock to generate creative text content using pre-trained large language models (LLMs) through the AWS Python SDK (boto3).

## Overview

AWS Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies through a unified API. This project shows how to invoke Meta's Llama 3 model to generate Shakespearean-style poetry about machine learning.

## Prerequisites

- Python 3.6+
- AWS account with access to AWS Bedrock
- AWS credentials configured
- Required Python packages:
  - boto3
  - json (standard library)

## Setup

1. Ensure you have AWS credentials configured with appropriate permissions for AWS Bedrock.
2. Install the required Python packages:

```bash
pip install boto3