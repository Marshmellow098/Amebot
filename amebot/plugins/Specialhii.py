from userbot.utils import amebot_cmd

@borg.on(amebot_cmd(pattern=r"hii ?(.*)"))
async def hii(event):
    giveVar = event.text
    ame = giveVar[5:6]
    if not ame:
        ame = "🌺"
    me = giveVar[7:8]
    if not me:
        me = "✨"
    await event.edit(
        f"{ame}{me}{me}{ame}{me}{ame}{ame}{ame}\n{ame}{me}{me}{ame}{me}{me}{ame}{me}\n{ame}{ame}{ame}{ame}{me}{me}{ame}{me}\n{ame}{me}{me}{ame}{me}{me}{ame}{me}\n{ame}{me}{me}{ame}{me}{ame}{ame}{ame}\n☁☁☁☁☁☁☁☁"
    )
