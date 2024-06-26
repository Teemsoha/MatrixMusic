import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from MatrixMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "تفعيل", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a3f0b02ae0a5f2374d909.jpg",
        caption=f"""<b> ❆︙مرحباً بك عزيزي</b>\n\n<b>❆︙استخدم الازرار بالاسفل ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر التشغيل ›", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر القناة ›", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "‹ اوامر الادمن ›", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر المطور ›", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "‹ ليطمـ𓆰ٰ⍣⃟ٰٰٖٖ۪۬🇾🇪۬ـئن عقلـ۬ۦٕ٘۬ﹻٰ۬ۛۛـي� ›", url="https://t.me/My1mind1"),
                ],
            ]
        ),
    )


@app.on_message(command(["مطور", "المبرمج"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>- - - - - - - - - - - - - - - - - -</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :{usr.first_name}
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :{usr.id}
 </b>- - - - - - - - - - - - - - - - - -</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("ليطمـ𓆰ٰ⍣⃟ٰٰٖٖ۪۬🇾🇪۬ـئن عقلـ۬ۦٕ٘۬ﹻٰ۬ۛۛـي�", url="https://t.me/My1mind1"),
            ],
          ]
       )                 
    )                    
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
