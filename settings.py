#RESOURCE_METHODS = ['GET']
#ITEM_METHODS = []
#RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
#ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
#X_DOMAINS = '*'

SERVER_NAME = '127.0.0.1:8000'

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

