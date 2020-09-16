import datetime

# MESSAGES
USER_GREETING_MESSAGES = (
    "hey",
    "hi",
    "good morning",
    "good evening",
    "hello",
    "hii",
    "heyy",
)

BOT_GREETING_MESSAGES = ("Hey", "Hi", "Whats up", "How are you doing")

NO_TERM_ENTERED_MESSAGES = (
    "Tell me what should I search on google!",
    "Dude, enter some value to search",
    "I'm confused! What to search?",
)

EMBEDDED_RESULTS_TITLE = "Top links for term "

# Google Search
GOOGLE_SEARCH_CACHE_TIMEOUT = datetime.timedelta(hours=6)
