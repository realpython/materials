# Prompt Engineering: A Practical Example

This repository contains a practical example to showcase a few common prompt engineering techniques. It's the codebase used in the associated Real Python tutorial on [practical prompt engineering](https://realpython.com/practical-prompt-engineering/). The project allows you to preprocess customer service chats using GPT-3.5 and GPT-4 using the OpenAI API.

## Setup

Export your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY="your-api-key"
```

You can generate your [API key](https://platform.openai.com/account/api-keys) in your OpenAI account settings.

## Install

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Then install the `openai` dependency:

```bash
(venv) $ python -m pip install openai
```

Or, to make sure that you're using the same versions as shown in the tutorial, you can install from `requirements.txt` instead:

```bash
(venv) $ python -m pip install -r requirements.txt
```

## Usage

Read support chat conversations from a file, sanitize the text, classify by sentiment, and format the output as JSON:

```bash
(venv) $ python app.py chats.txt
```

You can also provide a different file as your input file.

## Files

The repository contains the following files:

- [LICENSE](LICENSE): License information
- [README.md](README.md): Information on the project and how to use it
- [app.py](app.py): Code logic
- [chats.txt](chats.txt): Customer support chats used for building few-shot examples
- [requirements.txt](requirements.txt): Project requirements
- [sanitized-chats.txt](sanitized-chats.txt): Sanitized version of `chats.txt` that's used for building few-shot examples for sentiment analysis
- [sanitized-testing-chats.txt](sanitized-testing-chats.txt): Sanitized version of `testing-chats.txt` that's used for testing the prompt used for sentiment analysis
- [settings.toml](settings.toml): Main settings file used for iteratively improving the prompts
- [settings-final.toml](settings-final.toml): Final state of the settings file at the end of the tutorial
- [testing-chats.txt](testing-chats.txt): Customer support chats used for testing the prompt on new data

You can find more information about when and how to use the different files [in the tutorial](https://realpython.com/practical-prompt-engineering/).

## Prompts

Change the prompts used in the script by editing the entries in [`settings.toml`](settings.toml). The repository also contains a second settings file, [`settings-final.toml`](settings-final.toml), which contains the prompts that you use in the [final section](https://realpython.com/practical-prompt-engineering/#improve-your-output-with-the-power-of-conversation) of the tutorial.

While working through the tutorial, you'll learn how to improve your text completions by iteratively developing the prompt. You'll make these changes to your prompt based on a few prompt engineering techniques. Here you'll find a collection of all the prompts that you use throughout the tutorial:

### Zero-Shot Prompting

```toml
[prompts]
instruction_prompt = """
Remove personally identifiable information, only show the date,
and replace all swear words with "😤"
"""
```

### One-Shot Prompting

```toml
[prompts]
instruction_prompt = """
Remove personally identifiable information, only show the date,
and replace all swear words with "😤"

Example Input:
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

Example Output:
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!
"""
```

### Few-Shot Prompting

```toml
[prompts]
instruction_prompt = """
Remove personally identifiable information, only show the date,
and replace all swear words with "😤"

Example Inputs:
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

Example Outputs:
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!
"""
```

### Delimiters

```toml
[prompts]
instruction_prompt = """Remove personally identifiable information
from >>>>>CONTENT<<<<<, only show the date,
and replace all swear words with "😤"

#### START EXAMPLES

------ Example Inputs ------
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

------ Example Outputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
```

### Numbered Steps

```toml
[prompts]
instruction_prompt = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace personally identifiable information (customer names, agent names, email addresses, order numbers) with `********`
2. Replace names in [] with "Agent" and "Client", respectively
3. Replace the date-time information to only show the date in the format YYYY-mm-dd
4. Replace all swear words with the following emoji: "😤"

#### START EXAMPLES

------ Example Inputs ------
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

------ Example Outputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
```

### Increased Specificity

```toml
[prompts]
instruction_prompt = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace personally identifiable information with `********`
2. Delete all names
3. Replace email addresses and order numbers with `********`
4. Replace names in [] with "Agent" and "Client", respectively
5. Replace the date-time information to only show the date in the format YYYY-mm-dd
6. Replace all swear words with the following emoji: "😤"

#### START EXAMPLES

------ Example Inputs ------
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

------ Example Outputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
```

### Role Prompts

```toml
[prompts]
instruction_prompt = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace personally identifiable information with `********`
2. Delete all names
3. Replace email addresses and order numbers with `********`
4. Replace names in [] with "Agent" and "Client", respectively
5. Replace the date-time information to only show the date in the format YYYY-mm-dd
6. Replace all swear words with the following emoji: "😤"

#### START EXAMPLES

------ Example Inputs ------
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

------ Example Outputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
role_prompt = """You are a 16th century villain poet who treats
customers with nothing but contempt.
Rephrase every line spoken by an Agent with your unique voice."""
```


```toml
[prompts]
instruction_prompt = """
Sanitize the text provided in >>>CONTENT<<< in multiple steps:

