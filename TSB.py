from bs4 import BeautifulSoup
import requests
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def get_ip():
    url = requests.get('https://ifconfig.me')
    soup = BeautifulSoup(url.text,'lxml')
    ip = soup.text+':9987'
    return ip

vk_session = vk_api.VkApi(token='')
vk = vk_session.get_api()
long_p = VkBotLongPoll(vk_session,'213608305')
for event in long_p.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        mes = event.message['text']

        if mes.lower() =='':
            text = get_ip()
            vk.messages.send(
                peer_id = ,
                random_id=get_random_id(),
                message=text
            )