schema = {
    'title': {
        'type': 'string',
        'maxlength': 255,
    },
    'number': {
        'type': 'string',
        'maxlength': 255,
    },
    'department': {
        'type': 'string',
        'maxlength': 255,
    },
    'description': {
        'type': 'string',
        #'maxlength': 255,
    },
    'units': {
        'type': 'string', #integer threw validation error :/
    },
}
courses = {
    'schema': schema,
}
DOMAIN = {
    'courses': courses,
}

my_settings = {
    'X_DOMAINS': '*',
    'DOMAIN': {'courses': courses}    
}

from eve import Eve
app = Eve(settings=my_settings)
app.run()

