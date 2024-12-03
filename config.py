from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b39be032fc0c567d0cda60dbea99606e")
      API_ID = int(getenv("API_ID", "29563132"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7680437010:AAE5tlqPMHKfk4C8JZIYA4iqnzGPXYquqBM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002434067416:-1002498395810").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
