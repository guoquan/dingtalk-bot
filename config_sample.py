from dtb.config import WebhookConfig, BaseAuthConfig

config = WebhookConfig("https://oapi.dingtalk.com/robot/send?access_token=xxx")

config = BaseAuthConfig("https://oapi.dingtalk.com/robot/send",
                        access_token="xxxx")
