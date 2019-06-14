# dtb

![dtb logo](logo.svg)

DingTalk bot is a robot that post information to DingTalk group.

## Official Reference

Documents of DingTalk API is available [here](https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq).

## Usage

This project is under construction. There is only a rough run through.
Code is constructed and tested under *python 3*.
I will also try to adapt it with *python 2* later when we really have something running.

**MAKE SURE YOU UNDERSTAND THE DOCUMENTS [ABOVE](#official-reference) AND CODES PROVIDED IN THIS REPOSITORY, AND TRY IT AT YOUR OWN RISK!**

To try it, there are several steps:

1. Add Custom robot: DingTalk - Group - Group Setting - Group Robot - Add Robot - Custom - Add. Name it and give it a profile photo. Make sure you will not scare other members in the group during testing (and usage).

2. Get the `webhood`: Again go to Group Robot, in the list of Robot for this group, you should see the robot you just added. The `...` button on the right-side will lead you to the Settings page. You can update the settings for your robot. And more importantly, copy your `webhood` here.

3. Setup: Back to your workspace, copy the `config_sample.py` as `config.py` and create your config with your `webhood`. `WebhookConfig`, `BaseAuthConfig`, or `EnvironConfig`, either way would do.

4. Run: You are ready to set off.
```
python3 -m dtb
```
... and see? You just received a new message from the bot!
It should read
> **时代的火车向前开**
>
> 这个即将发布的新版本，创始人 ...

This is taken from [example](https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq#-5) in [official documnet](https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq).
Take a look at `dtb/__main__.py`, and you can play with it now.

## About DingTalk SDK

Do not use the DingTalk SDK python for the bot, because the functionality is not included in current release at all.
`get_dingtal_sdk.sh` is a script to fetch the SDK.
However, it is not used in this project.
I provide it here just because I did spend some minutes to write it.
