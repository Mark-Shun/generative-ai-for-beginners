import os
from openai import AzureOpenAI

# azure_endpoint_key = os.getenv("AZURE_OPENAI_ENDPOINT")  # e.g., "https://<your-resource-name>.openai.azure.com/"
# azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
# azure_deployment_key = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # Your deployment name

# print(azure_endpoint_key, azure_api_key, azure_deployment_key)

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model_name = "o3-mini"
deployment = "o3-mini"

subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=str(endpoint),
    api_key=str(subscription_key),
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Which AI model is this service using?"
        }
    ],
    max_completion_tokens=1000,
    model=deployment
)

print(response.choices[0].message.content)