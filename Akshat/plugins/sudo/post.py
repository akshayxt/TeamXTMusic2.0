from pyrogram import Client, filters
from Akshat import app
from config import OWNER_ID, BOT_USERNAME
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command(["post","anu daal do"], prefixes=["/", ".","j"]) & filters.user(OWNER_ID))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = -1002001578721
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("𝐓𝐄𝐀𝐌冬𝗫𝗧",  url=f"https://t.me/teamxt_support"),
                 InlineKeyboardButton("𝐓𝐄𝐀𝐌冬𝗫𝗧 𝐒𝐔𝐏𝐏𝐎𝐑𝐓",url=f"https://t.me/TeamX_TSupport")],
                [InlineKeyboardButton("𝐀𝐍𝐕𝐈冬𝗫𝗧", url=f"https://t.me/AnviXTRobot"),
                 InlineKeyboardButton("Co-𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/Subhi_love")]
            ]
        )
        
        await message.reply_to_message.copy(destination_group_id, reply_markup=buttons)
        await message.reply("ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ ")
