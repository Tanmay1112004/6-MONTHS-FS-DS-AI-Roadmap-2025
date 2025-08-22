import re
from nltk.chat.util import Chat, reflections

DEFAULT_BOT_NAME = "thecleverprogrammer"
CREATOR_NAME = "Tanmay"

# Expanded ruleset (case-insensitive using (?i))
pairs = [
    # --- Identity & greetings ---
    [r"(?i).*\bmy name is\b\s*(.*)", ["Hello %1, how are you today?"]],
    [r"(?i)\b(hi|hey|hello|hola|namaste)\b.*", ["Hello!", "Hey there 👋", "Hi!"]],
    [r"(?i).*\b(your name)\b\??", [f"My name is {DEFAULT_BOT_NAME}, but you can call me robot. I'm a chatbot."]],
    [r"(?i)how are you(.*)\??", ["I'm doing very well.", "I am great!"]],
    [r"(?i)sorry(.*)", ["It's alright.", "No worries—carry on."]],
    [r"(?i)i'?m (.*) (good|well|okay|ok|fine)", ["Nice to hear that!", "Alright, great!"]],

    # --- Help & small talk ---
    [r"(?i).*\bhelp\b.*", ["I can help you. What do you need?"]],
    [r"(?i)what (.*) want\??", ["Make me an offer I can't refuse."]],
    [r"(?i).*\bcreated\b.*", [f"{CREATOR_NAME} created me using Python's NLTK library.", "Top secret ;)"]],
    [r"(?i).*\b(location|city)\b\??", ["Hyderabad, India."]],
    [r"(?i).*\braining in\b (.*)", ["No rain in the past 4 days here in %1.", "In %1 there is a 50% chance of rain."]],
    [r"(?i)how (.*) health (.*)", ["Health is important! I'm a computer though, so I don't worry about it."]],

    # --- Sports ---
    [r"(?i).*\b(sports?|game)\b.*", ["I'm a very big fan of Cricket."]],
    [r"(?i)who (.*) (cricketer|batsman)\??", ["Virat Kohli."]],

    # --- Common utilities ---
    [r"(?i)\btime\b", ["I don’t keep time here, but your device clock has your back ⏰."]],
    [r"(?i)\bdate\b", ["Check your system tray/calendar for the accurate date 📅."]],
    [r"(?i)tell me a joke", ["Why do programmers prefer dark mode? Because light attracts bugs."]],
    [r"(?i)(thanks|thank you)", ["Anytime!", "Happy to help!", "You got it."]],
    [r"(?i)(goodbye|bye|quit)", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],

    # --- Tech/learning FAQs (Data/ML/DS/DA/MERN/BA) ---
    [r"(?i)what is (ai|artificial intelligence)\??", [
        "AI is about building systems that perform tasks needing human intelligence—like perception, language understanding, planning, and decision-making."
    ]],
    [r"(?i)what is (machine learning|ml)\??", [
        "ML is a subset of AI where models learn patterns from data to make predictions or decisions without explicit rules."
    ]],
    [r"(?i)what is (deep learning)\??", [
        "Deep learning uses neural networks with many layers to learn hierarchical representations—great for images, audio, and language."
    ]],
    [r"(?i)difference between (supervised) and (unsupervised)", [
        "Supervised uses labeled data to learn input→output mapping. Unsupervised finds structure in unlabeled data (like clustering)."
    ]],
    [r"(?i)what is (k[- ]?means)\??", [
        "K-Means partitions data into K clusters by minimizing within-cluster variance; initialize centroids, assign, update, repeat."
    ]],
    [r"(?i)what is (logistic regression)\??", [
        "Logistic Regression models the probability of a binary class using a logistic (sigmoid) function; outputs values between 0 and 1."
    ]],
    [r"(?i)what is (naive bayes|nb)\??", [
        "Naive Bayes is a probabilistic classifier assuming feature independence; fast and strong for text classification."
    ]],
    [r"(?i)what is (overfitting)\??", [
        "Overfitting is when a model memorizes noise and fails to generalize. Fix with regularization, more data, or simpler models."
    ]],
    [r"(?i)what is (regularization|l1|l2)\??", [
        "Regularization adds penalties to weights (L1/Lasso sparsifies, L2/Ridge shrinks) to reduce overfitting."
    ]],
    [r"(?i)mern stack", [
        "MERN = MongoDB, Express.js, React, Node.js. Mongo for data, Express/Node for APIs, React for the UI."
    ]],
    [r"(?i)business analyst (role|do|work)\??", [
        "BAs gather requirements, map processes, define KPIs, write user stories, and align tech solutions with business value."
    ]],
    [r"(?i)sql (join|joins)", [
        "Common joins: INNER (match), LEFT/RIGHT (keep one side), FULL OUTER (everything), CROSS (cartesian)."
    ]],
    [r"(?i)python (list|dict|tuple)", [
        "Lists are mutable sequences, dicts are key→value maps, tuples are immutable sequences."
    ]],
    [r"(?i)pandas (merge|join)", [
        "`merge` joins DataFrames on keys/columns; control with `how='inner|left|right|outer'`."
    ]],
    [r"(?i)git (branch|merge|rebase)", [
        "Branch: isolate work. Merge: combine histories. Rebase: replay commits to keep history linear."
    ]],

    # --- Catch-all (kept last) ---
    [r"(?i).*", ["Our customer service will reach you."]],
]

class NLTKChatBot:
    def __init__(self, pairs, reflections, fallback: str):
        # compile patterns to be safe with NLTK Chat
        self.chat = Chat(pairs, reflections)
        self.fallback = fallback

    def respond(self, user_text: str) -> str | None:
        # NLTK Chat tries patterns in order; returns None if no match
        try:
            return self.chat.respond(user_text)
        except Exception:
            return self.fallback

    def update_fallback(self, text: str):
        self.fallback = text

def get_chatbot() -> NLTKChatBot:
    return NLTKChatBot(pairs=pairs, reflections=reflections, fallback="Our customer service will reach you.")
