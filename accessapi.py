import openai
secret_key = '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'
prompt = 'tell me my billing this month'

# Call openai
openai.api_key = secret_key

# create a complete response based on the prompt
output = openai.Completion.create(
    # what model we use?
    model='text-davinci-003',
    prompt=prompt,
    # The max tokens that openAI can give to me? how many characters?
    # 1 token ~= 4 chars, 100 tokens ~= 75 words
    max_tokens=2,
    temperature=0
)

print(output)
