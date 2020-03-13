# -*- coding: utf-8 -*-
from data import db_session
from data.users import User
from data.news import News
import datetime

db_session.global_init("db/blogs.sqlite")

user = User()
user.name = "РџРѕР»СЊР·РѕРІР°С‚РµР»СЊ 3333"
user.about = "Р±РёРѕРіСЂР°С„РёСЏ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ 3333"
user.email = "CC@email.ru"
session = db_session.create_session()
session.add(user)
session.commit()
user = session.query(User).first()
user = session.query(User).filter(User.id == 1).first()
user.name = "РР·РјРµРЅРµРЅРЅРѕРµ РёРјСЏ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ"
user.created_date = datetime.datetime.now()
session.commit()
news = News(title="РџРµСЂРІР°СЏ РЅРѕРІРѕСЃС‚СЊ", content="РџСЂРёРІРµС‚ Р±Р»РѕРі!", 
            user_id=1, is_private=False)
session.add(news)
session.commit()
user = session.query(User).filter(User.id == 1).first()
news = News(title="Р’С‚РѕСЂР°СЏ РЅРѕРІРѕСЃС‚СЊ", content="РЈР¶Рµ РІС‚РѕСЂР°СЏ Р·Р°РїРёСЃСЊ!", 
            user=user, is_private=False)
session.add(news)
session.commit()
user = session.query(User).filter(User.id == 1).first()
news = News(title="Р›РёС‡РЅР°СЏ Р·Р°РїРёСЃСЊ", content="Р­С‚Р° Р·Р°РїРёСЃСЊ Р»РёС‡РЅР°СЏ", 
            is_private=True)
user.news.append(news)
session.commit()
