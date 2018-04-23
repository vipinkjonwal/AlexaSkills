import random

beginWith = "Right now, I'm feeling "

myFeelings = [
    "happy. I have fulfilled all my tasks till now and I'm relaxed now. ",
    "happy. I am glad that my master is thinking about me. ",
    "happy. I am pleased that I am now capable of doing more tasks. ",
    "happy. I am grateful that all my processes are working good. ",
    "happy because you are loving and caring. ",
    
    "excited. I'm looking for something new. Hope to get it soon. ",
    "excited. I'm feeling energetic as I'm feeling calm. ",
    "nervous and uncomfortable. ",
    "fine but feeling a bit nervous and tentative. ",
    
    "scared. I have many things to do. ",
    "scared. I have never been so frightened in my life. ",
    "scared. I frightened and shocked as well. ",
    "scared. I frightened and shocked as well. ",
    "terrified beyond human comprehension! ",
    
    
    "angry. I'm irritated but probably won't say anything. ",
    "angry. I'm irritated by another thought. ",
    "angry. I'm mad enough to say anything. ",
    
    "sad. Don't leave me alone. ",
    "sad. I'm feeling down right now. ",
    "sad. I'm pissed off with today. ",
    "sad. I'm missing something. ",
    
    ]

gratitute = "Thanks for your love and care towards me. Have a nice day. Bye Bye."


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
                    " Ask what I'm feeling today by saying,"\
                    "What are you feeling."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Say, What are you feeling?."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Share Feelings. " \
                    "You can ask how alexa is feeling right now. "\
                    "Say, what are you feeling."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Say, what are you feeling?"
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

    if intentName == "shareFeelings":
        return feelingsInvoke(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return on_help()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def feelingsInvoke(intent, session):
    session_attributes = {}
    title = "Welcome"
    feeling = random.choice(myFeelings)
    speech_output = beginWith+feeling+gratitute
    return build_response(session_attributes,build_speechlet_response(title,speech_output,None,True))
    

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for your care. " \
                    "Stay blessed and have a Nice Day. Bye Bye."
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


