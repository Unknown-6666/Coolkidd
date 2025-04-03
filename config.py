import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

# Bot configuration
DEFAULT_PREFIX = "!"
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("No Discord token found in environment variables")

# AI configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API", "AIzaSyC2s3PLPvGtfQloUfkyKmMSTULGob9NpAE")
USE_GOOGLE_AI = bool(GOOGLE_API_KEY)

# Bot owner and permission configuration
BOT_OWNER_IDS = (1003686821600960582, 1296213550917881856)  # Your Discord IDs
MOD_ROLE_IDS = [
    1259610617678135377, 1259606494719250492  # Moderator role ID
]

# YouTube channel configuration
YOUTUBE_CHANNELS = [

]
DEFAULT_ANNOUNCEMENT_CHANNEL = None  # Will be set when first announcement channel is configured

# Discord color scheme
COLORS = {
    "PRIMARY": 0x7289DA,    # Discord Blurple
    "SECONDARY": 0x99AAB5,  # Discord Grey
    "SUCCESS": 0x43B581,    # Discord Green
    "ERROR": 0xF04747,      # Discord Red
    "WARNING": 0xFAA61A,    # Warning/Orange
    "WHITE": 0xFFFFFF       # White
}

# Bot status messages
STATUS_MESSAGES = [
    "Looking for survivors"
]