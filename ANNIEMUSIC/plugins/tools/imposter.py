from pyrogram import filters
from pyrogram.types import Message
from ANNIEMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from ANNIEMUSIC import app




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**𓆩♡𓆪 ᴘʀᴇᴛᴇɴᴅᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ 𓆩♡𓆪**
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ
**𓆩♡𓆪 ɴᴀᴍᴇ** 𓆩♡𓆪 {message.from_user.mention}
**𓆩♡𓆪 ᴜsᴇʀ ɪᴅ** 𓆩♡𓆪 {message.from_user.id}
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**𓆩♡𓆪 ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ 𓆩♡𓆪**
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ
**𓆩♡𓆪 ғʀᴏᴍ** 𓆩♡𓆪 {bef}
**𓆩♡𓆪 ᴛᴏ** 𓆩♡𓆪 {aft}
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**🪧 ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ 🪧**
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ
**𓆩♡𓆪 ғʀᴏᴍ** 𓆩♡𓆪 {bef}
**𓆩♡𓆪 ᴛᴏ** 𓆩♡𓆪 {aft}
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**𓆩♡𓆪 ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ 𓆩♡𓆪**
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ
**𓆩♡𓆪ғʀᴏᴍ** 𓆩♡𓆪 {bef}
**𓆩♡𓆪 ᴛᴏ** 𓆩♡𓆪 {aft}
ﮩ٨ـﮩﮩﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ﮩ٨ـﮩﮩ٨ـ\n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo("https://telegra.ph/file/58afe55fee5ae99d6901b.jpg", caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ : ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
