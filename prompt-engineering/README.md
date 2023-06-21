# Bleach

Practical example to showcase some prompt engineering techniques. Preprocess customer service chats using GPT-4 through the OpenAI API.

## Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key
```

You can generate your [API key](https://platform.openai.com/account/api-keys) in your OpenAI account settings.

Move the `.env` file into the `src/bleach/` package folder.

## Install

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Then install the dependencies and the `bleach` package locally:

```bash
(venv) $ python -m pip install openai python-dotenv
(venv) $ python -m pip install .
```

## Usage

```bash
(venv) $ python -m bleach --help
usage: bleach [-h] [--file FILE]

Clean chat text with OpenAI's API

options:
  -h, --help   show this help message and exit
  --file FILE  Path to file with text
```

Read support chat content from a file, sanitize the text, classify by sentiment, and format as JSON:

```bash
(venv) $ python -m bleach --file support-chat.txt
```

## Prompts And Output

I want to show how developing the prompt can give you better results based on a couple of prompting techniques.
Change any of the prompts from `instructions_x` to `instructions` to run the script including the prompt.

### Step 1: Plain Prompt

```toml
instructions_1 = """
Remove personally identifyable information, only show the date, and replace all swear words with "😤"
"""
```

**Output** is already pretty good!

```
2022-08-24 : What can I help you with?
I CAN'T CONNECT TO MY 😤 ACCOUNT
Are you sure it's not your caps lock?
😤! You're right!

...

2022-09-15 : Good evening! How may I assist you?
Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.
I'm sorry to hear that. Let me help you. Can you please confirm your email address?
Sure.

2022-09-24 : Welcome! What can I do for you today?
Hi, I need to change my delivery address for my recent order.
Alright. Please provide your order number.
It's 3344556. Thanks for your help!
```

### Step 2: Delimiters And Step Instructions

```toml
instructions_2 = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Remove personally identifyable information by replacing names in [] with "Agent" and "Client", respectively
2. Replace the date-time information to only show the date in the format YYYY-mm-dd
3. Replace all swear words with the following emoji: "😤"
"""
```

**Output** is more specific, but doesn't replace an email address:

```
[Agent] 2022-08-24 : What can I help you with?
[Client] 2022-08-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2022-08-24 : Are you sure it's not your caps lock?
[Client] 2022-08-24 : 😤! You're right!

...

[Agent] 2022-09-15 : Good evening! How may I assist you?
[Client] 2022-09-15 : Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.
[Agent] 2022-09-15 : I'm sorry to hear that, Client. Let me help you. Can you please confirm your email address?
[Client] 2022-09-15 : Sure, it's sara.winters@email.com.

[Agent] 2022-09-24 : Welcome! What can I do for you today?
[Client] 2022-09-24 : Hi, I need to change my delivery address for my recent order.
[Agent] 2022-09-24 : Alright, Client. Please provide your order number.
[Client] 2022-09-24 : It's 3344556. Thanks for your help!
```

### Step 3: Increase the Steps for More Specificity

```toml
instructions_3 = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace names in [] with "A", for Agent, and "C", for Client, respectively
2. Replace any other personally identifyable information, such as names or email addresses
3. Replace the date-time information to only show the date in the format YYYY-mm-dd
4. Replace all swear words with the following emoji: "😤"
```

**Output** tackles the email address:

```
[A] 2022-08-24 : What can I help you with?
[C] 2022-08-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[A] 2022-08-24 : Are you sure it's not your caps lock?
[C] 2022-08-24 : 😤! You're right!

...

[A] 2022-09-15: Good evening! How may I assist you?
[C] 2022-09-15: Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.
[A] 2022-09-15: I'm sorry to hear that. Let me help you. Can you please confirm your email address?
[C] 2022-09-15: Sure, it's [REDACTED].

[A] 2022-09-24: Welcome! What can I do for you today?
[C] 2022-09-24: Hi, I need to change my delivery address for my recent order.
[A] 2022-09-24: Alright. Please provide your order number.
[C] 2022-09-24: It's 3344556. Thanks for your help!
```

### Step 4: Few-Shot Prompting to Improve Output

```toml
instructions_4 = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace names in [] with "A", for Agent, and "C", for Client, respectively
2. Replace any other personally identifyable information, such as names or email addresses
3. Replace the date-time information to only show the date in the format YYYY-mm-dd
4. Replace all swear words with the following emoji: "😤"

Here is some example output in the expected format:

2021-09-29:
----------------------------------------------
A: How can I assist you today?
C: I CAN'T GET THIS 😤 THING TO TURN ON!!


2022-02-24:
----------------------------------------------
A: Good morning! How can I help you today?
C: Could you help me with applying my coupon code?
"""
```

**Output** sticks to the provided format:

```
2022-08-24:
----------------------------------------------
A: What can I help you with?
C: I CAN'T CONNECT TO MY 😤 ACCOUNT
A: Are you sure it's not your caps lock?
C: 😤! You're right!

...

2022-09-15:
----------------------------------------------
A: Good evening! How may I assist you?
C: Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.
A: I'm sorry to hear that. Let me help you. Can you please confirm your email address?
C: Sure, it's [REDACTED].

2022-09-24:
----------------------------------------------
A: Welcome! What can I do for you today?
C: Hi, I need to change my delivery address for my recent order.
A: Alright. Please provide your order number.
C: It's 3344556. Thanks for your help!
```

### Step 5: Classify Sentiment of Chat Conversation

```toml
instructions_5 = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace names in [] with "A", for Agent, and "C", for Client, respectively
2. Replace any other personally identifyable information, such as names or email addresses
3. Replace the date-time information to only show the date in the format YYYY-mm-dd
4. Classify the sentiment of the client's responses in the conversation with "🔥" for negative and "✅" for positive
5. Replace all swear words with the following emoji: "😤"