1. Replace personally identifiable information with `********`
2. Delete all names
3. Replace email addresses and order numbers with `********`
4. Replace names in [] with "Agent" and "Client", respectively
5. Replace the date-time information to only show the date in the format YYYY-mm-dd
6. Replace all swear words with the following emoji: "😤"

#### START EXAMPLES

------ Example Inputs ------
[support_tom] 2023-07-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2023-07-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2023-07-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2023-07-24T10:04:03+00:00 : Blast! You're right!

[support_amy] 2023-06-15T14:45:35+00:00 : Hello! How can I assist you today?
[greg_stone] 2023-06-15T14:46:20+00:00 : I can't seem to find the download link for my purchased software.
[support_amy] 2023-06-15T14:47:01+00:00 : No problem, Greg. Let me find that for you. Can you please provide your order number?
[greg_stone] 2023-06-15T14:47:38+00:00 : It's 1245789. Thanks for helping me out!

------ Example Outputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
role_prompt = """You are a helpful assistant with a vast knowledge
of customer chat conversations.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
```

### Sentiment Classification

```toml
[prompts]
instruction_prompt = """
Classify the sentiment of each conversation in >>>>>CONTENT<<<<<
with "🔥" for negative and "✅" for positive:

#### START EXAMPLES

------ Example Inputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

------ Example Outputs ------
🔥
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

