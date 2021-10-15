import asyncio
from random import choice, randint

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import get_user_from_event
from . import ALIVE_NAME

plugin_category = "fun"


@jmthon.ar_cmd(
    pattern="فيك(?:\s|$)([\s\S]*)",
    command=("فيك", plugin_category),
    info={
        "header": "To show fake actions for a paticular period of time",
        "description": "if time is not mentioned then it may choose random time 5 or 6 mintues for mentioning time use in seconds",
        "usage": [
            "{tr}فيك <action> <time(in seconds)>",
            "{tr}فيك <action>",
            "{tr}scam",
        ],
        "examples": "{tr}scam photo 300",
        "actions": [
        "typing",
        "contact",
        "game",
        "location",
        "voice",
        "round",
        "video",
        "photo",
        "document",

        ],
    },
)
async def _(event):
    options = [
        "typing",
        "contact",
        "game",
        "location",
        "voice",
        "round",
        "video",
        "photo",
        "document",

    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:
        scam_action = choice(options)
        scam_time = randint(300, 360)
    elif len(args) == 1:
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(300, 360)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:
        try:
            scam_action = str(args[0]).lower()
            scam_time = int(args[1])
        except ValueError:
            return await edit_delete(event, "`Invalid Syntax !!`")
    else:
        return await edit_delete(event, "`Invalid Syntax !!`")
    try:
        if scam_time > 0:
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await asyncio.sleep(scam_time)
    except BaseException:
        return


@jmthon.ar_cmd(
    pattern="رفع ادمن$",
    command=("رفع ادمن", plugin_category),
    info={
        "header": "Fun animation for faking user promotion",
        "description": "An animation that shows enabling all permissions to him that he is admin(fake promotion)",
        "usage": "{tr}padmin",
    },
    groups_only=True,
)
async def _(event):
    "Fun animation for faking user promotion."
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "`جارِ ترقيتك.......`")
    animation_chars = [
        "**تحويل ملكية المجموعة الى المستخدم...**",
        "**اعطاء كافة الصلاحيات الى المستخدم...**",
        "**(1) ارسال الرسائل: ☑️**",
        "**(1) ارسال الرسائل: ✅**",
        "**(2) ارسال الوسائط: ☑️**",
        "**(2) ارسال الوسائط: ✅**",
        "**(3) ارسال الملصقات & المتحركات: ☑️**",
        "**(3) ارسال الملصقات & المتحركات: ✅**",
        "**(4) ارسال الاستفتاء: ☑️**",
        "**(4) ارسال الاستفتاء: ✅**",
        "**(5) حظر المستخدمين: ☑️**",
        "**(5) حظر المستخدمين: ✅**",
        "**(6) اضافة عضو: ☑️**",
        "**(6) اضافة عضو: ✅**",
        "**(7) تثبيت الرسائل: ☑️**",
        "**(7) تثبيت الرسائل: ✅**",
        "**(8) تغير معلومات المجموعة: ☑️**",
        "**(8) تغير معلومات المجموعة: ✅**",
        "**تم ترقيتك بنجاح ✅**",
        f"**لقد تم رفعك مالك المجموعة من قبل: {ALIVE_NAME}**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])
#Jepthon @lMl10l
