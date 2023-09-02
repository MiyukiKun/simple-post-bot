from telethon import events, Button
from config import bot

@bot.on(events.NewMessage(pattern="/start"))
async def _(event):
    await event.reply("Make sure to add me to the channel you are trying to post in.")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('Message Text: ')
        txt = await conv.get_response()
        txt = txt.raw_text
        await conv.send_message('How many rows of buttons you want?')
        r = await conv.get_response()
        r = int(r.raw_text)
        await conv.send_message('How many colunms of buttons you want?')
        c = await conv.get_response()
        c = int(c.raw_text)
        buttons = []
        for i in range(r):
            temp = []
            for j in range(c):
                await conv.send_message(f'Button row:{i+1} col:{j+1} Text: ')
                btxt = await conv.get_response()
                btxt = btxt.raw_text
                await conv.send_message(f'Button row:{i+1} col:{j+1} Link: ')
                link = await conv.get_response()
                link = link.raw_text
                temp.append(Button.url(text=btxt, url=link))
            buttons.append(temp)
        await conv.send_message('Target Channel Id: ')
        cid = await conv.get_response()
        cid = cid.raw_text
        if not cid.startswith("-100"):
            cid = f"-100{cid}"

        msg = await bot.send_message(int(cid), f"`{txt}`", buttons=buttons)
        await event.reply(f"Posted to channel\n\n t.me/c/{cid.replace('-100', '')}/{msg.id}")


@bot.on(events.NewMessage(pattern="/edit"))
async def _(event):
    await event.reply("Make sure to add me to the channel you are trying to edit in.")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message('Message Link: ')
        mlink = await conv.get_response()
        msgid = int(mlink.raw_text.split("/")[-1])
        await conv.send_message('Channel Id: ')
        cid = await conv.get_response()
        cid = cid.raw_text
        if not cid.startswith("-100"):
            cid = f"-100{cid}"
        await conv.send_message('How many rows of buttons you want?')
        r = await conv.get_response()
        r = int(r.raw_text)
        await conv.send_message('How many colunms of buttons you want?')
        c = await conv.get_response()
        c = int(c.raw_text)
        buttons = []
        for i in range(r):
            temp = []
            for j in range(c):
                await conv.send_message(f'Button row:{i+1} col:{j+1} Text: ')
                btxt = await conv.get_response()
                btxt = btxt.raw_text
                await conv.send_message(f'Button row:{i+1} col:{j+1} Link: ')
                link = await conv.get_response()
                link = link.raw_text
                temp.append(Button.url(text=btxt, url=link))
            buttons.append(temp)
        
        m = await bot.get_messages(int(cid), ids=msgid)
        await m.edit(buttons=buttons)
        await event.reply(f"Edited Successfully:\n{mlink.raw_text}")


bot.start()

bot.run_until_disconnected()