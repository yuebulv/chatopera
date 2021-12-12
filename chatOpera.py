from chatopera import Chatopera, Chatbot
import json
# 管理 BOT CLENT: 创建 ，删除，查看
admin = Chatopera(access_token="ucbdfe1966ec48c274eebdd75c98d121b4d1b3a770b6b93b53f5c4acdd4478d36",
    provider='https://bot.chatopera.com')
# BOT CLIENT
bot = Chatbot(app_id="61b5a42e2d17650013759adc",
        app_secret="62a0c5e60a6bc8d3e0b9d104a39ad645",
        provider='https://bot.chatopera.com')

# res = bot.command('Get', '/')
# print(res)

# # update bot
# body = {
#  "fallback": "请联系客服。",
#  "description": "我的超级能力是对话",
#  "welcome": "你好，我是机器人小巴巴"
# }
# bot.command('PUT', '/', body)
# res = bot.command('Get', '/')
# res = json.dumps(res, indent=4, ensure_ascii=False)
# print(res)

# 对话检索
body = {
    "fromUserId": "{{userId}}",
    "textMessage": "岩土考试时间",
    "faqBestReplyThreshold": 0.6,
    "faqSuggReplyThreshold": 0.35,
    "extras": {}
}
res = bot.command("POST", "/conversation/query", body)
res = json.dumps(res, indent=4, ensure_ascii=False)
print(res)

# 知识库检索
body = {
 "query": "如何查看快递单号",
 "fromUserId": "{{userId}}",
 "faqBestReplyThreshold": 0.8,
 "faqSuggReplyThreshold": 0.8
}

res = bot.command("POST", "/faq/query", body)
res = json.dumps(res, indent=4, ensure_ascii=False)
print(res)

# # 创建问答对
# body = {
#  "post": "如何查看快递单号",
#  "replies": [
#   {
#    "rtype": "plain",
#    "content": "foo",
#    "enabled": True
#   },
#   {
#    "rtype": "plain",
#    "content": "bar",
#    "enabled": True
#   }
#  ],
#  "enabled": True,
#  "categoryTexts": [
#   "一级分类名",
#   "二级分类名"
#  ]
# }
#
# res = bot.command("post", "/faq/database", body)