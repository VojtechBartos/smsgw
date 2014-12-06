# -*- coding: utf-8 -*-
# http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

VALID = {
    "label": "Random label",
    "text": "Random super long test of text content"
}

VALID_UPDATE = {
    "label": "Updated label",
    "text": "updated text which should be saved to database"
}

INVALID_NOLABEL = {
    "text": "Random super long test of text content"
}

INVALID_SHORTLABEL = {
    "label": "short",
    "text": "Random super long test of text content"
}

INVALID_LONGLABEL = {
    "label": """short short asld kasldk alskd lask dlaks ldkasl kdalsk dlaks d
                asdlkjasl dkjasl dkjasljk dlaskj dlaskj dljkas ldkjasl dkjaslkj
                asdaskjdkasjdkasjdkj ksja dkjas """,
    "text": "Random super long test of text content"
}

INVALID_NOTEXT = {
    "label": "Random "
}

INVALID_SHORTTEXT = {
    "label": "not too short",
    "text": "short"
}