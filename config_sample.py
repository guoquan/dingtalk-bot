from dtb.config import WebhookConfig, BaseAuthConfig, EnvironConfig

config = WebhookConfig("https://oapi.dingtalk.com/robot/send?access_token=xxx")

config = BaseAuthConfig("https://oapi.dingtalk.com/robot/send",
                        access_token="xxxx")

config = EnvironConfig[WebhookConfig]('DINGTALK_WEBHOOK')
