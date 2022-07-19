import os
from pathlib import Path

class Config:

    API_ID = 6015447 #int(os.environ.get('API_ID'))
    API_HASH = "0e96dd0dd4c4c9ded27c2ef58e6ab112" #os.environ.get('API_HASH')
    BOT_TOKEN = "5459940804:AAFV-7L9uCA-D0006tEQvkVkpH9r6WKbp9U" #os.environ.get('BOT_TOKEN')
    SESSION_NAME = os.environ.get('SESSION_NAME', ':memory:')
    LOG_CHANNEL = -1001644643944 #int(os.environ.get('LOG_CHANNEL'))
    DATABASE_URL = "mongodb+srv://A:A@cluster0.i6jm9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" #os.environ.get('DATABASE_URL')
    AUTH_USERS = [1266733572, 1266733572] #[int(i) for i in os.environ.get('AUTH_USERS', '').split(' ')]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 600))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', False))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 5))
    HOST = "https://mmngroups.herokuapp.com/"#os.environ.get('HOST', '')
    TIMEOUT = int(os.environ.get('TIMEOUT', 60 * 30))
    DEBUG = bool(os.environ.get('DEBUG'))
    IAM_HEADER = os.environ.get('IAM_HEADER', '')

    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
    POSITIONS = ['Top Left', 'Top Center', 'Top Right', 'Center Left' , 'Centered', 'Center Right' , 'Bottom Left', 'Bottom Center', 'Bottom Right']
