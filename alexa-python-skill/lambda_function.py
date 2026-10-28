# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the
# Alexa Skills Kit SDK for Python. It's the Alexa-hosted Hello World
# template with the Joke Bot changes from the tutorial applied.
import logging
import random

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import (
    AbstractExceptionHandler,
    AbstractRequestHandler,
)
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

jokes = [
    "Did you hear about the semi-colon that broke the law?"
    " He was given two consecutive sentences.",
    "I ate a clock yesterday, it was very time-consuming.",
    "I've just written a song about tortillas; actually, it's more of a rap.",
    "I woke up this morning and forgot which side the sun rises from,"
    " then it dawned on me.",
    "I recently decided to sell my vacuum cleaner"
    " as all it was doing was gathering dust.",
    "If you shouldn't eat at night, why do they put a light in the fridge?",
]


class JokeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("JokeIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = random.choice(jokes)

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = (
            "Hey there! I am a Joke Bot. You can ask me to tell you a random"
            " Joke that might just make your day better!"
        )

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = "Hello World!"

        return (
            handler_input.response_builder.speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open")
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AMAZON.CancelIntent")(
            handler_input
        ) or ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = "Goodbye!"

        return handler_input.response_builder.speak(speak_output).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and
    debugging. It will simply repeat the intent the user said. You can
    create custom handlers for your intents by defining them above, then
    also adding them to the request handler chain below.
    """

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder.speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open")
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If
    you receive an error stating the request handler chain is not found,
    you have not implemented a handler for the intent being invoked or
    included it in the skill builder below.
    """

    def can_handle(
        self, handler_input: HandlerInput, exception: Exception
    ) -> bool:
        return True

    def handle(
        self, handler_input: HandlerInput, exception: Exception
    ) -> Response:
        logger.error(exception, exc_info=True)

        speak_output = (
            "Sorry, I had trouble doing what you asked. Please try again."
        )

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


# The SkillBuilder object acts as the entry point for your skill, routing
# all request and response payloads to the handlers above. Make sure any
# new handlers or interceptors you've defined are included below. The order
# matters - they're processed top to bottom.

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(JokeIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Make sure IntentReflectorHandler is last so it
# Doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
