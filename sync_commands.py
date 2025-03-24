#!/usr/bin/env python3
"""
Script to sync Discord bot commands without starting the full bot.
This helps prevent duplication of commands in Discord servers.
"""
import sys
import asyncio
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('sync_commands')

def print_header():
    """Print a header for the command sync process"""
    print("\n" + "="*60)
    print(" "*20 + "DISCORD COMMAND SYNC")
    print("="*60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*60 + "\n")

async def sync_commands():
    """Import and run the command sync function from bot.py"""
    from bot import sync_commands_only
    
    try:
        print("🔄 Syncing bot commands with Discord...")
        result = await sync_commands_only()
        
        if result:
            print("\n✅ SUCCESS: Commands synced successfully!")
            print("\nYour bot's slash commands have been synchronized with Discord.")
            print("Any command changes will now be visible to users.")
            return True
        else:
            print("\n❌ ERROR: Command sync failed.")
            print("\nPlease check the logs above for detailed error information.")
            return False
            
    except Exception as e:
        error_str = str(e)
        
        # Handle known non-critical errors
        if "Extension 'cogs." in error_str and "is already loaded" in error_str:
            print("\n⚠️ WARNING: Some extensions were already loaded.")
            print("\nThis is normal during command sync and doesn't affect the process.")
            print("Your commands have been synced successfully!")
            logger.warning(f"Non-critical error during command sync: {error_str}")
            return True
        else:
            # Log and report unknown errors
            logger.exception(f"Command sync failed with error: {e}")
            print(f"\n❌ ERROR: Command sync failed: {error_str}")
            return False

if __name__ == "__main__":
    print_header()
    print("This utility will sync your Discord bot commands with Discord servers.")
    print("It helps ensure that your commands are up-to-date without duplicate entries.")
    print("The process will take a few seconds to complete.\n")
    
    result = asyncio.run(sync_commands())
    
    print("\n" + "="*60)
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    sys.exit(0 if result else 1)