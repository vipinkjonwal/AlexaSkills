
# Lambda Function for Epic Cricket Skill
# Type : Fact Skill

import random

cricketFacts = [
    "Sachin Tendulkar got out for a duck only once in his Ranji career.",
    "Sri Lanka has a sole Test win against the Aussies till date.",
    "Sanath Jayasuriya has more ODI wickets than Shane Warne.",
    "Dhaka’s Sher-e-Bangla stadium and Bangabandhu stadium have hosted more ODIs than Lord’s.",
    "The highest number of runs scored in an over is not 36. It’s 77.",
    "Adam Gilchrist holds the record for playing the most number of Tests straight after debut.",
    "Ishant Sharma is responsible for all the three highest scores made by a batsman against India in the 21 st century.",
    "On 12th January 1964, Indian spinner Bapu Nadkarni bowled 21 consecutive maiden overs vs England at Chennai.",
    "Chris Martin and B.S Chandrasekhar have taken more Test wickets in their career than the test runs they scored.",
    "Wilfred Rhodes took 4,204 wickets in First Class cricket.",
    "Sir Jack Hobbs scored 199 centuries in his First Class career.",
    "In a World Cup Match, chasing 335, Sunil Gavaskar scored an unbeaten 36 off 174 balls.",
    "Jim Laker once took 19 wickets in a Test match.",
    "Saurav Ganguly is the only Indian player to score a century in the knock out stages of a World Cup.",
    "After Virat Kohli’s debut, India has chased down 300+ targets five times.",
    "Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.",
    "Sachin + Zaheer = (Almost) Kallis, in terms of runs and wickets.",
    "The player with the most number of not outs in Test cricket is not Rahul Dravid, but Courtney Walsh.",
    "Saurav Ganguly is the only player to win four consecutive Man of the Match awards in ODIs.",
    "Dirk Nannes has represented both Australia and Netherlands in International Cricket. ",
    "Shahid Afridi used a bat borrowed from Waqar Younis to score the fastest century in a ODI match. ",
    "Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.",
    "Sir Don Bradman has just hit 6 sixes in his entire career.",
    "Virender Sehwag’s highest scores in T20, ODI and Tests are 119 (IPL), 219 and 319 respectively.",
    "Wasim Akram’s highest Test innings score of 257 is higher than that of Sachin Tendulkar's.",
    "Graeme Smith is the only player in the history of cricket to have captained a team for more than 100 Test matches. ",
    "Saeed Ajmal has never won a Man of the Match award in One Day International Cricket. ",
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
    speech_output = "I'm here to help you. " \
                    "Ask for Epic Cricket here by saying,"\
                    "Tell me tell me cricket facts or tell me epic facts."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = None
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Epic Cricket. " \
                    "Say, tell me cricket facts or tell me epic facts."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Say, tell me cricket facts or just say facts."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def onLaunch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    # Dispatch to your skill's launch
    return get_welcome_response()


def factInvoke(intent, session):
    newFact = random.choice(cricketFacts)
    session_attributes = {}
    title = 'Welcome'
    speech_output = newFact
    reprompt_text = "Say, tell me cricket facts."
    return build_response(session_attributes,build_speechlet_response(title,speech_output,reprompt_text,True))
    
def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for trying Epic Cricket Skill. " \
                    "Get back soon for more amazing facts. Have a Nice Day."
    shouldEndSession = True
    return build_response({}, build_speechlet_response(cardTitle, speechOutput, None, shouldEndSession))    

def onIntent(intentRequest, session):
             
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']

    if intentName == "EpicCricket" or intentName == "CricketFacts":
        return factInvoke(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return on_help()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")
        
def lambda_handler(event, context):
    # TODO implement
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])