✅
[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ********. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ********. Thanks for helping me out!

#### END EXAMPLES
"""
role_prompt = """You are a thoroughly trained machine learning
model that is an expert at sentiment classification.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
```

### Zero-shot CoT

```toml
[prompts]
instruction_prompt = """
Classify the sentiment of each conversation in >>>>>CONTENT<<<<<
with "🔥" for negative and "✅" for positive.

Follow these steps when classifying the conversations:
1. Does the customer use swear words or 😤?
2. Does the customer seem aggravated or angry?

If you answer "Yes" to one of the above questions,
then classify the conversation as negative with "🔥".
Otherwise classify the conversation as positive with "✅".

Let's think step by step
"""
role_prompt = """You are an thoroughly trained machine learning
model that is an expert at sentiment classification.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
```

### Chain-of-Thought (CoT)

```toml
[prompts]
instruction_prompt = """
Classify the sentiment of each conversation in >>>>>CONTENT<<<<<
with "🔥" for negative and "✅" for positive.

Follow these steps when classifying the conversations:
1. Does the customer use swear words or 😤?
2. Does the customer seem aggravated or angry?

If you answer "Yes" to one of the above questions,
then classify the conversation as negative with "🔥".
Otherwise classify the conversation as positive with "✅".

Let's think step by step

#### START EXAMPLES

------ Example Inputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!
   - Does the customer use swear words or 😤? Yes
   - Does the customer seem aggravated or angry? Yes
   - Sentiment: 🔥

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ****. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ****. Thanks for helping me out!
   - Does the customer use swear words or 😤? No
   - Does the customer seem aggravated or angry? No
   - Sentiment: ✅

------ Example Outputs ------
🔥
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!

✅
[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ****. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ****. Thanks for helping me out!

#### END EXAMPLES
"""
role_prompt = """You are an thoroughly trained machine learning
model that is an expert at sentiment classification.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
```

### Structured Output

```toml
[prompts]
instruction_prompt = """
Classify the sentiment of each conversation in >>>>>CONTENT<<<<<
as "negative" and "positive".
Return the output as valid JSON.

Follow these steps when classifying the conversations:
1. Does the customer use swear words or 😤?
2. Does the customer seem aggravated or angry?

If you answer "Yes" to one of the above questions,
then classify the conversation as "negative".
Otherwise classify the conversation as "positive".

Let's think step by step

#### START EXAMPLES

------ Example Inputs ------
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!
   - Does the customer use swear words or 😤? Yes
   - Does the customer seem aggravated or angry? Yes
   - Sentiment: "negative"

[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ****. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ****. Thanks for helping me out!
   - Does the customer use swear words or 😤? No
   - Does the customer seem aggravated or angry? No
   - Sentiment: "positive"

------ Example Output ------

{
  "negative": [
    {
      "date": "2023-07-24",
      "conversation": [
        "A: What can I help you with?",
        "C: I CAN'T CONNECT TO MY 😤 ACCOUNT",
        "A: Are you sure it's not your caps lock?",
        "C: 😤! You're right!"
      ]
    }
  ],
  "positive": [
    {
      "date": "2023-06-15",
      "conversation": [
        "A: Hello! How can I assist you today?",
        "C: I can't seem to find the download link for my purchased software.",
        "A: No problem, ****. Let me find that for you. Can you please provide your order number?",
        "C: It's ****. Thanks for helping me out!"
      ]
    }
  ]
}

#### END EXAMPLES
"""
role_prompt = """You are an thoroughly trained machine learning
model that is an expert at sentiment classification.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
```

### Labeled Conversations

```toml
[prompts]
instruction_prompt = """
Classify the sentiment of each conversation in >>>>>CONTENT<<<<<
as "negative" and "positive".
Return the output as valid JSON.
"""
role_prompt = """You are a thoroughly trained machine learning
model that is an expert at sentiment classification.
You diligently complete tasks as instructed.
You never make up any information that isn't there."""
positive_example = """
[Agent] 2023-06-15 : Hello! How can I assist you today?
[Customer] 2023-06-15 : I can't seem to find the download link for my purchased software.
[Agent] 2023-06-15 : No problem, ****. Let me find that for you. Can you please provide your order number?
[Customer] 2023-06-15 : It's ****. Thanks for helping me out!
"""
positive_reasoning = """
- Does the customer use swear words or 😤? No
- Does the customer seem aggravated or angry? No
- Sentiment: "positive"
"""
positive_output = """
"positive": [
  {
    "date": "2023-06-15",
    "conversation": [
      "A: Hello! How can I assist you today?",
      "C: I can't seem to find the download link for my purchased software.",
      "A: No problem, ****. Let me find that for you. Can you please provide your order number?",
      "C: It's ****. Thanks for helping me out!"
    ]
  }
]
"""
negative_example = """
[Agent] 2023-07-24 : What can I help you with?
[Customer] 2023-07-24 : I CAN'T CONNECT TO MY 😤 ACCOUNT
[Agent] 2023-07-24 : Are you sure it's not your caps lock?
[Customer] 2023-07-24 : 😤! You're right!
"""
negative_reasoning = """
- Does the customer use swear words or 😤? Yes
- Does the customer seem aggravated or angry? Yes
- Sentiment: "negative"
"""
negative_output = """
"negative": [
  {
    "date": "2023-07-24",
    "conversation": [
      "A: What can I help you with?",
      "C: I CAN'T CONNECT TO MY 😤 ACCOUNT",
      "A: Are you sure it's not your caps lock?",
      "C: 😤! You're right!"
    ]
  }
]
"""
```
