from settings.configuration import Config

ORM = {
    "connections": {"default": "mysql://root:@127.0.0.1:3307/todo"},
    'apps':{
        'models':{
            'models':['aerich', *Config.DB_MODELS]
        }
    }
} 