#!/bin/bash

TMP_NAME=dingtalk_sdk_python.zip
# SDK download link refers from: https://open-doc.dingtalk.com/microapp/faquestions/vzbp02
wget http://open-dev.dingtalk.com/download/openSDK/python -O /tmp/$TMP_NAME
TMP_NESTED_NAME=$(unzip -l /tmp/$TMP_NAME "taobao-sdk-PYTHON-auto*" | awk 'FNR == 4 {print $NF}')
unzip $TMP_NAME $TMP_NESTED_NAME -d /tmp
unzip /tmp/$TMP_NESTED_NAME -d "dingtalk-sdk-python"
export PYTHONPATH=.:./dingtalk_sdk_python:$PYTHONPATH
