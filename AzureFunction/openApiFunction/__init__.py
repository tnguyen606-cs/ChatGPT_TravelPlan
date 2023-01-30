import logging
import openai
import azure.functions as func

secret_key = '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'

# request_body
# {"model":"text-davinci-003", "prompt":"Give me a slogan for a fruit company", "max_tokens":200, "temperature":0}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI the secret_key to auth
    openai.api_key = secret_key

    # get variable from HTTP request body
    req_body = req.get_json()
    logging.info(type(req_body))

    # call OpenAI API
    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )

    # format the response
    output_text = output['choices'][0]['text']

    # provide/echo the response
    return func.HttpResponse(output_text,
                             status_code=200)
