import os
import logging
from os import getenv
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
LOGGER = logging.getLogger(__name__)

if not os.environ.get("ENV"):
    load_dotenv('.env', override=True)

class Config(object):
#--------------------

# MAIN BOT VARIABLES

#--------------------
    try:
        TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")
        APP_ID = int(getenv("APP_ID"))
        API_HASH = getenv("API_HASH")
        DATABASE_URL = getenv("DATABASE_URL")
        BOT_USERNAME = getenv("BOT_USERNAME")
        ADMINS = set(int(x) for x in getenv("ADMINS").split())
        PORT = getenv("PORT", "0")
        if PORT.isdigit():
            PORT = int(PORT)
    except KeyError as e:
        LOGGER.warning("Essential Configs are missing")
        exit(1)

    try:
        AUTH_CHAT = set(int(x) for x in getenv("AUTH_CHAT").split())
    except:
        AUTH_CHAT = ""
    
    IS_BOT_PUBLIC = getenv("IS_BOT_PUBLIC", True)
    LOG_CHAT = getenv("LOG_CHAT", "")
    LOG_ALL_INFO = getenv("LOG_ALL_INFO", "")

    try:
        AUTH_USERS = set(int(x) for x in getenv("AUTH_USERS").split())
    except:
        AUTH_USERS = ""

    # Dir to use for thumbs, download files etc. 
    WORK_DIR = getenv("WORK_DIR", "./bot/")
    # Just name of the Downloads Folder
    DOWNLOADS_FOLDER = getenv("DOWNLOADS_FOLDER", "DOWNLOADS")
    DOWNLOAD_BASE_DIR = WORK_DIR + DOWNLOADS_FOLDER

    BOT_LANGUAGE = getenv("BOT_LANGUAGE", "en")
    ANIT_SPAM_MODE = getenv("ANIT_SPAM_MODE", False)
    
#--------------------

# FILE/FOLDER NAMING

#--------------------
    PLAYLIST_NAME_FORMAT = getenv("PLAYLIST_NAME_FORMAT", "{title} - Playlist")
    ALBUM_NAME_FORMAT = getenv("ALBUM_PATH_FORMAT", "{album} - {albumartist}")
    TRACK_NAME_FORMAT = getenv("TRACK_NAME_FORMAT", "{title} - {artist}")
#--------------------

# KKBOX VARIABLES

#--------------------
    KKBOX_KEY = getenv("KKBOX_KEY", "abc")
    KKBOX_EMAIL = getenv("KKBOX_EMAIL", "")
    KKBOX_PASSWORD = getenv("KKBOX_PASSWORD", "")
#--------------------

# QOBUZ VARIABLES

#--------------------
    QOBUZ_EMAIL = getenv("QOBUZ_EMAIL", "")
    QOBUZ_PASSWORD = getenv("QOBUZ_PASSWORD", "")
    QOBUZ_USER = getenv("QOBUZ_USER", "")
    QOBUZ_TOKEN = getenv("QOBUZ_TOKEN", "")
#--------------------

# DEEZER VARIABLES

#--------------------
    DEEZER_EMAIL = getenv("DEEZER_EMAIL", "")
    DEEZER_PASSWORD = getenv("DEEZER_PASSWORD", "")
    DEEZER_BF_SECRET = getenv("DEEZER_BF_SECRET", "")
    DEEZER_TRACK_URL_KEY = getenv("DEEZER_TRACK_URL_KEY", "")
    DEEZER_ARL = getenv("DEEZER_ARL", "")
#--------------------

# SPOTIFY VARIABLES

#--------------------
    SPOTIFY_EMAIL = getenv("SPOTIFY_EMAIL", "")
    SPOTIFY_PASS = getenv("SPOTIFY_PASS", "")
    SPOTIFY_FORCE_PREMIUM = getenv("SPOTIFY_PASS", False)
#--------------------

# AUDIO SAVING OPTIONS (Dumping)

#--------------------
    COPY_AUDIO_FILES = getenv('COPY_AUDIO_FILES', False)
    DUPLICATE_CHECK = getenv('DUPLICATE_CHECK', False)
    SPOTIFY_CHAT = getenv('SPOTIFY_CHAT', None)
    QOBUZ_CHAT = getenv('QOBUZ_CHAT', None)
    TIDAL_CHAT = getenv('TIDAL_CHAT', None)
    DEEZER_CHAT = getenv('DEEZER_CHAT', None)
    KKBOX_CHAT = getenv('KKBOX_CHAT', None)


    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME[1:]
