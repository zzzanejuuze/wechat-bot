import openai 
import requests 
import constants


#os.environ["OPENAI_API_KEY"] = constants.APIKEY
openai.api_key = constants.APIKEY

# Text generation
def gpt(PROMPT, max_tokens=500, outputs=1):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=PROMPT,
        max_tokens=max_tokens,
        # number of outputs generated in one call
        n=outputs          
    )
    res = response['choices'][0]['text'].strip()
    return res


# Chat
def chat(message, maxtokens=500, outputs=1):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,#[{"role": "user", "content": message}],
        max_tokens=maxtokens,
        n=outputs
    )
    res = response.choices[0].message.content
    #tokens_used = response.usage.total_tokens         # prompt_tokens, completion_tokens, total_tokens

    return res


# Generate image
def generate_img(PROMPT):
    res = openai.images.generate(
        model="dall-e-2",          # 图片生成模型，可选 dall-e-2, dall-e-3
        prompt=PROMPT,
        size="256x256",            # 图片大小,可选有 256x256, 512x512, 1024x1024 (dall-e-3默认为1024x1024)
        quality="standard",
        n = 1,

    )
    url = res.data[0].url
    response = requests.get(url, stream=True)
    with open("bot_draw_img.jpg", "wb") as f:
        f.write(response.content)




