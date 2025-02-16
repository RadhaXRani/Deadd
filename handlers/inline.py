from pyrogram import Client, filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

async def inline_query(client, query: InlineQuery):
    results = [
        InlineQueryResultArticle(
            title="YouTube डाउनलोडर",
            description="YouTube लिंक से ऑडियो या वीडियो डाउनलोड करें",
            input_message_content=InputTextMessageContent(
                message_text="कृपया YouTube लिंक भेजें।"
            )
        )
    ]
    await query.answer(results, cache_time=1)

inline_query_handler = filters.inline_query(inline_query)
