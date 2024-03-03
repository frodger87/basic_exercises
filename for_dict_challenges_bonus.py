"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import datetime
import random
import uuid

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def count_values(messages: list, target_field: str) -> dict:
    count_values = {}
    for message in messages:
        if message[target_field] not in count_values:
            count_values[message[target_field]] = 1
        else:
            count_values[message[target_field]] += 1
    return count_values


def key_for_max_value(target_dict):
    target_key = ''
    max_value = 0
    for key, value in target_dict.items():
        if target_dict[key] > max_value:
            target_key = key
            max_value = target_dict[key]
    return target_key


def count_replies(messages: list):
    replies = []
    user_message_replies = {}

    for message in messages:
        if message['reply_for']:
            replies.append(message['reply_for'])
            user_message_replies[message['sent_by']] = 0

    for message in messages:
        if message['id'] in replies:
            user_message_replies[message['sent_by']] += 1

    return user_message_replies


print()

if __name__ == "__main__":
    chat_history = generate_chat_history()
    # print(generate_chat_history())
    user_count_messages = count_values(chat_history, 'sent_by')
    print(
        f'Наибольшее число сообщений у пользователя id = {key_for_max_value(user_count_messages)}')
    print(
        f'Наибольшее число ответов на сообщение пользователя id = {key_for_max_value(count_replies(chat_history))}')
