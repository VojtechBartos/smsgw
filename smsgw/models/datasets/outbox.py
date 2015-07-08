# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

from smsgw.models import Outbox

SEND_BASIC = {
    'destination_number': '+420736202560',
    'message': 'basic message',
    'coding': Outbox.DEFAULT_NO_COMPRESSION
}

SEND_FLASH = {
    'destination_number': '+420736202560',
    'message': 'flash message',
    'coding': Outbox.DEFAULT_NO_COMPRESSION,
    'flash': True
}

MULTIPART_MESSAGES = [
    {
        'destination_number': '+420736202561',
        'message': " ".join([
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin",
            "blandit dignissim quam, ut bibendum quam. Fusce et urna vel",
            "magna dapibus elementum dapibus sit amet nibh. Donec ",
            "vestibulum nulla sed maximus tincidunt. Ut quis finibus",
            "mauris. Vivamus at libero sed sapien bibendum tincidunt",
            "venenatis non tellus. Sed in tincidunt dolor."
        ]),
        'coding': Outbox.DEFAULT_NO_COMPRESSION
    },
    {
        'destination_number': '+420736202562',
        'message': "".join([
            "Custom text contains special characters as ^2 or something",
            "more sophisticated as tilda ~",
            "Custom text contains special characters as ^2 or something",
            "more sophisticated as tilda ~",
            "Custom text contains special characters as ^2 or something",
            "more sophisticated as tilda ~",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin",
            "blandit dignissim quam, ut bibendum quam. Fusce et urna vel",
            "magna dapibus elementum dapibus sit amet nibh.",
            "Custom text contains special characters as ^2 or something",
            "more sophisticated as tilda ~",
            "Custom text contains special characters as ^2 or something",
            "more sophisticated as tilda ~",
        ]),
        'coding': Outbox.DEFAULT_NO_COMPRESSION,
        'flash': True
    }
]

MESSAGE_LENGTH = [
    (" ".join([
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin",
        "blandit dignissim quam, ut bibendum quam. Fusce et urna vel",
        "magna dapibus elementum dapibus sit amet nibh."
    ]), 169),
    ("And we would like to have these character [] |", 49),
    ("".join([
        "Custom text contains special characters as ^2 or something",
        "more sophisticated as tilda ~"
    ]), 89)
]
