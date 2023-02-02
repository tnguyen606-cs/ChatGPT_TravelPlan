import logging
import openai
import azure.functions as func

secret_key = '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'

# request_body
# {"model":"text-davinci-003", "prompt":"A fruit company", "max_tokens":200, "temperature":0}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(
        'Python HTTP trigger function processed a request for ImageAI.')

    # give OpenAI the secret_key to auth
    openai.api_key = secret_key
    openai.Model.list()

    # get variable from HTTP request body
    req_body = req.get_json()
    logging.info(type(req_body))

    # call OpenAI API
    image_resp = openai.Image.create(
        prompt=req_body['prompt'],
        n=1,
        size="1024x1024"
    )

    # format the response
    image_url = image_resp['data'][0]['url']

    # provide/echo the response
    return func.HttpResponse(image_url, status_code=200)