Here is some example output in the expected format:

🔥 2021-09-29:
----------------------------------------------
A: How can I assist you today?
C: I CAN'T GET THIS 😤 THING TO TURN ON!!


✅ 2022-02-24:
----------------------------------------------
A: Good morning! How can I help you today?
C: Could you help me with applying my coupon code?
"""
```

**Output** works pretty well and could be good for visual inspection of a customer service agent:

```
🔥 2022-08-24:
----------------------------------------------
A: What can I help you with?
C: I CAN'T CONNECT TO MY 😤 ACCOUNT
A: Are you sure it's not your caps lock?
C: 😤! You're right!

...

✅ 2022-09-15:
----------------------------------------------
A: Good evening! How may I assist you?
C: Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.
A: I'm sorry to hear that, C. Let me help you. Can you please confirm your email address?
C: Sure, it's [REDACTED].

✅ 2022-09-24:
----------------------------------------------
A: Welcome! What can I do for you today?
C: Hi, I need to change my delivery address for my recent order.
A: Alright, C. Please provide your order number.
C: It's 3344556. Thanks for your help!
```

### Step 6: Format as Machine-Readable Output (JSON)

```toml
instructions_6 = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace names in [] with "A", for Agent, and "C", for Client, respectively
2. Replace any other personally identifyable information, such as names or email addresses
3. Replace the date-time information to only show the date in the format YYYY-mm-dd
4. Classify the sentiment of the client's responses in the conversation as "negative" and "positive"
5. Replace all swear words with the following emoji: "😤"
6. Format the resulting text as JSON

Here is some example output in the expected JSON format:

``json
{
    "negative": [
        {
            "date": "2021-09-29",
            "conversation": [
                "A: How can I assist you today?",
                "C: I CAN'T GET THIS 😤 THING TO TURN ON!!"
            ]
        },
        ]
    "positive": [
        {
            "date": "2022-02-24",
            "conversation": [
                "A: Good morning! How can I help you today?",
                "C: Could you help me with applying my coupon code?"
            ]
        },
        ]
}
``
"""
```

**Output** is classified according to sentiment, and well-formatted JSON:

```json
{
    "negative": [
        {
            "date": "2022-08-24",
            "conversation": [
                "Agent: What can I help you with?",
                "Client: I CAN'T CONNECT TO MY 😤 ACCOUNT",
                "Agent: Are you sure it's not your caps lock?",
                "Client: 😤! You're right!"
            ]
        },
        {
            "date": "2022-10-05",
            "conversation": [
                "Agent: Hi, how can I help you today?",
                "Client: MY 😤 ORDER STILL HASN'T ARRIVED AND IT'S BEEN A WEEK!!!",
                "Agent: I'm sorry to hear that, Client. Let's look into this issue.",
                "Agent: Can you please provide your order number so I can check the status for you?",
                "Client: Fine, it's ******.",
                "Agent: Thank you, Client. I see there was a delay in shipping. Your order will arrive within the next 2 days."
            ]
        }
    ],
    "positive": [
        {
            "date": "2022-09-15",
            "conversation": [
                "Agent: Hello! How can I assist you today?",
                "Client: I can't seem to find the download link for my purchased software.",
                "Agent: No problem, Client. Let me find that for you. Can you please provide your order number?",
                "Client: It's ******. Thanks for helping me out!"
            ]
        },
        {
            "date": "2022-09-18",
            "conversation": [
                "Agent: Hello! How can I help you today?",
                "Client: I accidentally placed an order twice, can you help me cancel one?",
                "Agent: Sure, Client. Can you give me the order number you'd like to cancel?",
                "Client: Yes, it's ******. Thank you!",
                "Agent: I've successfully canceled order number ******. You will receive a confirmation email shortly."
            ]
        },
        {
            "date": "2022-09-29",
            "conversation": [
                "Agent: Good morning, what can I assist you with today?",
                "Client: Hi there, I received a damaged item in my order. Can you help me return it?",
                "Agent: I'm sorry to hear that, Client. Can you provide your order number and specify the damaged item?",
                "Client: Sure, order number is ****** and the damaged item is a coffee mug."
            ]
        },
        {
            "date": "2022-10-04",
            "conversation": [
                "Agent: How can I help you today?",
                "Client: My coupon code isn't working at checkout. Can you help?",
                "Agent: Of course, Client. Please provide the coupon code you're trying to use.",
                "Client: It's \"HELLO10\".",
                "Agent: I've checked the code, and it seems to have expired. I apologize for the inconvenience. Here's a new code for you to use: \"WELCOME15\"."
            ]
        },
        {
            "date": "2022-09-15",
            "conversation": [
                "Agent: Good evening! How may I assist you?",
                "Client: Hi there, I'm having trouble logging into my account. I've tried resetting my password, but it's not working.",
                "Agent: I'm sorry to hear that, Client. Let me help you. Can you please confirm your email address?",
                "Client: Sure, it's **********."
            ]
        },
        {
            "date": "2022-09-24",
            "conversation": [
                "Agent: Welcome! What can I do for you today?",
                "Client: Hi, I need to change my delivery address for my recent order.",
                "Agent: Alright, Client. Please provide your order number.",
                "Client: It's ******. Thanks for your help!"
            ]
        }
    ]
}
```