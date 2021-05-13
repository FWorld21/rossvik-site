#!/usr/bin/env python3

import telebot
from optparse import OptionParser


def message_for_study_comments():
    if options.website == '':
        msg = f'<b>Внимание!</b>\n\n' \
              f'<b>Пользователь:</b> <i>{options.name}</i>\n' \
              f'<b>К обучению:</b> <i>{options.subject}</i>\n\n' \
              f'<b>Оставил коментарий:</b> <i>{options.message}</i>\n\n' \
              f'<b>E-mail пользователя:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт пользователя:</b> <i>У пользователя отсутствует сайт</i>'
    else:
        msg = f'<b>Внимание!</b>\n\n' \
              f'<b>Пользователь:</b> <i>{options.name}</i>\n' \
              f'<b>К обучению:</b> <i>{options.subject}</i>\n\n' \
              f'<b>Оставил коментарий:</b> <i>{options.message}</i>\n\n' \
              f'<b>E-mail пользователя:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт пользователя:</b> <i>{options.website}</i>'
    return msg


def message_for_news_comments():
    if options.website == '':
        msg = f'<b>Внимание!</b>\n\n' \
              f'<b>Пользователь:</b> <i>{options.name}</i>\n' \
              f'<b>К новости:</b> <i>{options.subject}</i>\n\n' \
              f'<b>Оставил коментарий:</b> <i>{options.message}</i>\n\n' \
              f'<b>E-mail пользователя:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт пользователя:</b> <i>У пользователя отсутствует сайт</i>'
    else:
        msg = f'<b>Внимание!</b>\n\n' \
              f'<b>Пользователь:</b> <i>{options.name}</i>\n' \
              f'<b>К новости:</b> <i>{options.subject}</i>\n\n' \
              f'<b>Оставил коментарий:</b> <i>{options.message}</i>\n\n' \
              f'<b>E-mail пользователя:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт пользователя:</b> <i>{options.website}</i>'
    return msg


def message_for_question():
    msg = f'<b>Внимание!</b>\n\n' \
          f'<b>Пользователь:</b> <i>{options.name}</i>\n' \
          f'<b>К теме:</b> <i>{options.subject}</i>\n\n' \
          f'<b>Написал сообщение:</b> <i>{options.message}</i>\n\n' \
          f'<b>E-mail пользователя:</b> <i>{options.email}</i>'
    return msg


parser = OptionParser()
parser.add_option('-n', '--name', dest='name',
                  help='Name', metavar='NAME')
parser.add_option('-e', '--email', dest='email',
                  help='Email', metavar='EMAIL')
parser.add_option('-s', '--subject', dest='subject',
                  help='Subject', metavar='SUBJECT')
parser.add_option('-m', '--message', dest='message',
                  help='Message', metavar='MESSAGE')
parser.add_option('-w', '--website', dest='website',
                  help='Web-Site', metavar='WEBSITE')
parser.add_option('-o', '--option', dest='option',
                  help='comments or question', metavar='OPTION')

(options, args) = parser.parse_args()

with open('bot_engine/api.txt', 'r') as apifile:
    bot = telebot.TeleBot(apifile.read())

with open('bot_engine/chat_id.txt', 'r') as chat_id:
    if options.option == 'news_comments':
        bot.send_message(chat_id=chat_id.read(), text=message_for_news_comments(), parse_mode='html')
    elif options.option == 'question':
        bot.send_message(chat_id=chat_id.read(), text=message_for_question(), parse_mode='html')
    elif options.option == 'study_comments':
        bot.send_message(chat_id=chat_id.read(), text=message_for_study_comments(), parse_mode='html')
