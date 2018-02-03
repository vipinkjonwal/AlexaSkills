
import random

greatInventions = [
    "Wheel, the oldest known wheel is Mesopotamia, around 3500 BC.",
    "Compass, invented by the Chinese around 1050 BC.",
    "Automobile, the foundation was laid down in 1886.",
    "Nail, invented around 3400 BC.",
    "Light Bulb, invented by Thomas Edison in 1879.",
    "Electricity, year 1831 is marked the year of major breakthrough for elecricity.",
    "Printing press, developed around 1440 in Mainz, Germany.",
    "Telegraph, developed around 1830 by Samuel Morse.",
    "Transistors, an essential electronic component in 1947.",
    "Antibiotics, Alexander Fleming set the first leap in antibiotics in 1928.",
    "X-ray, discovered accidentally in 1895.",
    "Refrigerator, offered ways to preserve our food, inveneted in 1927.",
    "Television, a small box with enormous information, invenetd in 1884.",
    "Camera, in 1826, first permanennt photograoh was being taken.",
    "Email, the first substaintial use of email began in 1960s.",
    "Internet, being evoved with time, started in 1950.",
    "Credit Cards, the idea started in 1950 to consolidate multiple cards.",
    "ATM, automated teller machine, the bright idea was implemented in 1967.",
    "Robots, the foundation of modern robots was laid in 1950.",
    "Films, in March 1895, first film was shot."
    ]

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def on_help():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "I'm here to hep you." \
                    " Ask for great inventions facts here by saying,"\
                    "Tell me a great invention."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask, What are great inventions."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Great Inventions. " \
                    "Ask, Tell me a great invention."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask, What are great inventions."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def onLaunch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    # Dispatch to your skill's launch
    return get_welcome_response()

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']

    if intentName == "GreatInventionsIntent":
        return inventionInvoke(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return on_help()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def inventionInvoke(intent, session):
    invention = random.choice(greatInventions)
    session_attributes = {}
    title = 'Welcome'
    speech_output = invention
    reprompt_text = 'You can ask for great inventions facts by saying,'\
                    'Tell me about an invention.'
    return build_response(session_attributes,build_speechlet_response(title,speech_output,reprompt_text,True))
    

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for trying Great Inventions Alexa Skills. " \
                    "Get back soon for more facts. Have a Nice Day."
    shouldEndSession = True
    return build_response({}, build_speechlet_response(cardTitle, speechOutput, None, shouldEndSession))    
        
def lambda_handler(event, context):
    # TODO implement
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])


