# coding=utf-8

import os
import time
import re
import sys

# ====================Function()====================
# ƥ���ַ����е���֤�루6λ���֣�


def match_vercode(str_msg):
    ver_code = re.search("\d{6}", str_msg, 0)
    return ver_code.group()


# adbʶ���ֻ��Ƿ�������
def is_connect_adb():
    cmd_adb = "adb devices"
    content = os.popen(cmd_adb).read()
    default_adb_devices = "List of devices attached"
    return (content.strip() != "List of devices attached")


# ��ȡ������֤�룬Ĭ�ϳ�ʱ20��
def get_code_from_mms(timeout=10):
    os.system("adb logcat -c")

    # ִ��cmd��ȡ�յ��Ķ�������
    cmd = "adb logcat -d | findstr /C:\"message content is \""

    num = 0
    while num < timeout:
        msg_content = os.popen(cmd).read()
        print(msg_content)

        # ���Զ�������
        # if num == 5:
        #    msg_content = "D/PPL/PplSmsFilterExtension( 1185): pplFilter: message content is ��֤�룺708933"

        if msg_content != "":
            #msg_content = matchVercode(msg_content)
            print("code is {}:".format(msg_content))
            break
        else:
            time.sleep(1)
            num += 1
            print('�ѵȴ�:{}��'.format(num))
            continue

    if num == timeout:
        print("�ȴ���ʱ�����Ž���ʧ�ܡ�")


# ====================����====================
# �ж��Ƿ���timeout������û����ִ��Ĭ��
def run_get_code(list):
    length = len(list)
    if length == 2:
        get_code_from_mms(list[1])
    else:
        get_code_from_mms()


# ���ж�adb�Ƿ����������������д��롣
if(is_connect_adb()):
    print("adb������������ʼ�ȴ���ȡ������֤�룡")
    run_get_code(sys.argv)
else:
    print("Android�豸adb���������⣬��cmd����\"adb devces\"������¼���豸���ӡ�")
