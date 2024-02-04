import openai 
import requests 
import constants
import json

from tools.tools import tools, get_stock_price


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


def chat_test(messages, tools=tools, maxtokens=500, outputs=1):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=maxtokens,
        n=outputs
    )
    res = response.choices[0].message

    tool_calls = res.tool_calls
    if tool_calls:
        available_functions = {
            "get_stock_price": get_stock_price,
        }
        tool_message = [i for i in messages]
        tool_message.append(res)

        # Depends on questions, it may call the function multiple times
        for tool_call in tool_calls:      
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(ticker=function_args.get("ticker"))

            tool_message.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        second_res = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=tool_message,
                max_tokens=4000, 
                n=1
            )
        return second_res.choices[0].message.content

    else:
        print('check')
        return res.content




