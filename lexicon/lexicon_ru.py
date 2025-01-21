COMMANDS_MENU: dict[str, str] = {
    '/start': 'Start',
    '/help': 'Get help',
}

COMMANDS_LEXICON = {
    'start' : "Hello! I'm helper bot for travelling and daily tasks. Use any button below to use me!",
    'help' : "This is help menu \n\n Choose a button below what you need help with!"
}

BUTTONS_LEXICON = {
    'travel_btn' : '🌍 Travel',
    'tasks_btn' : '📋 Tasks',
    'daily_btn' : '🛠 Daily Help',
    'back_btn' : 'Back',
    'developer_btn' : 'Contact developer',
    'instruction_btn' : "See what I can do",
    'currency_btn': 'Currency rates 💵',
    'weather_btn': 'Weather 🌥️',

    'usd_btn': 'US Dollars',
    'rub_btn': 'Russian Rubles',
    'eur_btn': 'Euro',
    'cad_btn': 'Canadian Dollars'
}

ANSWERS_LEXICON = {
    'travel_btn' : 'You pressed the travel menu. \n\n Please choose the next one you need to use.',
    'tasks_btn' : 'Tasks button pressed',
    'daily_btn' : 'Daily help button pressed',
    'back_btn' : 'Getting back',
    'developer_btn' : 'Type your message for the developer and we will contact you',
    'developer_message_sent' : 'Your message has been sent to the developer',
    'instruction_btn' : "I'm not ready to work, do it later",
    'currency_btn' : 'Please choose the first currency you want to convert below or enter yours',
    'second_currency': 'Please choose the second currency you want convert to below or enter yours',
    'amount_currency': 'Please enter amount you want to convert',
    'result_currency': '{} {} = {} {}'
}

CALLBACKS_LEXICON = {
    'usd_btn': 'USD',
    'eur_btn': 'EUR',
    'rub_btn': 'RUB',
    'cad_btn': 'CAD',
    'back_btn': 'back_btn_pressed',
}