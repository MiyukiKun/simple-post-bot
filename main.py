from telethon import events, Button
from config import bot

@bot.on(events.NewMessage(pattern="/start"))
async def _(event):
    await event.reply("Make sure to add me to the channel you are trying to post in.")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('Message Text: ')
        txt = await conv.get_response()
        txt = txt.raw_text
        await conv.send_message('Button Link: ')
        link = await conv.get_response()
        link = link.raw_text
        await conv.send_message('Target Channel Id: ')
        cid = await conv.get_response()
        cid = cid.raw_text
        if not cid.startswith("-100"):
            cid = f"-100{cid}"

        msg = await bot.send_message(int(cid), f"`{txt}`", buttons=[Button.url(text="Click here to download", url=link)])
        await event.reply(f"Posted to channel\n\n t.me/c/{cid.replace('-100', '')}/{msg.id}")

bot.start()

bot.run_until_disconnected()