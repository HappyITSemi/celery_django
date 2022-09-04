import time

from django.http import HttpResponse
from celery import shared_task
import logging

logger = logging.getLogger('django')


@shared_task
def tel_exec(message):  # 裏側で実行される処理
    print('tel_exec ---')
    logger.info('tel_exec ---')
    time.sleep(1)  # 1秒待機する
    print(message)


@shared_task
def mail_exec(message):
    print('mail_exec ---')
    logger.info('mail_exec ---')
    time.sleep(1)
    print(message)


@shared_task
def sam_exec(message):
    print('sam_exec ---')
    logger.info('sam_exec ---')
    time.sleep(1)
    print(message)


def task_1(request):  # 本処理
    msg_tel = '1/3 非同期処理-->tel'
    msg_mail = '2/3 非同期処理-->mail'
    msg_sam = '3/3 非同期処理-->mail'
    tel_exec.delay(msg_tel)
    mail_exec.delay(msg_mail)
    sam_exec.delay(msg_sam)
    return HttpResponse('パイプ--> workerへ --->3 task', status=202)


def task_2(request):
    msg_2 = '1-1パイプに入れる-->sam'
    sam_exec.delay(msg_2)
    return HttpResponse('パイプ --->only sam', status=202)
