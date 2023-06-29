import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6299210485:AAEb3tjYjE8DmwqX8ZCQ98kx8XcA3Q9Vals")
    
    API_ID = int(os.environ.get("API_ID", "20219667"))
    
    API_HASH = os.environ.get("API_HASH", "82b82bcd10c857178cc49e22f5e8d67c" )
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1929795683"))

    SESSION_NAME = "spectreurluploaderbot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongo.db")

    MAX_RESULTS = "50"
