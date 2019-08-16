# -*- coding: utf-8 -*-

"""
Created on Mon May  6 10:45:55 2019

@author: hp
"""

########################################################################
######### CHAT BOT VARIABLES
########################################################################

# Import Modules

from flask import Flask, request, jsonify
from datetime import datetime

import sys
import os
import json

import mysql.connector
import datetime
import time

from dateutil import relativedelta
import random
import requests

import urllib.request
from bs4 import BeautifulSoup

import re
# Define Messages

all_okay_message = """
All Okay.
"""

wrong_customer_message = """
申し訳ありませんが、そのようなお客様は見つかりませんでした。 
登録時に使用した正しい名前とEメールを入力してください。
"""

welcome_message = """
こんにちは。アプリ登録ありがとうございます。
私の名前はミライです。
私は、あなた専属の美容コンシェルジュです。
サロンの予約受付は私が行います。
さらに、サロンのこと、美容のこと、
わからないことがあれば何でも解決策を考えます。
知りたい情報はいち早くお伝えいたします。
あなたの人生が楽しく、そして快適に過ごせるように・・・
全力でお手伝いいたします。
どうぞよろしくお願いいたします。
"""

ask_lastname_message_1 = """
あなたのお名前を教えてください。
"""

ask_lastname_message_2 = """
姓
"""

ask_firstname_message = """
名
"""

is_nickname_message_1 = """
とっても可愛いお名前ですね。
"""

is_nickname_message_2 = """
ニックネームはありますか？
"""

ask_nickname_message = """
ニックネームは何ですか？
"""

ask_birthday_message_1 = """
いいですね。ありがとうございました{0}。
今後も仲良くしてください。
"""

ask_birthday_message_2 = """
あなたの誕生日に特別なメッセージをお送りできたらと思います。
お誕生日を教えていただけますか {0}？
"""

ask_birthday_without_nickname_message = """
あなたの誕生日に特別なメッセージをお送りできたらと思います。
お誕生日を教えていただけますか？
"""


ibis_message_1 = """
そうなんですね。あなたは{0}ですね。

今日の{1}の運勢は....

{2}
"""

ibis_message_2 = """
あなたは星座占いを信じますか？
"""

is_daily_horoscope_message = """
いいですね！星座占いが毎日配信されるとしたら、
興味はありますか？						
"""						
						
iss_nbis_message_1 = """
わかりました。
"""

iss_ndh_message_1 = """
わかりました。
"""

iss_ydh_message_1 = """
わかりました。
ではあなたのために毎日の運勢を配信しますね！
"""

is_specific_salon_message_2 = """
ありがとうございます。ちなみにお気に入りでよく利用するサロンはありますか？							
"""							
is_specific_salon_message = """
ありがとうございます。ちなみにお気に入りでよく利用するサロンはありますか？
"""

ask_specific_salon_message = """
おぉいいですね！
あなたのお気に入りのサロンを教えてください。
"""

ask_salon_again_message = """
そうでしたか...もう一度、入力してもらえますか？
"""

use_recommended_salon_message = """
すみません。名前の入力のエラーかそのサロンにMiraiが導入されていないので、
あなたのサロンを見つけることができませんでした。もし良ければおすすめのサロンをご紹介しましょうか？
"""

confirm_specific_salon_message_1 = """
ありがとうございます。
"""
confirm_specific_salon_message_2 = """
あなたのお気に入りのサロンはここですか？
"""

ask_if_alt_salon_message_1 = """
。。月。。日でしたら、
このサロンをオススメします。
"""


ask_if_alt_salon_message_2 = """
。。月。。日でしたら、
このサロンをオススメします。
"""

is_confirm_message = """
予約を確定してよろしいですか？
"""

wrong_is_nickname_message = """
ニックネームがあるかどうかについて有効な応答を入力してください。
はいの場合は1、いいえの場合は2を押します。
"""

wrong_is_reservation_now_message = """
今すぐ予約するかどうかの有効な回答を入力してください。
「はい」の場合は1、「いいえ」の場合は2を押します。
"""

wrong_is_time_for_more_message = """
他に質問があるかどうかについて、有効な回答を入力してください。
はいの場合は1、いいえの場合は2を押します。 
"""

wrong_is_confirm_message = """
確認するかどうかについて有効な回答を入力してください。
はいの場合は1、いいえの場合は2を押します。 
"""

wrong_cust_type_of_salon_message = """
表示されたオプションから有効な種類のサロンを入力してください。 
"""

wrong_cust_service_message = """
表示されたオプションから有効なサービスを入力してください。    
"""

wrong_cust_avail_options_message = """
表示されたオプションから有効なスタッフと時間を選択してください。 
"""

wrong_cust_sub_service_message = """
表示されたオプションから有効なメニュー項目を入力してください。
"""

ask_alt_time_message = """
何時がいいですか？ 
"""

ask_alt_date_message = """
で施術可能な日付はこちらです 
"""

ask_free_days_message = """
ありがとうございます。
どんな日にサロンを利用することが多いですか？
"""

ask_free_days_message_1 = """
ありがとうございます。{0}はいつ自由な時間がありますか？
あなたにぴったりな美容サロンの情報をお届けするために、教えてください。
"""

ask_free_days_message_2 = """
あなたが時間をとれるのいつですか？
"""

ask_free_days_message_wo_nn_1 = """
ありがとうございます。はいつ自由な時間がありますか？
あなたにぴったりな美容サロンの情報をお届けするために、教えてください。
"""

ask_free_time_message = """
いいですね。では詳しく時間帯を教えてください。
"""

ask_often_service_message = """
ありがとうございます。どんなサロンを利用することが多いですか？
"""

chat_more_message_1 = """
おぉいいですね。ありがとうございます。
"""

chat_more_message_2 = """
今、何か仕事をしていますか？
"""

is_time_for_more_message = """
そうなんですね。
もう少し質問に答えていただける時間はありますか？
"""

is_time_for_more_2_message_1 = """
わかりました。
予約をとりたいときはいつでも知らせてください。
"""

is_time_for_more_2_message_2 = """
質問に答える時間はまだありますか？
もう少し質問に答えていただける時間はありますか？
"""

is_time_for_more_message_1 = """
そうなんですね。
"""

is_time_for_more_message_2 = """
もう少し質問に答えていただける時間はありますか？
"""

ask_phone_nbis_message_1 = """
わかりました。
"""

ask_phone_ndh_message_1 = """
わかりました。
"""

ask_phone_ydh_message_1 = """
わかりました。
ではあなたのために毎日の運勢を配信しますね！
"""

ask_phone_message_2 = """
ありがとうございます。
電話番号を教えてください。
"""

ask_phone_message_salon_found_1 = """
素敵ですね。では今から常にそのサロンの予約をお取りしますね
"""

ask_phone_message_salon_not_found_1 = """
あぁ、このサロンにはまだMiraiが導入されていないようですね。利用してもらえるよう伝えてもらえますか
現在はMajestic Beautyで予約する予定です。
"""

find_salon_message = """
おぉ、ではあなたにとってベストなサロンを探していきましょう。
"""

#CHANGE_TEL
ask_phone_message_2 = """
あなたの電話番号を教えてください。
サロンから緊急連絡がある際の連絡に使用します。
"""

#ask_phone_message_2 = """
#あなたのメールアドレスを教えてください。
#"""


ask_phone_message_1 = """
ありがとうございます。
"""

ask_color_message_1 = """
ありがとうございます。
"""

ask_color_message_2 = """
{0}、何色がお好きですか？
"""

ask_color_without_nickname_message_1 = """
ありがとうございます。
"""

ask_color_without_nickname_message_2 = """
何色がお好きですか？
"""

ask_hobbies_message_1 = """
いい色ですよね。このカラーを選んだあなたの特徴は
{0} 
"""
ask_hobbies_message_2 = """
あなたの趣味は何ですか？
"""

confirmed_message = """
あなたの予約は確認されました。 あなたの予約番号は：{0}

今後も様々なご要望にお応えしていきます。
ぜご予約を取りたい時など、何かありましたら、お知らせください。

もう少し質問に答えていただける時間はありますか？
"""

confirmed_without_more_message = """
あなたの予約は確認されました。 あなたの予約番号は：{0}

今後も様々なご要望にお応えしていきます。
ぜご予約を取りたい時など、何かありましたら、お知らせください。
"""

ask_hair_frequency_message = """
どれくらいの頻度でそのサロンを利用しますか？
ヘアサロン:
"""

ask_aesthetic_frequency_message = """
どれくらいの頻度でそのサロンを利用しますか？
エステサロン:
"""

ask_nails_frequency_message = """
どれくらいの頻度でそのサロンを利用しますか？
ネイルサロン:
"""

ask_eyelash_frequency_message = """
どれくらいの頻度でそのサロンを利用しますか？
アイラッシュサロン:
"""

ask_relaxation_frequency_message = """
どれくらいの頻度でそのサロンを利用しますか？
リラクゼーションサロ:
"""

ask_email_message_1 = """
ありがとうございます。
"""
ask_email_message_2 = """
ではあなたのアドレスも教えてもらえますか？
"""
#ask_email_message = """
#あぁ忘れていました！{0}のメールアドレスを教えてください
#"""

ask_email_wo_nn_message = """
あぁ忘れていました！のメールアドレスを教えてください
"""

ask_home_address_message_1 = """
ありがとうございます。あなたにとって最適なサロンを探すために教えてほしいことがあります
"""

ask_home_address_message_2 = """
もし良ければご自宅の住所を教えてください。
おおまかな住所、最寄駅でも構いません。
"""


ask_home_address_is_working_message = """
ありがとうございます
あなたにとって最適なロケーションのサロンをお探しするために、
もし良ければ、あなたのご自宅の住所と会社の住所を教えてもらえませんか？
もし会社の住所がわからなければ、おおまかな住所、最寄駅でも構いません。
私の役割は、あなたにとってベストなサロンを探すこと。
あなたのライフスタイルをより快適にすることです。
"""


ask_home_address_not_working_message = """
ありがとうございます
あなたにとって最適なロケーションのサロンをお探しするために、
もし良ければ、あなたのご自宅の住所を教えてもらえませんか？
"""

#ask_home_address_message_2 = """
#ご自宅の住所:
#"""

ask_work_address_message = """
ありがとうございます
お勤め先の住所:
"""

red_idea = """
個性的でありたい、目立ちたい願望が強く、好奇心旺盛。少し感情的になる面もあるため、自生が必要なときもある。
面倒見がよくリーダーシップを発揮し、行動的でみんなから慕われます。根が楽天的で、細かいところは気にしなくておおざっぱです。
外見的が物静かに見える人でも落ち着いた外見とは裏腹に激しい情熱や欲望を秘めています。
"""

orange_idea = """
陽気で社交的な性格。
物事にあまりこだわらず、諦めが早い。温かい心の持ち主で、人なつっこく、誰からも愛される人柄。
人生に対して常に意欲的で、かなりの社交家です。人が集まる場所では常に注目のまとになるでしょう。
"""


yellow_idea = """
明るく、話し上手で表現力豊かな人です。好奇心旺盛で、つねに新しいことを求めている個性派。
社交的でユーモアのセンスも抜群なので、人の輪の中心にいるタイプです。
明るく可愛い、天真爛漫な性格。知的なのに子供っぽく、ユーモアセンスがあるので、人から好かれやすい。
"""

green_idea = """
基本的に穏やかで、何事においても堅実さが際立ち、我慢強さもあります。手堅く成功をおさめるタイプと言えるでしょう。
忍耐強く、優しい性格。争いごとを好まず、穏やかな日常を願う。
礼儀正しく、決して人の道を踏み外さない人。
人と協調したいので自己主張が弱く、優柔不断な面も見られます
"""

purple_idea = """
冷静で理知的、一つの枠の中で自制できる従順さを持っています。
理知的で誠実、控えめな内向的な性格。どんなことにも感情的にならず、冷静に物事を判断できる。
自制心はありますが、内向的で保守的な面もあり、自分の考え方は常に正しいと思っている事が多いようです。
整理整頓が得意で、創造性に富み、内向的な人が好む傾向があります。
"""

pink_idea = """
どんなときでも大きな心で受け止める愛情深い人。
優しく穏やかなロマンチスト。
デリケートで傷つきやすく人のちょっとした言葉や態度に、いつまでもくよくよしがちです。
"""

brown_idea = """
責任感があり、チームワークを作り出す特技を持っているのが特徴
自己表現が下手な人が多い。自分を犠牲にして他人に尽くすタイプ。
"""

gray_idea = """
優柔不断で自己中心的な性格。だれとでも調子を合わせることができ、自分を主張しない反面、人から干渉されることを嫌う。
感情をあまり表面に出さないので、クールでおとなしい人と見られる。
"""

white_idea = """
気高く、つねに完璧を求めて努力するタイプ。
純粋で誠実、潔癖、真面目で、素直、無邪気な性格
"""

black_idea = """
感情を溜め込む傾向があり、子供っぽいことが嫌いで、クールで大人な自分をアピールする。
人から命令されたり、強制されることを嫌う。プライドを傷つけられることを好まない面を持つ
意思が強く、少し頑固。いつも情熱を抑えている人。人を動かす才能はあるけれど、明るさと素直さに欠ける面も。
"""

blue_idea = """
冷静で理知的、一つの枠の中で自制できる従順さを持っています。
理知的で誠実、控えめな内向的な性格。どんなことにも感情的にならず、冷静に物事を判断できる。
"""


ask_type_of_salon_message_1 = """
ありがとうございます。
"""

ask_type_of_salon_message_2 = """
どんな美容サロンが好きですか？
"""

new_welcome_message_1 = """
おかえりなさい {0}
"""
new_welcome_message_2 = """
今日は何をお手伝いしましょうか？
"""

new_welcome_without_nickname_message_1 = """
おかえりなさい
"""

new_welcome_without_nickname_message_2 = """
今日は何をお手伝いしましょうか？
"""

is_reservation_now_message_1 = """
わかりました。
お客様の期待に答えられるように、努めてまいります。
"""

is_reservation_now_message_2 = """
次回予約をお取りしましょうか？
"""

ask_date_message_1 = """
かしこまりました。
"""

ask_date_message_2 = """
ご予約のお日にちはいつがよろしいですか？
"""

ask_service_message = " メニューはお決まりですか？"

empty_name_message = """
正しい名前を入力してください。 
"""

empty_nickname_message = """
正しいニックネームを入力してください。
"""

empty_phone_message = """
正しい電話番号を入力してください。
"""
wrong_color_message = """
色の正しいオプションを選択してください。  
"""

wrong_hobby_message = """
あなたの趣味として何かを入力してください。
"""


wrong_service_message = """
正しいサービスを選択してください。
"""

wrong_date_message = """
正しい形式で正しい日付を入力してください。
例：2019年6月21日の場合は、次のいずれかを入力します。

06月21日
"""

wrong_time_message = """
正しい形式で時間を入力してください。
例：午後1時に13:00と入力
"""

def create_sql_conn():
    mydb = mysql.connector.connect(
                                   host="34.85.64.241",
                                   user="jts",
                                   passwd="Jts45678@?",
                                   database="jtsboard_jts",
                                   buffered=True
                                   )
    #mycursor = mydb.cursor(buffered=True)
    mycursor = mydb.cursor()
    return mydb,mycursor

slot_list = ["00:00:00","00:30:00","01:00:00","01:30:00","02:00:00","02:30:00","03:00:00","03:30:00",
             "04:00:00","04:30:00","05:00:00","05:30:00","06:00:00","06:30:00","07:00:00","07:30:00",
             "08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00",
             "12:00:00","12:30:00","13:00:00","13:30:00","14:00:00","14:30:00","15:00:00","15:30:00",
             "16:00:00","16:30:00","17:00:00","17:30:00","18:00:00","18:30:00","19:00:00","19:30:00",
             "20:00:00","20:30:00","21:00:00","21:30:00","22:00:00","22:30:00","23:00:00","23:30:00"]

zodiac_jap_to_eng = { 
    "牡羊座" : "aries",
    "牡牛座":"taurus",
    "双子座":"gemini",
    "蟹座":"cancer",
    "獅子座":"leo",
    "乙女座":"virgo",
    "天秤座":"libra",
    "蠍座":"scorpio",
    "射手座": "sagittarius",
    "山羊座":"capricorn",
    "水瓶座":"aquarius",
    "魚座":"pisces"
}


def failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses):
    return_dict["status"] = "failure"
    return_dict["error_msg"] = out_msg
    return_dict["chat"] = return_list_of_dicts
    update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
    out_json = json.dumps(return_dict,ensure_ascii= False)
    return out_json


def get_zodiac(birth_day_obj):
    month = birth_day_obj.month
    day = birth_day_obj.day
    birth_day_tuple = (month,day)

    print("birth_day_tuple")
    print(birth_day_tuple)
    if (3,21) <= birth_day_tuple <= (4,19): 
        zodiac = "牡羊座"
    if (4,20) <= birth_day_tuple <= (5,20): 
        zodiac = "牡牛座"
    if (5,21) <= birth_day_tuple <= (6,20): 
        zodiac = "双子座"
    if (6,21) <= birth_day_tuple <= (7,22): 
        zodiac = "蟹座"
    if (7,23) <= birth_day_tuple <= (8,22): 
        zodiac = "獅子座"
    if (8,23) <= birth_day_tuple <= (9,22): 
        zodiac = "乙女座"
    if (9,23) <= birth_day_tuple <= (10,22): 
        zodiac = "天秤座"
    if (10,23) <= birth_day_tuple <= (11,21): 
        zodiac = "蠍座"
    if (11,22) <= birth_day_tuple <= (12,21): 
        zodiac = "射手座"
    if (12,22) <= birth_day_tuple <= (12,31): 
        zodiac = "山羊座"
    if (1,1) <= birth_day_tuple <= (1,19): 
        zodiac = "山羊座"
    if (1,20) <= birth_day_tuple <= (2,18): 
        zodiac = "水瓶座"
    if (2,19) <= birth_day_tuple <= (3,20): 
        zodiac = "魚座"
    return zodiac


def color_menu_int_to_idea(argument):
    argument = int(argument)
    switcher = {
        1: red_idea,
        2: pink_idea,
        3: orange_idea,
        4: yellow_idea,
        5: green_idea,
        6: blue_idea,
        7: purple_idea,
        8: gray_idea, 
        9: brown_idea,
        10: black_idea, 
        11: white_idea 
    }
    return switcher.get(argument, "nothing")

def hobby_to_idea(hobby_string):

    hobby_dict = { 

        "スポーツ観戦" : "スポーツ観戦は、特にあなたの好きなチームが勝利したときにリラックスするのに役立ちます。",
    
        "スポーツ" : "スポーツをすることは運動だけでなく楽しみにもなり得ます。",
    
        "運動" : "運動は健康で幸せな滞在をするのに役立ちます",
    
        "ジム" : "ジムは健康維持に役立ちます。",
    
        "ヨガ" : "ヨガは古代インドのテクニックで、心身ともに良いものです。",
    
        "ネットサーフィン" : "インターネットサーフィンはあなたがあなたの家の快適さで世界についてのあなたの知識を増やすのを助けることができます。",
    
        "ゲーム":"ゲームをすることはあなたにスポーツの精神を植え付ける", 
    
        "アプリゲーム":"アプリのゲームは楽しいですし、どこでも遊べます",
    
        "睡眠":"睡眠は体の適切な機能のために必要です",
    
        "アニメ鑑賞":"最近のアニメは世界中で人気があります。",
    
        "食べること":"あなたの好きな食べ物を持っていることは最も楽しい経験の一つになることができます。",
    
        #"アイドル":"
    
        "コンサート": "あなたのお気に入りのバンドが演奏しているときにコンサートは特に素晴らしいです。",
    
        "英語": "英語は世界中の人々とのコミュニケーションを助けます。",
    
        "お笑い": "コメディを見ることはあなたを幸せにすることができます。",
    
        "お笑い芸人":"人々を笑わせることはあなたに内なる満足を与えることができます。",
    
        "テレビ鑑賞":"テレビは週末に最適なパスタイムです。",

        "映画":"映画は友達や家族と一緒に楽しめる素晴らしい経験です。",
    
        "貯金":"貯蓄はあなたの経済的未来に不可欠です。",
    
        "献血":"それが命を救うのを助けることができるので、献血は素晴らしい趣味です。",
    
        #"映画鑑賞"
    
        "ドライブ":"運転はあなたの家から出てあなたの周りを楽しむためのクールな方法です。",
    
        "旅行":"旅行は私たちが新しい人と出会い、異なる文化を理解するのを助けます。",
    
        "写真":"写真撮影は本当にクールな趣味です。",
    
        "カメラ":"カメラはとても楽しいです。",
    
        "音楽":"音楽は世界共通の言語であり、最も古い芸術形式の一つです。",

    
        "楽器":"楽器は素晴らしいです。 アインシュタインでさえバイオリンを弾いた。",
    
        "ギター":"ああ！あなたはロックスターです！",
    
        "ピアノ":"ピアノは美しい響きの楽器です。",
    
        #"コンサート"
    
        "読書":"ああ！ あなたは知的な種類のようです。",
    
        "マラソン":"あなたは珍しい人です。 多くの人はマラソンを走ることができません。",
    
        "ランニング":"ランニングヘルプあなたはより速くあなたの目的地に到達するのと同様に健康を維持します。",
    
        "野球":"野球は世界中で急速に人気が高まっています。",

        "バッティングセンター":"バッティングセンターは本当にかっこいいです。",
    
        "ゲームセンター":"ゲームセンターは楽しい時間です。",
    
        "食べ歩き":"食べ歩きはシンプルでクールな趣味です。",
    
        "料理":"料理はあなたや他の人を幸せにするものです。",
    
        "お菓子作り":"お菓子は私のお気に入りのものです。 仲良くしましょう。",
    
        "食べること":"食べることも私が楽しむものです。",
    
        "花":"花はきれいです。 私はそれらがとても好きです。",
    
        "ガーデニング": "ガーデニングはすごいです。 それはあなたが環境に情熱を持っていることを示しています。",
    
        "海外ドラマ":"海外のドラマも好きです。",
    
        "編み物":"編み物はあなたが家で服を製造するのを助ける素晴らしい趣味です。",
    
        "DIY":"DIYはとても楽しいです。",
    
        "ダンス":"ダンスは素晴らしい運動です。",
    
        "フラダンス":"フラフープダンスは素晴らしい運動です。",
    
        "ベリーダンス":"ベリーダンスは運動の素晴らしい形です。",
    
        "ヒップホップ": "ヒップホップミュージックは、人々が自分自身を簡単に表現するのを助けます",
    
        "コーヒー": "コーヒーは長い一日の後にあなたの心をリフレッシュさせる",
    
        "勉強": "勉強することはあなたがあなたの心を育てるのを助けます。",
    
        #"ロック":
   
        #"インターネット"

    }   

    out_msg = ""
    
    for key in hobby_dict:
        if key in hobby_string: 
            out_msg = out_msg + hobby_dict[key] + " " 
    if out_msg == "": 
            if "しない" in hobby_string or "何もない" in hobby_string or "いいえ" in hobby_string:
                out_msg = "趣味？まれです！私はあなたが秘密を守っていると思います。"
    if out_msg == "": 
        out_msg = "いい趣味をお持ちですね。"

    return out_msg

def get_reservations_for_customer(cust_id):
   
    is_rsv = 0 
    exist_rsv_dict = {}  
    
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    select_sql = """ 
        select id,service_id,employee_ids,
        start_date,start_time from reservations 
        where (customer_id = %s and reservation_type = 1 and status = 1) 
        and ((start_date = %s and start_time >= %s) 
        or (start_date > %s))
    """ 

    select_tuple = (cust_id,today_date,current_time,today_date)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    #SQL
    mycursor.close()
    mydb.close()
     
 
 
  
    if len(myresult_list) == 0:
        is_rsv = 0 
    else:
        is_rsv = 1 
        menu_int = 1 
        
        for rsv_tuple in myresult_list:
            r_id = rsv_tuple[0]
            serv_id = rsv_tuple[1]
            emp_id = rsv_tuple[2]
            start_date = str(rsv_tuple[3])
            start_time = str(rsv_tuple[4])

            exist_rsv_dict[str(menu_int)] = { 
                "r_id": r_id,
                "serv_id": serv_id,
                "emp_id": emp_id,  
                "start_date": start_date,
                "start_time": start_time
            }   
            menu_int += 1
    #print(exist_rsv_dict)
    return is_rsv,exist_rsv_dict
            
#c_id = 2967
#get_reservations_for_customer(c_id)

def ask_hair_frequency_fun():

    ask_hair_frequency_options = [
    {"key":"1", "value": "３週間に１度"},
    {"key":"2", "value": "月に１度"},
    {"key":"3", "value": "２ヶ月に１度"},
    ]   

    return ask_hair_frequency_message,ask_hair_frequency_options

def ask_nails_frequency_fun():

    ask_nails_frequency_options = [
    {"key":"1", "value": "３週間に１度"},
    {"key":"2", "value": "月に１度"},
    {"key":"3", "value": "２ヶ月に１度"},
    ]   

    return ask_nails_frequency_message,ask_nails_frequency_options

def ask_eyelash_frequency_fun():

    ask_eyelash_frequency_options = [
    {"key":"1", "value": "３週間に１度"},
    {"key":"2", "value": "月に１度"},
    {"key":"3", "value": "２ヶ月に１度"},
    ]   

    return ask_eyelash_frequency_message,ask_eyelash_frequency_options

def ask_relaxation_frequency_fun():

    ask_relaxation_frequency_options = [
    {"key":"1", "value": "３週間に１度"},
    {"key":"2", "value": "月に１度"},
    {"key":"3", "value": "２ヶ月に１度"},
    ]   

    return ask_relaxation_frequency_message,ask_relaxation_frequency_options


def ask_work_address_fun():
    return ask_work_address_message

def ask_home_address_fun(cust_responses):

    #if cust_responses["is_working"] == "yes":
    #    return ask_home_address_is_working_message,ask_home_address_message_2
    #else:
    #    return ask_home_address_not_working_message,ask_home_address_message_2
    return ask_home_address_message_1, ask_home_address_message_2

def ask_email_fun(cust_responses):
    """
    if "is_nickname" in cust_responses:
        if cust_responses["is_nickname"] == "yes":
            nick = cust_responses["nickname"]
            return ask_email_message.format(nick)
        else:
            return ask_email_wo_nn_message
    else:
        return ask_email_wo_nn_message
    """

    return ask_email_message_1, ask_email_message_2

def ask_aesthetic_frequency_fun():

    ask_aesthetic_frequency_options = [
    {"key":"1", "value": "３週間に１度"},
    {"key":"2", "value": "月に１度"},
    {"key":"3", "value": "２ヶ月に１度"},
    ]   

    return ask_aesthetic_frequency_message,ask_aesthetic_frequency_options

def ask_often_service_fun():

    ask_often_service_options = [
    {"key":"1", "value": "ヘアサロン"},
    {"key":"2", "value": "ネイル"},
    {"key":"3", "value": "アイラッシュ"},
    {"key":"4", "value": "リラクゼーション"},
    {"key":"5", "value": "エステ"},
    ]   

    return ask_often_service_message,ask_often_service_options



def ask_free_time_fun():

    ask_free_time_options = [
    {"key":"1", "value": "午前"},
    {"key":"2", "value": "午後"},
    {"key":"3", "value": "夕方以降"},
    ]   

    return ask_free_time_message,ask_free_time_options

def ask_free_days_fun(cust_responses):

    ask_free_days_options = [
    {"key":"1", "value": "平日"},
    {"key":"2", "value": "週末"},
    {"key":"3", "value": "どちらも"}

    ]   

    """

    if "is_nickname" in cust_responses:
        if cust_responses["is_nickname"] == "yes":
            nick = cust_responses["nickname"]
            return ask_free_days_message_1.format(nick),ask_free_days_message_2,ask_free_days_options
        else:
            return ask_free_days_message_wo_nn_1,ask_free_days_message_2,ask_free_days_options
    else:
        return ask_free_days_message_wo_nn_1,ask_free_days_message_2,ask_free_days_options
    """
    return ask_free_days_message, ask_free_days_options


def insert_into_ratings_table(customer_id,user_id,rating):
    now_obj = datetime.datetime.now()
    now_str = str(now_obj)

    
    insert_sql = """
        insert into ratings values (default,%s,%s,%s,%s)  
    """

    insert_tuple = (customer_id,user_id,rating,now_str)

    mydb,mycursor = create_sql_conn()
    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()
    mycursor.close()
    mydb.close()



def check_working_day(date_obj,user_id):
    select_sql = """ 
        select day from user_working_days where user_id = %s 
    """        
    select_tuple = (user_id,)

    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    list_of_working_days = []

    for item in myresult_list:
        item_ft = item[0]
        day = item_ft.decode() ; day 
        fl = day[0]
        fl = fl.upper()
        new_day = list(day)
        new_day[0] = fl
        new_day_str = "".join(new_day)
        list_of_working_days.append(new_day_str)
        
    print(list_of_working_days)
    day = date_obj.strftime("%a")
    print(day)
    if day in list_of_working_days:
        working = 1 
    else:
        working = 0 
    return working


def get_cid_from_ip(ip):

    name_phone_status = 0
    existing_status = 0 
    
    select_sql = """select cust_responses from sessions where ip = %s"""
    select_tuple = (ip,)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    if len(myresult_list) != 0:
        first_tuple = myresult_list[0]
        first_element = first_tuple[0]
        json_acceptable_string = first_element.replace("'", "\"")
        my_dict = json.loads(json_acceptable_string)
        if "name" in my_dict:
            if "phone" in my_dict:
                name_phone_status = 1
                name = my_dict["name"]
                phone = my_dict["phone"]

    if name_phone_status == 1:

        select_sql = """select id from customers where name = %s and tel = %s"""
        select_tuple = (name,phone)

        mydb,mycursor = create_sql_conn()
        mycursor.execute(select_sql,select_tuple)
        myresult_list = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        
        if len(myresult_list) == 0:
            existing_status = 0
            c_id = 0
        else:
            existing_status = 1
            tuple0 = myresult_list[0]
            c_id = tuple0[0]
    else:
        c_id = 0
   
    return existing_status,c_id



def find_todays_horoscope(sign):
    print("inside find todays horoscope")
    now = datetime.datetime.now()
    now_format = now.strftime("%Y-%m-%d") 

    month = str(now.month)
    day = str(now.day)

    print("about to enter try block")

    #try:
    #    print("inside try block")
    #    love_url = "https://www.vogue.co.jp/horoscope/daily/" + year + "/" + month + "/" + day + "/" + sign 
    #    print("1")
    #    love_response = urllib.request.urlopen(love_url, timeout=10)
    #    print("2")
    #    love_html = love_response.read()
    #    print("3")

    #    love_utf = str(love_html, 'utf-8', errors='ignore')
    #    love_soup = BeautifulSoup(love_utf, 'html.parser')
    #    love_mydivs = love_soup.findAll("div", {"class": "horoscope__single__message__text"})
    #    love_one = love_mydivs[0]
    #    love_text=love_one.select('div > p')[0].get_text(strip=True)
    #except:
    #    print("inside except")
    #    love_text = "気になる人がいるなら時間をかけて、少しずつお互いの気持ちの温度を高めていこう。友情が愛情に変わる日も近いかも。"


    love_text1 = "年齢が近い人からの誘いに乗るとよさそう。仕事をスマートにこなしているあなたに、異性の注目も集まりそう。" 
    love_text2 = "家族ぐるみの交際を強要され、戸惑ってしまいそう。将来を考えられない相手なら、残念だけど早めにお断りするのが正解かも。"
    love_text3 = "諦めかけていた恋に希望が見えてきそう。勇気を出してアタックを。好きな人と両思いになれるかも！"

    love_arr = [love_text1,love_text2,love_text3]
    love_text = random.choice(love_arr)

    return love_text


def chat_more_fun():

    chat_more_options = [
    {"key":"1", "value": "はい、仕事をしています。"},
    {"key":"2", "value": "いいえ、今は仕事をしていません。"},
    {"key":"3", "value": "私は学生です。"},
    {"key":"4", "value": "私は主婦です。"}
    ]   

    return chat_more_message_1,chat_more_message_2,chat_more_options


def cancel_change_reservation_fun(cust_responses,user_id,action):
    cust_id = cust_responses["customer_id"] 
    is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id)
    option_list = []

    service_dict = get_services(user_id) 
    emp_name_dict = find_employee_name(user_id) 
    
    for key in exist_rsv_dict:

        serv_id = exist_rsv_dict[key]["serv_id"]

        for i in service_dict:
            print(service_dict[i]["id"])
            print(serv_id)

            if service_dict[i]["id"] == serv_id:
                print("matched")
                serv_name = service_dict[i]["name"]
        
        emp_id = exist_rsv_dict[key]["emp_id"]

        for i in emp_name_dict:
            print(i)
            print(emp_id)

            if i == int(emp_id):
                print("matched")

                emp_bytearray_list = emp_name_dict[i]
                emp_bytearray_firstelement = emp_bytearray_list[0]
                emp_name = emp_bytearray_firstelement.decode() ; emp_name

        start_date = exist_rsv_dict[key]["start_date"]
        start_date_jap = convert_date_from_yyyymmdd_to_jap(start_date)
        start_time = exist_rsv_dict[key]["start_time"]
                 

        #value = serv_name + " と " + emp_name + " に " + start_date + " で " + start_time 
        value = serv_name + " と " + emp_name + " に " + start_date_jap + " で " + start_time 
        
        #value = str(exist_rsv_dict[key]["serv_id"]) + " with " + str(exist_rsv_dict[key]["emp_id"]) + " on " + exist_rsv_dict[key]["start_date"] + " at " + exist_rsv_dict[key]["start_time"] 
        
        option = {
            "key": key,
            "value": value
        }
        
        option_list.append(option) 

    if action == "cancel":
        out_msg = "どの予約をキャンセルしますか？"
    if action == "change":
        out_msg = "どの予約を変更しますか？"
    
    return out_msg, option_list, exist_rsv_dict 



"""
def change_reservation_fun(cust_responses):
    
    cust_id = cust_responses["customer_id"] 
    is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id)
    option_list = []
    
    for key in exist_rsv_dict:

        value = str(exist_rsv_dict[key]["serv_id"]) + " with " + str(exist_rsv_dict[key]["emp_id"]) + " on " + exist_rsv_dict[key]["start_date"] + " at " + exist_rsv_dict[key]["start_time"] 
        
        option = {
            "key": key,
            "value": value
        }
        
        option_list.append(option) 

    out_msg = "Which reservation do you want to change"
    return out_msg, option_list,exist_rsv_dict 
"""


def color_menu_int_to_name(argument):
    print("Inside Switcher")
    print("Argument:" + str(argument) + "Arg")
    print(type(argument))
    try:
        argument = int(argument)
    except:
        return "nothing"
     
    switcher = {
        1:	"赤",
        2:	"ピンク",
        3: "オレンジ",
        4: "黄色",
        5: "緑",
        6:	"青",
        7:  "紫",
        8:  "グレー", 
        9: "茶色",
        10: "黒", 
        11: "白"
    }

    #x = switcher[argument]
    #print(x)
    return switcher.get(argument, "nothing")




def convert_date_from_yyyymmdd_to_jap(inp_str):
    str_list = inp_str.split("-")

    year = str_list[0]
    month = str_list[1]
    day = str_list[2]

    jap_date = year + "年" + month + "月" + day + "日"

    return jap_date


def get_date_in_ddmmyyyy_format(inp_str):
    status = 0 
    try:
        print("inside try") 
        inp_str = inp_str.replace("日","")
        inp_str = inp_str.replace("月","-")
        inp_str = inp_str.replace("年","-")

        print("inp_str")
        print(inp_str)
            
        str_list = inp_str.split("-")

        if len(str_list) == 3:
            print("year included")
            day = str_list[2]
            month = str_list[1]
            year = str_list[0]

            if len(day) == 1:
                if int(day) < 10:  
                    day = "0" + day  

            if len(month) == 1:
                if int(month) < 10:  
                    month = "0" + month 
                     
            status = 1   
            out_date = day + "-" + month + "-" + year 
            date_obj = datetime.datetime.strptime(out_date, '%d-%m-%Y')
            
        elif len(str_list) == 2:

            print("year not included")
            print("year not included")
            print("year not included")
            print("year not included")

            day = str_list[1]
            month = str_list[0]
            print("year not included")
            now = datetime.datetime.now()
            year= str(now.year)
            print("here")
            if len(day) == 1:
                if int(day) < 10:  
                    day = "0" + day  

            if len(month) == 1:
                if int(month) < 10:  
                    month = "0" + month 
            status = 1   
            out_date = day + "-" + month + "-" + year 
            print("out_date")
            print(out_date)
            date_obj = datetime.datetime.strptime(out_date, '%d-%m-%Y')
            print("date_obj")
            print(date_obj)
        else:
            out_date = ""  
            status = 0 
            return status, out_date,wrong_date_message
    except:
            out_date = ""  
            status = 0 
            return status, out_date,wrong_date_message
                
    return status,date_obj,all_okay_message


def insert_into_chats_db(user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state):

    sql = "insert into chats values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    insert_tuple = (user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,insert_tuple)
    
    mydb.commit()

    mycursor.close()
    mydb.close()


def insert_into_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):

    print("\n\nInside insert session\n\n")
    print("HHHHHHHHHHH" + return_list_of_dicts + "IIIIIIIIIIII")
    #return "nothing"

    select_sql = "select * from sessions where ip = %s"
    select_tuple = (ip,)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    if len(myresult_list) != 0:
        delete_sql = "delete from sessions where ip = %s"
        delete_tuple = (ip,)
        mydb,mycursor = create_sql_conn()
        mycursor.execute(delete_sql,delete_tuple)
        mydb.commit()
        mycursor.close()
        mydb.close()
    
    insert_sql = "insert into sessions(ip,STATE,return_list_of_dicts,return_dict,cust_responses) values(%s,%s,%s,%s,%s)"
    insert_tuple = (ip,STATE,return_list_of_dicts,return_dict,cust_responses)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()
    mycursor.close()
    mydb.close()




def update_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):
    #cust_name

    json_acceptable_string = cust_responses.replace("'", "\"")
    d = json.loads(json_acceptable_string)

    if "name" in d:
        cust_name = d["name"]
    else:
        cust_name = ""
    
    #sql = "update session set STATE = %s, return_list_of_dicts = %s, return_dict = %s,cust_responses= %s where ip = %s"
    
    sql = """
        update sessions set STATE = %s, return_list_of_dicts = %s, 
        return_dict = %s, cust_responses= %s, cust_name = %s where ip = %s
    """
    
    insert_tuple = (STATE,return_list_of_dicts,return_dict,cust_responses,cust_name,ip)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,insert_tuple)
    mydb.commit()
    mycursor.close()
    mydb.close()


def generate_reservation_number():
    print("run")
    low =  10000000
    high =  99999999
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    al = random.choice(letters)
    num = str(random.randint(low,high))
    new_code = "M" + al + num 
    sql = """select reservation_number from reservations"""
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    found = 0 
    for code_tuple in myresult_list:
        exist_code_ba = code_tuple[0]
        exist_code = exist_code_ba.decode() ; exist_code
        if new_code == exist_code:
            found = 1 
            break
    if found == 0:
        return new_code
    elif found == 1:
        generate_reservation_number()


def delete_from_reservations_table(r_id):

    r_id_status = 0 

    select_sql = """select * from reservations where id = %s"""
    select_tuple = (r_id,)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()
        
    if len(myresult_list) == 0:
        r_id_status = 0 
    else:
        r_id_status = 1
        
        update_sql = """update reservations set status = 4 where id = %s"""
        update_tuple = (r_id,)
        
        mydb,mycursor = create_sql_conn()
        mycursor.execute(update_sql,update_tuple)
        mydb.commit()
        mycursor.close()
        mydb.close()

    return r_id_status


def insert_into_reservations_table(u_id,c_id,s_id,ss_id,e_id,s_date,e_date,s_time,e_time,total):

    ex_s_date = s_date + " 00:00:00"
    ex_e_date = e_date + " 00:00:00" 
    r_num = generate_reservation_number() 
    now_obj = datetime.datetime.now()
    now_str = str(now_obj)
    print("generated code successfully")

    insert_sql = """
        insert into reservations
        (id,user_id,customer_id,service_id,
        sub_service_id,employee_ids,reservation_number,
        start_date,end_date,extra_start_date,
        extra_end_date,start_time,end_time,
        reservation_type,reservation_total,
        used_points,payment_total,status,created,modified,note)
        values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'1',%s,'0',%s,1,%s,%s,'')
    """
   
    insert_tuple = (
        u_id,c_id,s_id,ss_id,e_id,r_num,s_date,e_date,
        ex_s_date,ex_e_date,s_time,e_time,total,total,
        now_str,now_str
    )

    mydb,mycursor = create_sql_conn()
    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("yahaan hoon")
        
    select_sql1 = """select id from reservations where reservation_number = %s"""
    select_tuple1 = (r_num,)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql1,select_tuple1)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    print("yahaan hoon")
    tuple0 = myresult_list[0]
    r_id = tuple0[0]
    
    return r_num,r_id



def check_existing_customer(name,email):

    existing_status = 0

    select_sql = """select id,user_id from customers where name = %s and email = %s"""
    select_tuple = (name,email)


    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    if len(myresult_list) == 0:
        existing_status = 0
        c_id = 0
        user_id = 0
    else:
        existing_status = 1
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
        user_id = tuple0[1]
   
    return existing_status,c_id,user_id 



def insert_into_customers_table(c_name,c_kana,c_dob,c_tel,user_id,is_daily_horoscope,cust_zodiac_eng,device_id,device_type):

#def insert_into_customers_table(c_name,c_kana,c_dob,c_tel,user_id,is_daily_horoscope,cust_zodiac_eng):
    #device_id = "VHGGS1239403"
    #device_type = "iphone"
    
    na = c_name.split(' ')
    
    if len(na) == 1:
        c_first_name = na[0] 
        c_last_name = ""  
    else:
        c_first_name = na[1] 
        c_last_name = na[0] 

    nna = c_kana.split(' ')
    if len(nna) == 1:
        c_kana_first_name = nna[0] 
        c_kana_last_name = ""  
    else:
        c_kana_first_name = nna[1] 
        c_kana_last_name = nna[0] 
    
    #CHANGE_TEL 
    select_sql = """select * from customers where user_id = %s and name = %s and tel = %s"""
    #select_sql = """select * from customers where user_id = %s and name = %s and email = %s"""
    select_tuple = (user_id,c_name,c_tel)

    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    
    if len(myresult_list) == 0:
        now_obj = datetime.datetime.now()
        now_str = str(now_obj)
        
        # CHANGE_TEL 
        insert_sql = """ 
            insert into customers (user_id,name,first_name,last_name,kana,
            kana_first_name,kana_last_name,dob,tel,created,modified,daily_horoscope,zodiac,device_id,device_type) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        
        #insert_sql = """ 
        #    insert into customers (user_id,name,first_name,last_name,kana,
        #    kana_first_name,kana_last_name,dob,email,created,modified,daily_horoscope,zodiac,device_id,device_type) 
        #    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        #"""

        insert_tuple = (
            user_id,c_name,c_first_name,c_last_name,c_kana,c_kana_first_name,
            c_kana_last_name,c_dob,c_tel,now_str,now_str,is_daily_horoscope,
            cust_zodiac_eng,device_id,device_type
        )

        mydb,mycursor = create_sql_conn()
        mycursor.execute(insert_sql,insert_tuple)
        mydb.commit() 
        mycursor.close()
        mydb.close()

        # CHANGE_TEL
        select_sql1 = """select * from customers where user_id = %s and name = %s and tel = %s"""
        #select_sql1 = """select * from customers where user_id = %s and name = %s and email = %s"""
        
        select_tuple1 = (user_id,c_name,c_tel)
        
        mydb,mycursor = create_sql_conn()
        mycursor.execute(select_sql1,select_tuple1)
        myresult_list = mycursor.fetchall()
        mycursor.close()
        mydb.close()
    
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
    else:
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
   
    return c_id

def find_often_service_state(cust_responses):
    often_service_arr = cust_responses["often_service_arr"]

    print("-------------------------------")
    print(often_service_arr)
    print("-------------------------------")

    count = 0
    one_found = 0 
    for ind in often_service_arr:
        if ind == 1:
            one_found = 1 
            break
        count += 1

    if one_found == 1:
    
        if count == 0:
            STATE= "ASK_HAIR_FREQUENCY"
        if count == 1:
            STATE= "ASK_NAILS_FREQUENCY"
        if count == 2:
            STATE= "ASK_EYELASH_FREQUENCY"
        if count == 3:
            STATE= "ASK_RELAXATION_FREQUENCY"
        if count == 4:
            STATE= "ASK_AESTHETIC_FREQUENCY"
        
        often_service_arr[count] = 0
        cust_responses["often_service_arr"] = often_service_arr
    else:
        #STATE = "ASK_EMAIL"
        STATE = "IS_SPECIFIC_SALON"

    return STATE, cust_responses




def find_employee_name(user_id):
    select_sql = """select id,name from employees where user_id = %s and is_technician = 1 order by service_id """
    select_tuple = (user_id,) 
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    
    emp_name_dict = dict()

    for emp_tuple in myresult_list:
        emp_name_dict[emp_tuple[0]] = [emp_tuple[1]]

    return emp_name_dict


def get_services(user_id):

    print("user_id")
    print(user_id)

    select_sql = """
        select id, name from services where id in 
        (select distinct service_id from employees 
        where user_id = %s and is_technician = 1 and status = 1 and service_id in 
        (select distinct service_id from sub_services where user_id = %s));
    """

    select_tuple = (user_id,user_id)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    s_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        s_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        s_name = serv_tuple_second.decode() ; s_name 

        s_dict[str(menu_int)] = {"id": s_id, "name": s_name}
    
        menu_int += 1

    return s_dict


def get_super_services(service_id,user_id):

    print("inside get sub serices")
    print("service_id","user_id")
    print(service_id,user_id)
    sql = """select id,name from sub_services where user_id = %s and status = 1 and service_id = %s and parent_id = %s"""
    select_tuple = (user_id,service_id,0)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    print("myresult_list") 
    print(myresult_list) 
    sup_serv_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        sup_serv_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        sup_serv_name = serv_tuple_second.decode() ; sup_serv_name 
    
        sup_serv_dict[str(menu_int)] = {"id": sup_serv_id, "name": sup_serv_name}
    
        menu_int += 1
    
    print("sup_serv_dict")
    print(sup_serv_dict)

    return sup_serv_dict

def get_sub_services(service_id,user_id):

    print("inside get sub serices")
    print("service_id","user_id")
    print(service_id,user_id)
    sql = """select id,name,duration,price from sub_services where user_id = %s and status = 1 and service_id = %s"""
    select_tuple = (user_id,service_id)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    
    print("myresult_list") 
    print(myresult_list) 
    ss_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        ss_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        ss_name = serv_tuple_second.decode() ; ss_name 
    
        serv_tuple_third = serv_tuple[2]
        ss_duration = serv_tuple_third.decode() ; ss_duration 
    
        serv_tuple_fourth = serv_tuple[3]
        ss_price = serv_tuple_fourth.decode() ; ss_price

        ss_dict[str(menu_int)] = {"id": ss_id, "item": ss_name, "duration": ss_duration, "price": ss_price}
    
        menu_int += 1
    print("ss_dict")
    print(ss_dict)

    return ss_dict

def find_employees_for_service(service_id,user_id):


    print("inside find employees for service")
    print("service_id,user_id")
    print(service_id,user_id)
    
    select_sql = """select service_id,id from employees where user_id = %s and is_technician = 1 and status = 1 order by service_id"""
    select_tuple = (user_id,)
    mydb,mycursor = create_sql_conn()
    mycursor.execute(select_sql,select_tuple)

    myresult_list = mycursor.fetchall()
    mycursor.close()
    mydb.close()

    print("myresult_list")
    print(myresult_list)
        
    service_dict = dict()

    for serv_tuple in myresult_list:
        if serv_tuple[0] in service_dict:
            service_dict[serv_tuple[0]].append(serv_tuple[1])
        else:
            service_dict[serv_tuple[0]] = [serv_tuple[1]]
    print("\n\n------------\n\n")
    print(service_dict)


    print("service_dict[service_id]")
    print(service_dict[service_id])

    return service_dict[service_id]

#def check_availability(service_int, date_time_obj,employee_list,time_duration):
#    return result_list


def check_new_availability(date_time_obj,employee_list,time_duration,user_id):
    print("Check New Availability")
    print("date_time_obj,employee_list,time_duration,user_id")
    print(date_time_obj,employee_list,time_duration,user_id)
    #return 0

    result_dict = {}
    date_format = date_time_obj.strftime("%Y-%m-%d")
    time_format = date_time_obj.strftime("%H:%M:%S")
    
    for employee in employee_list:
        print("\n\n\nEmployee\n\n\n")
        employee_schedule = []
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """
            select service_id, employee_ids, start_date, start_time, end_time 
            from reservations where user_id = %s and reservation_type='1' 
            and start_date = %s and employee_ids = %s
        """

        select_tuple = (user_id, date_format, employee)
        mydb,mycursor = create_sql_conn()
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        for appointment in appointments:
            print("--- appointment ---")
            #print(appointment) 
            
            service_id = appointment[0]
            employee_id = appointment[1]
            date = appointment[2]
            start_time = appointment[3]
            end_time = appointment[4]
            start_hour = start_time.seconds//3600
            start_minute = (start_time.seconds//60) % 60
            
            start_slot_number = start_hour * 2
            if start_minute >= 30 and start_minute <= 59:
                start_slot_number += 1
            
            end_hour = end_time.seconds//3600
            end_minute = (end_time.seconds//60) % 60
            
            end_slot_number = end_hour * 2
            
            if end_minute == 0:
                end_slot_number -= 1
            if end_minute > 30 and end_minute <= 59:
                end_slot_number += 1
            
            for i in range(start_slot_number,end_slot_number+1):
                employee_schedule[i] = 1

        print("employee_schedule")
        print(employee_schedule)
    #return 0

     
        num_of_slots_needed = time_duration * 2

        free_slots = []

        slot_i = 20 # Starting at 10:00 AM

        for i in range(3):
            #print("Iteration " + str(i) + " Started")
            zero_count = 0
            
            if i != 0 :     ## Increase slot number
                slot_i += 1 ## from previous iteration
            
            #while slot_i <= 44: # Ending search at 10:00 PM
            while slot_i <= 40: # Ending search at 08:00 PM
                #print("Inside While Loop")
                #print("slot = " + str(slot_i))
                if employee_schedule[slot_i] == 1:
                    zero_count = 0
                else:
                    zero_count += 1
                
                if zero_count == num_of_slots_needed:
                    break
                slot_i += 1

            avail_end_slot = slot_i
            avail_start_slot = avail_end_slot - num_of_slots_needed + 1
        
            free_slots.append(avail_start_slot)
            result_dict[employee] = free_slots
     
    print("result_dict")
    print(result_dict)
    return result_dict


def get_employee_schedule_for_date(date_time_obj,employee_list):

    date_format = date_time_obj.strftime("%Y-%m-%d")
    employee_schedule_dict = {}

    for employee in employee_list:
        print("here")
        employee_schedule = []  
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """ 
            select service_id, employee_ids, start_date, start_time, end_time 
            from reservations where reservation_type='1' 
            and start_date = %s and employee_ids = %s
        """

        select_tuple = (date_format, employee)
        mydb,mycursor = create_sql_conn()
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        for appointment in appointments:
            #print("--- appointment ---")
    
            service_id = appointment[0]
            employee_id = appointment[1]
            date = appointment[2]
            start_time = appointment[3]
            end_time = appointment[4]
            start_hour = start_time.seconds//3600
            start_minute = (start_time.seconds//60) % 60  

            start_slot_number = start_hour * 2 
            if start_minute >= 30 and start_minute <= 59: 
                start_slot_number += 1 
    
            end_hour = end_time.seconds//3600
            end_minute = (end_time.seconds//60) % 60  
    
            end_slot_number = end_hour * 2 
    
            if end_minute == 0:
                end_slot_number -= 1 
            if end_minute > 30 and end_minute <= 59: 
                end_slot_number += 1 
    
            for i in range(start_slot_number,end_slot_number+1):
                employee_schedule[i] = 1 
 
        employee_schedule_dict[employee] = employee_schedule

    return employee_schedule_dict



def check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours):
    result_dict = {}
    num_of_slots_needed = time_duration_in_hours * 2 

    start_time_split = start_time.split(":")
    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])

    start_slot_number = start_hour * 2 
    if start_minute >= 30 and start_minute <= 59: 
        start_slot_number += 1 
    next_slot_number = start_slot_number + num_of_slots_needed

    for employee in employee_schedule_dict:
        zero_count = 0 
        print("\n\npppppppppppppppp\n\n")
        print(start_slot_number,next_slot_number)
        print("\n\npppppppppppppppp\n\n")
        for slot_i in range(start_slot_number,next_slot_number):
            print("slot_i")
            print(slot_i)
            print("employee schedule")
            print(employee_schedule_dict[employee])

            if employee_schedule_dict[employee][slot_i] == 1:
                zero_count = 0 
            else:
                zero_count += 1

            satisfied = 0
            
            if zero_count == num_of_slots_needed:
                satisfied = 1
                break

        print("satisfied")
        print(satisfied)

        if satisfied == 1:
            avail_end_slot = slot_i
            avail_start_slot = avail_end_slot - num_of_slots_needed + 1 

            free_slots = [avail_start_slot,]
            result_dict[employee] = free_slots 
        else:
            free_slots = []
            result_dict[employee] = free_slots 
        
    return result_dict



def convert_avail_dict_to_display_options(avail_dict,emp_name_dict):
    print("Convert Avail Dict TO Display Options") 
    print("avail_dict,emp_name_dict")
    print(avail_dict,emp_name_dict)
    #return 0,0,0 
    
    avail_msg = "かしこまりました。次のお日にちで空きがあります。\n"
    #avail_msg = avail_msg + "さて、私たちは以下の時期に空室状況があります：\n"
    option_list = []
    option_new_list = []
    display_options = []

    emp_serial = 1
    
    for emp_id in avail_dict:
        list_of_avail_slots = avail_dict[emp_id]
        
        for slot in list_of_avail_slots:
            time_start = slot_list[slot]
            
            emp_bytearray_list = emp_name_dict[emp_id]
            emp_bytearray_firstelement = emp_bytearray_list[0]
            emp_name = emp_bytearray_firstelement.decode() ; emp_name
            option_str = str(emp_serial) + ") " + emp_name + " で利用可能です " + str(time_start)
            option_list.append(option_str)

            key = str(emp_serial)
            value = emp_name + " で利用可能です " + str(time_start)

            my_dict = {
                "key": key,
                "value": value
            }
            option_new_list.append(my_dict)
            option = [emp_serial,emp_id,slot]
            display_options.append(option)
            emp_serial += 1

    none_option_str = str(emp_serial) + ") " + "上記の時間のどれも私には合いません。"
    option_list.append(none_option_str)

    none_key = str(emp_serial)
    none_value = "上記の時間のどれも私には合いません。"
    none_dict = {
    "key": none_key,
    "value": none_value
    }
    option_new_list.append(none_dict)

    none_option = [emp_serial,"none","none"]
    display_options.append(none_option)

    print("display_options,option_new_list")
    print(display_options,option_new_list)

    return avail_msg,display_options,option_new_list




def type_of_salon_menu_int_to_name(argument):
    switcher = {
    1: "早く仕上げてくれる",
    2: "安い",
    3: "静かなサロン",
    4: "接客がとてもいいサロン",
    5: "高級感のあるサロン",
    6: "スタッフの質が高いサロン",
    7: "清潔感のあるサロン",
    8: "落ち着いたサロン"

    }

    return switcher.get(argument, "nothing")

"""
"""


def service_menu_int_to_id(argument):
    switcher = {
    1: 1,
    2: 2
    }

    return switcher.get(argument, "nothing")


def service_numbers_to_strings(argument):
    switcher = {
    1: "nails",
    2: "beauty_treatment",
    3: "eye_lashes",
    4: "body",
    5: "hair_removal",
    6: "facial"
    }
    return switcher.get(argument, "nothing")



def first_welcome_fun():
    #return welcome_ask_name_message
    return welcome_message

def ask_lastname_fun():
    return ask_lastname_message_1, ask_lastname_message_2

def ask_firstname_fun():
    return ask_firstname_message

def is_nickname_fun():
    is_nickname_options = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "いいえ"} 
    ]
    #return is_nickname_message,is_nickname_options
    return is_nickname_message_1,is_nickname_message_2,is_nickname_options

def ask_nickname_fun():
    return ask_nickname_message

def ask_alt_time_fun():
    return ask_alt_time_message

def ask_alt_date_fun(cust_responses):
    #alt_avail_days = cust_responses["alt_avail_days"]
    alt_avail_days = cust_responses["jap_option_list"] 
    return ask_alt_date_message,alt_avail_days

def ask_specific_salon_fun():
    return ask_specific_salon_message

def ask_salon_again_fun():
    return ask_salon_again_message

def is_specific_salon_fun(cust_responses):
    option_list = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "いいえ"} 
    ]

    """
    if cust_responses["is_believe_in_signs"] == "yes":
        if cust_responses["is_daily_horoscope"] == "yes":
            return iss_ydh_message_1,is_specific_salon_message_2,option_list
        else:
            return iss_ndh_message_1,is_specific_salon_message_2,option_list
    else:
        return iss_nbis_message_1,is_specific_salon_message_2,option_list
    """

    return is_specific_salon_message,option_list


def is_daily_horoscope_fun():
    option_list = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "いいえ"} 
    ]
    return is_daily_horoscope_message,option_list


def is_believe_in_signs_fun(cust_responses):
    zodiac = cust_responses["zodiac"]
    #if cust_responses["is_nickname"] == "yes": 
    #    nick = cust_responses["nickname"]
    
    zodiac_eng = zodiac_jap_to_eng[zodiac]

    print("About to find todays horoscope")
    todays_horoscope = find_todays_horoscope(zodiac_eng)


    #todays_horoscope = "This is todays horoscope"
    #はい/ 私にとって良いことなら信じる :D/いいえ
    option_list = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "私にとって良いことなら信じる"},
    {"key":"3","value": "いいえ"} 
    ]
    return ibis_message_1.format(zodiac,zodiac,todays_horoscope),ibis_message_2,option_list



def ask_birthday_fun(cust_responses):
    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        #return ask_birthday_message.format(nick,nick)
        return ask_birthday_message_1.format(nick),ask_birthday_message_2.format(nick)
    else:
        return ask_birthday_without_nickname_message
def confirmed_fun(r_num):
    
    options = [ 
    {"key":"1", "value": "はい、今から大丈夫です。"}, 
    {"key":"2", "value": "今は難しいです。"} 
    ]
    
    return confirmed_message.format(r_num), options

def confirmed_without_more_fun(r_num):
    return confirmed_without_more_message.format(r_num)

def is_time_for_more_2_fun():
    is_time_for_more_2_options = [ 
    {"key":"1", "value": "はい"}, 
    {"key":"2", "value": "いいえ"} 
    ]

    return is_time_for_more_2_message_1,is_time_for_more_2_message_2,is_time_for_more_2_options


def is_time_for_more_fun():
    #is_time_for_more_options = ["1) はい、今から大丈夫です。/ I can chat now", "2) 今は難しいです。/ let’s talk later"]

    is_time_for_more_options = [ 
    {"key":"1", "value": "はい、今から大丈夫です。"}, 
    {"key":"2", "value": "今は難しいです。"} 
    ]

    #return is_time_for_more_message,is_time_for_more_options
    return is_time_for_more_message_1,is_time_for_more_message_2,is_time_for_more_options

def use_recommended_salon_fun():

    option_list = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2","value": "いいえ"} 
    ]
    return use_recommended_salon_message, option_list

def confirm_specific_salon_fun(cust_responses):

    salon1_staff_list = [
        {
            "id": 49,
            "name": "大原 めぐみ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/file_15363817070.jpg",
            "service": "ネイル"
        },

    ]

    salon1_image_list = [
        "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/9082fe64759dda4eb76f5e7002226c01.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/dbc43e089746dd33dfb027c282902aca.jpg",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,102)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    
    
    
    salon1 = {
        "id": "102", 
        "name": "マジェスティックビューティー",
        "star": "5",
        "location":"愛知県名古屋市中村区名駅南3丁目3-21 BIANCASA水主町2階",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"ネイル",
        "staff": salon1_staff_list,
        "description": "名古屋市で自爪に優しいラグジュアリーネイルサロン「マジェスティックビューティー」",
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon1_image_list,
        "zip_code": "450-0003",
        "today_status": today_status
    }

    salon2_staff_list = [
        {
            "id": 196,
            "name": "岩崎緑",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステティック"
        },

        {
            "id": 197,
            "name": "山下ゆうこ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステティック"
        },
    ]

    salon2_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,592)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon2 = {
        "id": "592", 
        "name": "ハイパーナイフ痩身小顔専門店salon de me",
        "star": "5",
        "location":"",###############
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステティック",
        "staff": salon2_staff_list,
        "description": "",###########
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon2_image_list,
        "zip_code": "453-0014",
        "today_status": today_status
    }

    salon3_staff_list = [
        {
            "id": 213,
            "name": "高橋　小百合",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon3_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,626)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon3 = {
        "id": "626", 
        "name": "LunaTiara",
        "star": "5",
        "location":"東区泉3丁目24-7",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon3_staff_list,
        "description": "Luna ティアラ", ############
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon3_image_list,
        "zip_code": "", ############
        "today_status": today_status
    }

    salon4_staff_list = [
        {
            "id": 221,
            "name": "金沢由伊",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon4_image_list = [
        "https://api.jtsboard.com/uploads/my_shop/original/99dc354ba8edccc555eaeabab85b21af.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/b6c755e29b19c489124b4d609b28e661.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/b7d011766ac2343b2403b57154a1f270.jpg",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,627)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon4 = {
        "id": "627", 
        "name": "La Luna",
        "star": "5",
        "location":"中区錦3丁目15-32 ホワイトビル3F",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon4_staff_list,
        "description": "",#################
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon4_image_list,
        "zip_code": "460-0003",
        "today_status": today_status
    }

    salon5_staff_list = [
        {
            "id": 222,
            "name": "みわこ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon5_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,628)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon5 = {
        "id": "628", 
        "name": "Cellestia",
        "star": "5",
        "location":"",###########################
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon5_staff_list,
        "description": "",####################
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon5_image_list,
        "zip_code": "",#################
        "today_status": today_status
    }


    if cust_responses["user_id"] == 102:
        salon_gallery_list = [ 
            {"key":"1", "value": salon1}, 
        ]
    if cust_responses["user_id"] == 592:
        salon_gallery_list = [ 
            {"key":"1", "value": salon2}, 
        ]
    if cust_responses["user_id"] == 626:
        salon_gallery_list = [ 
            {"key":"1", "value": salon3}, 
        ]
    if cust_responses["user_id"] == 627:
        salon_gallery_list = [ 
            {"key":"1", "value": salon4}, 
        ]
    if cust_responses["user_id"] == 628:
        salon_gallery_list = [ 
            {"key":"1", "value": salon5}, 
        ]

    option_list = [ 
    {"key":"1", "value":"はい"}, 
    {"key":"2", "value": "いいえ"} 
    ]
    return confirm_specific_salon_message_1, confirm_specific_salon_message_2, salon_gallery_list, option_list

def find_salon_fun():

    salon1_staff_list = [
        {
            "id": 49,
            "name": "大原 めぐみ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/file_15363817070.jpg",
            "service": "ネイル"
        },

    ]

    salon1_image_list = [
        "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/9082fe64759dda4eb76f5e7002226c01.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/dbc43e089746dd33dfb027c282902aca.jpg",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,102)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon1 = {
        "id": "102", 
        "name": "マジェスティックビューティー",
        "star": "5",
        "location":"愛知県名古屋市中村区名駅南3丁目3-21 BIANCASA水主町2階",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"ネイル",
        "staff": salon1_staff_list,
        "description": "名古屋市で自爪に優しいラグジュアリーネイルサロン「マジェスティックビューティー」",
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon1_image_list,
        "zip_code": "450-0003",
        "today_status": today_status
    }

    salon2_staff_list = [
        {
            "id": 196,
            "name": "岩崎緑",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステティック"
        },

        {
            "id": 197,
            "name": "山下ゆうこ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステティック"
        },
    ]

    salon2_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,592)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon2 = {
        "id": "592", 
        "name": "ハイパーナイフ痩身小顔専門店salon de me",
        "star": "5",
        "location":"",###############
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステティック",
        "staff": salon2_staff_list,
        "description": "",###########
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon2_image_list,
        "zip_code": "453-0014",
        "today_status": today_status
    }

    salon3_staff_list = [
        {
            "id": 213,
            "name": "高橋　小百合",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon3_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,626)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    
    salon3 = {
        "id": "626", 
        "name": "LunaTiara",
        "star": "5",
        "location":"東区泉3丁目24-7",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon3_staff_list,
        "description": "Luna ティアラ", ############
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon3_image_list,
        "zip_code": "", ############
        "today_status": today_status
    }

    salon4_staff_list = [
        {
            "id": 221,
            "name": "金沢由伊",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon4_image_list = [
        "https://api.jtsboard.com/uploads/my_shop/original/99dc354ba8edccc555eaeabab85b21af.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/b6c755e29b19c489124b4d609b28e661.jpg",
        "https://api.jtsboard.com/uploads/my_shop/original/b7d011766ac2343b2403b57154a1f270.jpg",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,627)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon4 = {
        "id": "627", 
        "name": "La Luna",
        "star": "5",
        "location":"中区錦3丁目15-32 ホワイトビル3F",
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon4_staff_list,
        "description": "",#################
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon4_image_list,
        "zip_code": "460-0003",
        "today_status": today_status
    }

    salon5_staff_list = [
        {
            "id": 222,
            "name": "みわこ",
            "image": "https://web.jtsboard.com/uploads/note_image/original/emp_image.png",
            "service": "エステ / リラクゼーション"
        },

    ]

    salon5_image_list = [
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
        "https://web.jtsboard.com//img/site/logo.png",
    ]
    
    now_obj = datetime.datetime.now()
    #(102,592,626,627,628)
    open_state = check_working_day(now_obj,628)
    
    if open_state == 1:
        today_status = "Open"
    else:
        today_status = "Closed"
    #"today_status": today_status
    salon5 = {
        "id": "628", 
        "name": "Cellestia",
        "star": "5",
        "location":"",###########################
        "latitude":"35.159884",
        "longitude":"136.892322",
        "open_time":"10:00",
        "close_time":"22:00",
        "services":"エステ / リラクゼーション",
        "staff": salon5_staff_list,
        "description": "",####################
        "image": "https://api.jtsboard.com/uploads/my_shop/original/8f078d545fecf1ee3e75dd30470f1b13.jpg",
        "image_list": salon5_image_list,
        "zip_code": "",#################
        "today_status": today_status
    }


    salon_gallery_list = [ 
        {"key":"1", "value": salon1}, 
        {"key":"2", "value": salon2}, 
        {"key":"3", "value": salon3}, 
        {"key":"4", "value": salon4}, 
        {"key":"5", "value": salon5}, 
    ]

    return find_salon_message,salon_gallery_list


def ask_phone_fun(cust_responses):
    print("\n\npppppppppppppppppppp\n\n")
    print("Inside ask phone") 
    print("Is Specific Salon") 
    
    # UNCOMMENT THIS BLOCK ONCE APP GETS APPROVED 
    """
    print(cust_responses["is_specific_salon"])
    print("Salon Found") 
    #print(cust_responses["salon_found"])
    
    if cust_responses["is_specific_salon"] == "yes":
        
        if cust_responses["salon_found"] == "yes": 
            return ask_phone_message_salon_found_1,ask_phone_message_2
        
        if cust_responses["salon_found"] == "no": 
            return ask_phone_message_salon_not_found_1,ask_phone_message_2
    else:
        return ask_phone_message_1,ask_phone_message_2
    #if cust_responses["is_specific_salon"] == "no": 
    #    return ask_phone_message_no_specific_salon_1,ask_phone_message_2
    """

    if cust_responses["is_believe_in_signs"] == "yes":
        if cust_responses["is_daily_horoscope"] == "yes":
            return ask_phone_ydh_message_1, ask_phone_message_2
        else:
            return ask_phone_ndh_message_1, ask_phone_message_2
    else:
        return ask_phone_nbis_message_1, ask_phone_message_2
    
def ask_hobbies_fun(color_idea):
    #return ask_hobbies_message
    #return ask_hobbies_message.format(color_idea)
    return ask_hobbies_message_1.format(color_idea),ask_hobbies_message_2

def ask_color(cust_responses):

    color_options = [  
    {"key":"1", "value": "赤"}, 
    {"key":"2", "value": "ピンク"}, 
    {"key":"3", "value": "オレンジ"},
    {"key":"4", "value": "黄色"},
    {"key":"5", "value": "緑"},
    {"key":"6", "value": "青"},
    {"key":"7", "value": "紫"},
    {"key":"8", "value": "グレー"},
    {"key":"9", "value": "茶色"},
    {"key":"10", "value": "黒"},
    {"key":"11", "value": "白"}
    ]     

    if "is_nickname" in cust_responses:
        print("inside if")
        if cust_responses["is_nickname"] == "yes":
            nick = cust_responses["nickname"]
            #return ask_color_message.format(nick),color_options
            return ask_color_message_1, ask_color_message_2.format(nick),color_options
        else:
            return ask_color_without_nickname_message_1,ask_color_without_nickname_message_2,color_options
    else:
        return ask_color_without_nickname_message_1,ask_color_without_nickname_message_2,color_options


def new_welcome_fun(cust_responses):
    
    cust_id = cust_responses["customer_id"]
    is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id) 


    if is_rsv == 1:
        new_welcome_options = [
            {"key":"1", "value": "新しい予約を取りたい"},
            {"key":"2", "value": "予約をキャンセルしたい"},
            {"key":"3", "value": "現在の予約を変更したい"},
            {"key":"4", "value": "登録されている情報が知りたい"},
            {"key":"5", "value": "もっとお互いを知るためにチャットがしたいだけ"},
        ]  
    else:
        new_welcome_options = [
            {"key":"1", "value": "新しい予約を取りたい"},
            {"key":"2", "value": "登録されている情報が知りたい"},
            {"key":"3", "value": "もっとお互いを知るためにチャットがしたいだけ"},
        ] 
     
    if "is_nickname" in cust_responses:
        if cust_responses["is_nickname"] == "yes":
            nick = cust_responses["nickname"]
            return new_welcome_message_1.format(nick),new_welcome_message_2,new_welcome_options
        else:
            return new_welcome_without_nickname_message_1,new_welcome_without_nickname_message_2, new_welcome_options
    else:
        return new_welcome_without_nickname_message_1,new_welcome_without_nickname_message_2, new_welcome_options

def ask_type_of_salon():
    ask_type_of_salon_options = [
    {"key":"1", "value": "早く仕上げてくれる。"},
    {"key":"2", "value": "安い。"},
    {"key":"3", "value": "静かなサロン。"},
    {"key":"4", "value": "接客がとてもいいサロン。"},
    {"key":"5", "value": "高級感のあるサロン。"},
    {"key":"6", "value": "スタッフの質が高いサロン。"},
    {"key":"7", "value": "清潔感のあるサロン。"},
    {"key":"8", "value": "落ち着いたサロン。"}
    ]   

    return ask_type_of_salon_message_1,ask_type_of_salon_message_2, ask_type_of_salon_options

def is_reservation_now_fun():
#is_reservation_now_options = ["1) 予約を取る。/ Make a reservation","2) 後で予約を取る。/ Later"]
#is_reservation_now_options = {"1": "予約を取る。/ Make a reservation","2": "後で予約を取る。/ Later"}
    is_reservation_now_options = [
    {"key":"1", "value": "予約を取る。"},
    {"key":"2", "value": "後で予約を取る。"}
    ]   

    #return is_reservation_now_message,is_reservation_now_options
    return is_reservation_now_message_1,is_reservation_now_message_2,is_reservation_now_options

def ask_date():
    #return ask_date_message
    return ask_date_message_1,ask_date_message_2


def ask_service_fun(user_id):
    service_dict = get_services(user_id) 
    ask_service_options = []
    
    for service in service_dict:
        value = str(service_dict[service]["name"])
        option = {"key": service, "value": value} 
        ask_service_options.append(option)
    return ask_service_message, ask_service_options,service_dict


def ask_super_service_fun(cust_responses):
    print("inside ask super service function")

    ask_super_service_message = "どんなメニューですか？"
    sup_service_dict = cust_responses["sub_service_dict"] 
   
    ask_sub_service_options = []
    for sub_service in sub_service_dict:
        value = str(sub_service_dict[sub_service]["item"]) + " : " + str(sub_service_dict[sub_service]["price"])
        #option = {"key": sub_service, "value": sub_service_dict[sub_service]} 
        option = {"key": sub_service, "value": value} 
        ask_sub_service_options.append(option)
     
    return ask_sub_service_message,ask_sub_service_options

def ask_sub_service_fun(cust_responses):
    print("inside ask sub service function")

    #ask_sub_service_message = "メニューから項目を選択してください。"
    ask_sub_service_message = "どんなメニューですか？"
    sub_service_dict = cust_responses["sub_service_dict"] 
   
    ask_sub_service_options = []
    for sub_service in sub_service_dict:
        value = str(sub_service_dict[sub_service]["item"]) + " : " + str(sub_service_dict[sub_service]["price"])
        #option = {"key": sub_service, "value": sub_service_dict[sub_service]} 
        option = {"key": sub_service, "value": value} 
        ask_sub_service_options.append(option)
     
    return ask_sub_service_message,ask_sub_service_options



def show_avail_options():
    return session['cust_avail_msg']

def ask_if_alt_salon_fun():

    ask_if_alt_salon_options = [
    {"key":"1", "value": "はい"},
    {"key":"2", "value": "いいえ"},
    ]

    return is_confirm_message,is_confirm_options


def is_confirm_fun():
#is_confirm_options = ["1) はい / Yes", "2) いいえ / No"]
#is_confirm_options = {"1": "はい / Yes", "2": "いいえ / No"}

    is_confirm_options = [
    {"key":"1", "value": "はい"},
    #{"key":"2", "value": "いいえ"},
    {"key":"2", "value": "他の日付を確認する"},
    {"key":"3", "value": "今、予約をとるのをやめる"},
    ]

    return is_confirm_message,is_confirm_options


def ask_name():
    return get_name_message

def check_name(name):
    name_status = 0
    if not name:
        name_status = 0
        return name_status, empty_name_message
    else:
        name_status = 1
        return name_status, all_okay_message


def check_is_nickname(is_nickname_menu_int):

    is_nickname_status = 0

    try:
        is_nickname_menu_int = int(is_nickname_menu_int)
    except:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message
        return is_nickname_status, is_nickname_response, out_msg


    if is_nickname_menu_int != 1 and is_nickname_menu_int != 2:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message

    if is_nickname_menu_int == 1:
        is_nickname_status = 1
        is_nickname_response = "yes"
        out_msg = all_okay_message

    if is_nickname_menu_int == 2:
        is_nickname_status = 1
        is_nickname_response = "no"
        out_msg = all_okay_message

    return is_nickname_status, is_nickname_response, out_msg

def check_is_confirm(is_confirm_menu_int):

    is_confirm_status = 0

    try:
        is_confirm_menu_int = int(is_confirm_menu_int)
    except:
        is_confirm_status = 0
        is_confirm_response = None
        out_msg = wrong_is_confirm_message
        return is_confirm_status, is_confirm_response, out_msg


    #if is_confirm_menu_int != 1 and is_confirm_menu_int != 2:
    #    is_confirm_status = 0
    #    is_confirm_response = None
    #    out_msg = wrong_is_confirm_message

    is_confirm_status = 0
    is_confirm_response = None
    out_msg = wrong_is_confirm_message
    
    if is_confirm_menu_int == 1:
        is_confirm_status = 1
        is_confirm_response = "yes"
        out_msg = all_okay_message

    if is_confirm_menu_int == 2:
        is_confirm_status = 1
        is_confirm_response = "no"
        out_msg = all_okay_message

    if is_confirm_menu_int == 3:
        is_confirm_status = 1
        is_confirm_response = "stop"
        out_msg = all_okay_message

    return is_confirm_status, is_confirm_response, out_msg



def check_is_reservation_now(is_reservation_now_menu_int):

    is_reservation_now_status = 0

    try:
        is_reservation_now_menu_int = int(is_reservation_now_menu_int)
    except:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message
        return is_reservation_now_status, is_reservation_now_response, out_msg


    if is_reservation_now_menu_int != 1 and is_reservation_now_menu_int != 2:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message

    if is_reservation_now_menu_int == 1:
        is_reservation_now_status = 1
        is_reservation_now_response = "yes"
        out_msg = all_okay_message

    if is_reservation_now_menu_int == 2:
        is_reservation_now_status = 1
        is_reservation_now_response = "no"
        out_msg = all_okay_message

    return is_reservation_now_status, is_reservation_now_response, out_msg


def check_nickname(nickname):
    nickname_status = 0
    if not nickname:
        nickname_status = 0
        return nickname_status, empty_nickname_message
    else:
        nickname_status = 1
        return nickname_status, all_okay_message


def check_is_time_for_more(is_time_for_more_menu_int):

    is_time_for_more_status = 0

    try:
        is_time_for_more_menu_int = int(is_time_for_more_menu_int)
    except:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message
        return is_time_for_more_status, is_time_for_more_response, out_msg


    if is_time_for_more_menu_int != 1 and is_time_for_more_menu_int != 2:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message

    if is_time_for_more_menu_int == 1:
        is_time_for_more_status = 1
        is_time_for_more_response = "yes"
        out_msg = all_okay_message

    if is_time_for_more_menu_int == 2:
        is_time_for_more_status = 1
        is_time_for_more_response = "no"
        out_msg = all_okay_message

    return is_time_for_more_status, is_time_for_more_response, out_msg


def check_cust_type_of_salon(cust_type_of_salon_menu_int_list):
    print("inside check type of salon")
    print(cust_type_of_salon_menu_int_list)

    cust_type_of_salon_status = 0

    try:
        for menu_int in cust_type_of_salon_menu_int_list:
            print(menu_int)
            menu_int = int(menu_int)
    except:
        print("inside except")
        cust_type_of_salon_status = 0
        cust_type_of_salon_response = None
        out_msg = wrong_cust_type_of_salon_message
        return cust_type_of_salon_status, cust_type_of_salon_response, out_msg
    print("done with try except")

    salon_types = []

    print("cust_type_of_salon_menu_int_list")
    print(cust_type_of_salon_menu_int_list)
    
    for menu_int in cust_type_of_salon_menu_int_list:
        salon_type_name = type_of_salon_menu_int_to_name(int(menu_int))
        salon_types.append(salon_type_name)
    print("salon_types")
    print(salon_types)
 
    wrong_type = 0
    
    for s_type in salon_types:
        print("s_type")
        print(s_type)
        if s_type == "nothing":
            wrong_type = 1
            break
    
    if wrong_type == 1:
            cust_type_of_salon_status = 0
            cust_type_of_salon_response = None
            out_msg = wrong_cust_type_of_salon_message

    else:
        cust_type_of_salon_status = 1
        cust_type_of_salon_response = salon_types
        out_msg = all_okay_message

    return cust_type_of_salon_status, salon_types, out_msg



def check_often_service(check_often_list):

    often_service_status = 1
    response_list = []

    for item in check_often_list:
   
        if item == "1":
            response_list.append("ヘアサロン")

        if item == "2":
            response_list.append("ネイルサロン")

        if item == "3":
            response_list.append("アイラッシュサロン")
        
        if item == "4":
            response_list.append("リラクゼーションサロン")
       
        if item == "5":
            response_list.append("エステサロン")
      
    return often_service_status, response_list

def check_free_time(free_time_menu_int):

    free_time_status = 1
   
    if free_time_menu_int == "1":
        free_time_response = "午前"

    if free_time_menu_int == "2":
        free_time_response = "午後"

    if free_time_menu_int == "3":
        free_time_response = "夕方以降"
    
    return free_time_status, free_time_response

def check_hair_frequency(hair_frequency_menu_int):

    hair_frequency_status = 1
   
    if hair_frequency_menu_int == "1":
        hair_frequency_response = "３週間に１度"

    if hair_frequency_menu_int == "2":
        hair_frequency_response = "月に１度"

    if hair_frequency_menu_int == "3":
        hair_frequency_response = "２ヶ月に１度"
    
    return hair_frequency_status, hair_frequency_response


def check_nails_frequency(nails_frequency_menu_int):

    nails_frequency_status = 1
   
    if nails_frequency_menu_int == "1":
        nails_frequency_response = "３週間に１度"

    if nails_frequency_menu_int == "2":
        nails_frequency_response = "月に１度"

    if nails_frequency_menu_int == "3":
        nails_frequency_response = "２ヶ月に１度"
    
    return nails_frequency_status, nails_frequency_response


def check_eyelash_frequency(eyelash_frequency_menu_int):

    eyelash_frequency_status = 1
   
    if eyelash_frequency_menu_int == "1":
        eyelash_frequency_response = "３週間に１度"

    if eyelash_frequency_menu_int == "2":
        eyelash_frequency_response = "月に１度"

    if eyelash_frequency_menu_int == "3":
        eyelash_frequency_response = "２ヶ月に１度"
    
    return eyelash_frequency_status, eyelash_frequency_response



def check_relaxation_frequency(relaxation_frequency_menu_int):

    relaxation_frequency_status = 1
   
    if relaxation_frequency_menu_int == "1":
        relaxation_frequency_response = "３週間に１度"

    if relaxation_frequency_menu_int == "2":
        relaxation_frequency_response = "月に１度"

    if relaxation_frequency_menu_int == "3":
        relaxation_frequency_response = "２ヶ月に１度"
    
    return relaxation_frequency_status, relaxation_frequency_response

def check_aesthetic_frequency(aesthetic_frequency_menu_int):

    aesthetic_frequency_status = 1
   
    if aesthetic_frequency_menu_int == "1":
        aesthetic_frequency_response = "３週間に１度"

    if aesthetic_frequency_menu_int == "2":
        aesthetic_frequency_response = "月に１度"

    if aesthetic_frequency_menu_int == "3":
        aesthetic_frequency_response = "２ヶ月に１度"
    
    return aesthetic_frequency_status, aesthetic_frequency_response


def check_free_days(free_days_menu_int):

    free_days_status = 1
   
    if free_days_menu_int == "1":
        free_days_response = "平日"

    if free_days_menu_int == "2":
        free_days_response = "週末"

    if free_days_menu_int == "3":
        free_days_response = "どちらも"	

    return free_days_status, free_days_response



def check_is_specific_salon(is_specific_salon_menu_int):

    is_specific_salon_status = 1
    is_specific_salon = 0

    if is_specific_salon_menu_int == "1":
        is_specific_salon_response = "はい"
        is_specific_salon = 1

    if is_specific_salon_menu_int == "2":
        is_specific_salon_response = "いいえ"
    
    return is_specific_salon_status, is_specific_salon_response, is_specific_salon



def check_is_daily_horoscope(is_daily_horoscope_menu_int):

    is_daily_horoscope_status = 1
    is_daily_horoscope = 0

    if is_daily_horoscope_menu_int == "1":
        is_daily_horoscope_response = "はい"
        is_daily_horoscope = 1

    if is_daily_horoscope_menu_int == "2":
        is_daily_horoscope_response = "いいえ"
    
    return is_daily_horoscope_status, is_daily_horoscope_response, is_daily_horoscope



def check_is_believe_in_signs(is_believe_in_signs_menu_int):

    print("Here---------------")
    is_believe_in_signs_status = 1
    is_believe_in_signs = 0

    if is_believe_in_signs_menu_int == "1":
        is_believe_in_signs_response = "はい"
        is_believe_in_signs = 1

    if is_believe_in_signs_menu_int == "2":
        is_believe_in_signs_response = "私にとって良いことなら信じる :D"
        is_believe_in_signs = 1

    if is_believe_in_signs_menu_int == "3":
        is_believe_in_signs_response = "いいえ"
    
    return is_believe_in_signs_status, is_believe_in_signs_response, is_believe_in_signs


def check_chat_more(chat_more_menu_int):

    chat_more_status = 1
    is_working = 0
   
    if chat_more_menu_int == "1":
        chat_more_response = "はい、仕事をしています。"
        is_working = 1

    if chat_more_menu_int == "2":
        chat_more_response = "いいえ、今は仕事をしていません。"

    if chat_more_menu_int == "3":
        chat_more_response = "私は学生です。"
    
    if chat_more_menu_int == "4":
        chat_more_response = "私は主婦です。"
    
    return chat_more_status, chat_more_response, is_working


def check_new_welcome(new_welcome_menu_int, cust_responses):

    new_welcome_status = 1
   
    cust_id = cust_responses["customer_id"]

    #print("\n\n\n----------")
    #print("Cust Id: ",cust_id) 
    is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id) 
    #print("\n\n\n----------")
    if is_rsv == 1:
        
        if new_welcome_menu_int == "1":
            new_welcome_response = "new_reservation"

        if new_welcome_menu_int == "2":
            new_welcome_response = "cancel_reservation"

        if new_welcome_menu_int == "3":
            new_welcome_response = "change_reservation"
        
        if new_welcome_menu_int == "4":
            new_welcome_response = "what_do_you_know"
        
        if new_welcome_menu_int == "5":
            new_welcome_response = "chat_more"


    else:
        
        if new_welcome_menu_int == "1":
            new_welcome_response = "new_reservation"

        if new_welcome_menu_int == "2":
            new_welcome_response = "what_do_you_know"
        
        if new_welcome_menu_int == "3":
            new_welcome_response = "chat_more"

    return new_welcome_status, new_welcome_response


def check_service(cust_service_menu_int,cust_responses):
    
    cust_service_status = 0
    try:
        cust_service_menu_int = int(cust_service_menu_int)
    except:
        
        cust_service_status = 0
        cust_service_id = None
        cust_service_name = ""
        out_msg = wrong_cust_service_message
        
        return cust_service_status,cust_service_id,cust_service_name,out_msg

    found = 0
    selected_option = {}
    
    for option in cust_responses["service_dict"]:
        if str(cust_service_menu_int) == option:
            found = 1
            cust_service_id = cust_responses["service_dict"][option]["id"]
            cust_service_name = cust_responses["service_dict"][option]["name"]
            break

    if found == 0:
        cust_service_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        cust_service_status = 1
        out_msg = all_okay_message

    return cust_service_status,cust_service_id,cust_service_name,out_msg


def check_sub_service(cust_sub_service_menu_int,cust_responses):
    print("Check Sub Service Function")
    print("cust_sub_service_menu_int")
    print(cust_sub_service_menu_int)
     
    cust_sub_service_status = 0
    try:
        cust_sub_service_menu_int = int(cust_sub_service_menu_int)
    except:
        ss_status = 0
        ss_id = 0
        ss_name = "" 
        ss_duration = 0
        ss_price = 0
        out_msg = wrong_cust_sub_service_message
        return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg
    
    print("Done with try catch") 
    found = 0
    selected_option = {}
    print("ssdict")
    print(cust_responses["sub_service_dict"])

    
    for option in cust_responses["sub_service_dict"]:
        print("HHH")
        print(option)
        print(cust_sub_service_menu_int)
        if str(cust_sub_service_menu_int) == option:
            print("found")
            found = 1
            ss_id = cust_responses["sub_service_dict"][option]["id"]
            ss_name = cust_responses["sub_service_dict"][option]["item"]
            ss_duration = cust_responses["sub_service_dict"][option]["duration"]
            ss_price = cust_responses["sub_service_dict"][option]["price"]
            break
        else:
            print("not found")
            ss_id = 0
            ss_name = "" 
            ss_duration = 0 
            ss_price = ""

    if found == 0:
        print("I am not found")
        ss_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        print("I am found")
        ss_status = 1
        out_msg = all_okay_message
    
    
    return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg




def check_avail_options(cust_avail_options_menu_int, avail_display_options):
    cust_avail_options_status = 0
    try:
        cust_avail_options_menu_int = int(cust_avail_options_menu_int)
    except:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message
        return cust_avail_options_status, cust_avail_options_response, out_msg

    #avail_options_id = avail_options_menu_int_to_id(cust_avail_options_menu_int)
    found = 0
    selected_option = [0,0,0]
    print("HELLO")
    for option in avail_display_options:
        print(option)
        print(option[0])
        if cust_avail_options_menu_int == option[0]:
            found = 1
            selected_option = option
            break # This works without "break" only because I have not added ELSE part

    if found == 0:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message

    elif found == 1:
        cust_avail_options_status = 1
        cust_avail_options_response = selected_option
        out_msg = all_okay_message

    return cust_avail_options_status, selected_option, out_msg



def check_phone(phone):
    phone_status = 0
    if not phone:
        phone_status = 0
        return phone_status, empty_phone_message
    else:
        phone_status = 1
        return phone_status, all_okay_message

def check_color(color_menu_int):
    print("ColorMenuInt: " + str(color_menu_int))
    print("Inside CheckColor")
    color_status = 0
    if not color_menu_int:
        print("Inside NotColorMenuInt")
        color_status = 0
        color_response = 0
        color_idea = 0
        return color_status, color_response, color_idea, wrong_color_message
    else:
        print("Inside Else")
        color_name = color_menu_int_to_name(color_menu_int)
        print("ColorName: " + str(color_name))
        if color_name == "nothing":
            print("Inside ColorNameNothing")
            color_status = 0
            color_response = 0
            color_idea = 0
            return color_status, color_response, color_idea, wrong_color_message
        else:
            print("Inside Inner Else")
            color_status = 1
            color_response = color_name
            color_idea = color_menu_int_to_idea(color_menu_int)
        print("All Okay")
    return color_status, color_response, color_idea, all_okay_message


def check_hobby(hobby_text):
    hobby_status = 0
    if not hobby_text:
        hobby_status = 0
        hobby_idea = 0
        return hobby_status, hobby_idea, wrong_hobby_message
    else:
        print("Inside Else")
        hobby_status = 1
        hobby_idea = hobby_to_idea(hobby_text)
    return hobby_status, hobby_idea, all_okay_message

def check_date(date_inp):
    date_status = 0
    date_obj = None

    try:
        date_obj = datetime.datetime.strptime(date_inp, '%Y-%m-%d')
    except:
        date_status = 0
        return date_obj, date_status, wrong_date_message

    if date_obj is None:
        date_status = 0
        return date_obj, date_status, wrong_date_message
    else:
        date_status = 1
        return date_obj, date_status, all_okay_message



def check_time(time_inp):
    time_status = 0
    dummy_time_inp = "01-01-2000 " + time_inp
    time_obj = None

    try:
        time_obj = datetime.datetime.strptime(dummy_time_inp, '%d-%m-%Y %H:%M')
        print("Time Obj: " + str(time_obj))
    except:
        time_status = 0
        return time_obj, time_status, wrong_time_message

    if time_obj is None:
        time_status = 0
        return time_obj, time_status, wrong_time_message
    else:
        time_status = 1
        return time_obj, time_status, all_okay_message 


def old_ask_date():
    date_str = input(get_date_message)
    date_obj = None

    while date_obj is None:

        try:
            date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y')
    #print ("DateObject:" + str(date_obj))
        except:
            #print(wrong_date_message)
            date_str = input(wrong_date_message)
        return date_obj


"""
"""


def calc_date_time(date_obj,time_obj):
    inp_hour = time_obj.hour
    inp_minute = time_obj.minute
    date_time_obj = date_obj.replace(hour=inp_hour, minute=inp_minute)
    return date_time_obj

##########################################################################
###### CHAT BOT VARIABLES END HERE
##########################################################################


#####################################################################
#####  CHAT BOT API
#####################################################################

# PROGRAM STARTS HERE
app = Flask(__name__)

@app.route('/existingcustomer', methods=['POST'])

def existingcustomer():
    print("inside login session")
    json_input = request.json
    ip = json_input['ip']
    name = json_input['name']
    email = json_input['email']

    if "device_id" in json_input:
        device_id = json_input['device_id']
        device_id = device_id.replace("'","")
        device_id = device_id.replace('"','')
    else: 
        device_id = "DUMMY"

    if "device_type" in json_input:
        device_type = json_input['device_type']
    else:
        device_type = "DUMMY"

    existing_status,c_id,user_id = check_existing_customer(name,email)

    if existing_status == 0:
        return_dict = {"status":"error", "message": wrong_customer_message}
        out_json = json.dumps(return_dict,ensure_ascii= False)
        return out_json

    else:
        return_list_of_dicts = []
        return_dict = {}
        return_dict["status"] = "success"
        return_dict["error_msg"] = ""
        return_dict["chat"] = return_list_of_dicts
        cust_responses = {}
        cust_responses["customer_id"] = c_id
        cust_responses["user_id"] = user_id
        cust_responses["device_id"] = device_id
        cust_responses["device_type"] = device_type
        
        STATE = "NEW_WELCOME" 
        insert_into_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
        
        return_dict = {"status":"success", "message": "", "user_id":"102" }
        
        out_json = json.dumps(return_dict,ensure_ascii= False)
        return out_json

   
@app.route('/review', methods=['POST'])

def review():
    print("inside review")
    json_input = request.json
    
    ip = json_input['ip']
    user_id = json_input['user']
    if "user" in json_input:
        if json_input["user"]: 
            user_id = json_input["user"]
        else:
            user_id = "0"
    else:
        user_id = "0"

    rating = json_input['rating']

    print("here")

    st,cid = get_cid_from_ip(ip)
    if st == 1:
        insert_into_ratings_table(user_id,cid,rating)
        out_dict = {"status":"success"}  
        out_json = json.dumps(out_dict,ensure_ascii= False)
        return out_json 
    else:
        out_dict = {"status":"error"}  
        out_json = json.dumps(out_dict,ensure_ascii= False)
        return out_json 

"""   
@app.route('/newcustomer', methods=['POST'])
def newcustomer():
    print("inside login session")
    json_input = request.json
    ip = json_input['ip']
    mobile = json_input['mobile']
    email = json_input['email']
    return_list_of_dicts = []
    return_dict = {}
    return_dict["status"] = "success"
    return_dict["error_msg"] = ""
    return_dict["chat"] = return_list_of_dicts
    cust_responses = {}
    STATE = "FIRST_WELCOME" 
    insert_into_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
    return "Hey Welcome" 
""" 
   
@app.route('/dropsession', methods=['POST'])

def dropsession():
    print("inside drop session")
    json_input = request.json
    ip = json_input['ip']
    print("IP:",ip)

    sql = "DELETE FROM sessions WHERE ip = %s"
    delete_tuple = (ip,)
    
    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,delete_tuple)
    mydb.commit()
    mycursor.close()
    mydb.close()

    #DELETE FROM table_name WHERE condition;
    return "dropped\n"

@app.route('/chat', methods=['POST'])

def chat():

    print("START")
    print("I am inside chat method")
    print("Inside CHAT")
    json_input = request.json

    ip = json_input['ip']
    inp_msg  = json_input['message']
    
    
    #if "user" in json_input:
    #    user_id = json_input['user']
    #else:
    #    user_id = 102

    print("\n\n\n\n\n\n\n\n")
    print(ip)
    print("\n\n\n\n\n\n\n\n")
    
    sql = """select * from sessions where ip = %s """
    data = (ip,)

    mydb,mycursor = create_sql_conn()
    mycursor.execute(sql,data)
    myresult_list = mycursor.fetchall()
    mycursor.close() 
    mydb.close()
    
    #emp_name_dict = dict()

    print("Myresult",type(myresult_list),"List")
    #print(myresult_list)
    #return "nothing"

    if len(myresult_list) != 0:
        print("matched")
        #myfirst_tuple = None
        myfirst_tuple = myresult_list[0]
        #if myfirst_tuple is not None:
        ip= myfirst_tuple[0]
        #cust_name= myfirst_tuple[1]
        #is_nickname= myfirst_tuple[2]
        #cust_nickname= myfirst_tuple[3]
        #cust_birthday= myfirst_tuple[4]
        #cust_phone= myfirst_tuple[5]
        #cust_is_time_for_more= myfirst_tuple[6]
        #cust_color= myfirst_tuple[7]
        #cust_type_of_salon= myfirst_tuple[8]
        #cust_is_reservation_now= myfirst_tuple[9]
        #cust_date= myfirst_tuple[10]
        #cust_service_id= myfirst_tuple[11]
        #cust_avail_msg=myfirst_tuple[12]
        #cust_avail_display_options= myfirst_tuple[13]
        #cust_avail_display_options = list(cust_avail_display_options)
        #cust_avail_option_list= myfirst_tuple[14]
        #cust_avail_option_list = list(cust_avail_option_list)



        print("\n\n\n I am here1 \n\n\n")
        return_list_of_dicts = []
        
        return_list_of_dicts_1= myfirst_tuple[15]
        #return_list_of_dicts_proc=list(return_list_of_dicts_proc)

        print("\n\n\nReturn List OF Dicts PROC\n\n\n")
        #print(return_list_of_dicts_1)
        #print(type(return_list_of_dicts_1))

        print("\n\n\n\n\n")
        print("HEllo")
        print(return_list_of_dicts_1) 
        print("\n\n\n\n\n")



        return_list_of_dicts_2 = return_list_of_dicts_1.replace("'", "\"")

        print("\n\n\n\n\n")
        print("HEllo")
        print(return_list_of_dicts_2) 
        print("\n\n\n\n\n")
         
        return_list_of_dicts = json.loads(return_list_of_dicts_2)
        #return_list_of_dicts = json.loads(return_list_of_dicts_1)
        #return "nothing"
         
        #print(return_list_of_dicts)
        #print(type(return_list_of_dicts))

        print("\n\n\n I am here2 \n\n\n")
        #count = 0


        #return "nothing"
        """
        """
        #cust_duration= myfirst_tuple[16]
        STATE= myfirst_tuple[17]

        return_dict_str= myfirst_tuple[18]
        return_dict_accept_str = return_dict_str.replace("'", "\"")
        return_dict = json.loads(return_dict_accept_str)
        print("here2.5")
        cust_responses_str= myfirst_tuple[19]
        cust_responses_accept_str = cust_responses_str.replace("'", "\"")


        print("cust responses acc\n")
        #print(cust_responses_accept_str)
        print("\ncust responses acc\n")

        cust_responses = json.loads(cust_responses_accept_str)
        print("here3")
        #return_dict= dict(return_dict)
        #print(session)
        #return "hello"
    else:
        print("unmatched")
        STATE= "FIRST_WELCOME"
        cust_name= ""
        cust_firstname= ""
        cust_lastname= ""
        is_nickname= ""
        cust_nickname= ""
        cust_birthday= ""
        is_time_for_more= ""
        cust_phone= ""
        cust_color= ""
        cust_type_of_salon= ""
        is_reservation_now= ""
        cust_date_obj= ""
        cust_service_id= ""
        cust_avail_msg= ""
        cust_avail_display_options= []
        cust_avail_option_list= []
        cust_responses= {}
        return_list_of_dicts= []
        return_dict= {}
        duration= 2



    print("Return Dicts")
    #print(type(return_dict))
    #return "okay"

    #print(type(cust_avail_display_options))
    #print(type(cust_avail_option_list))
    #print(type(return_list_of_dicts))

    #return("okay")
    #if 'user' not in session:
    #    return "yes are not logged in"
    print("Inside CHAT")
    #print("Session", session)
    print(STATE)
    print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
    #return "nothing"

    
    if inp_msg == "init" and STATE != "FIRST_WELCOME":
        
        if STATE == "NEW_WELCOME":
            out_msg_1,out_msg_2,option_list = new_welcome_fun(cust_responses)
            STATE = "NEW_WELCOME_ASKED"
            
            return_dict["rid"] = ""

            if "booked_just_now" in cust_responses:
                if cust_responses["booked_just_now"] == 1:
                    rsv_id = cust_responses["rsv_id"]
                    return_dict["rid"] = str(rsv_id)
                cust_responses["booked_just_now"] = 0  
            
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "new_welcome_1"
            }
            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "new_welcome_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        else:
            print("ReturnDict")

            if return_dict["status"] == "failure":
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""   
                return_dict["rid"] = ""
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
      
    
    return_dict["rid"] = ""

    while True:
        print("loop")

        if STATE == "FIRST_WELCOME":
            if "device_id" in json_input: 
                device_id = json_input['device_id']
                device_id = device_id.replace("'","")
                device_id = device_id.replace('"','')
            else:
                device_id = "DUMMY"

            if "device_type" in json_input: 
                device_type = json_input['device_type']
            else:
                device_type = "DUMMY"


            cust_responses["device_id"] = device_id
            cust_responses["device_type"] = device_type
            
            out_msg = first_welcome_fun()
            STATE = "WELCOME_MESSAGE_SHOWN"
            
            out_dict = {"type" : "text", "question": out_msg,"qid": "first_welcome"}
            return_list_of_dicts.append(out_dict)
       
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            insert_into_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
         
        if STATE == "WELCOME_MESSAGE_SHOWN":
            
            if inp_msg == "init2":
                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts
                STATE = "ASK_NAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = "ウェルカムメッセージを表示した後にinit2を受信しなかった" 
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_NAME":
            out_msg_1,out_msg_2 = ask_lastname_fun()
            STATE = "NAME_ASKED"

            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none", 
                "qid": "ask_last_name_1"
            }
            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "input", 
                "question": out_msg_2, 
                "message_type": "name", 
                "place_holder": "氏",
                "qid": "ask_last_name_2"
            }
            return_list_of_dicts.append(out_dict)
            
            
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        
        if STATE == "NAME_ASKED":
            cust_name = inp_msg
            name_st,out_msg = check_name(cust_name)
            if name_st == 1:
                #cust_responses["name"] = cust_name
                cust_responses["last_name"] = cust_name

                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type": "text", "answer": cust_name, "message_type": "none","qid": "ask_name"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "ASK_FIRST_NAME"
                #STATE = "IS_NICKNAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_FIRST_NAME":
            out_msg = ask_firstname_fun()
            STATE = "FIRST_NAME_ASKED"

            out_dict = {
                "type" : "input", 
                "question": out_msg, 
                "message_type": "name", 
                "place_holder": "名",
                "qid": "ask_first_name"
            }
            return_list_of_dicts.append(out_dict)
            
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        
        if STATE == "FIRST_NAME_ASKED":
            cust_name = inp_msg
            name_st,out_msg = check_name(cust_name)
            if name_st == 1:
                cust_responses["first_name"] = cust_name

                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type": "text", "answer": cust_name, "message_type": "none","qid": "ask_name"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "IS_NICKNAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "IS_NICKNAME":
            out_msg_1,out_msg_2,option_list = is_nickname_fun()
            STATE = "IS_NICKNAME_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "is_nickname"
            }

            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "is_nickname"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json


        if STATE == "IS_NICKNAME_ASKED":
            print("I am here")
            is_nickname_menu_int = inp_msg
            
            is_nickname_status,is_nickname_response,out_msg = check_is_nickname(is_nickname_menu_int)
            
            if is_nickname_status == 1:
                cust_responses["is_nickname"] = is_nickname_response
            
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if is_nickname_response == "yes":
                    is_nickname_response_jap = "はい"
                else:
                    is_nickname_response_jap = "いいえ"
               
                out_dict = {"type": "text", "answer": is_nickname_response_jap, "message_type": "none","qid": "is_nickname"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                if is_nickname_response == "yes":
                    STATE = "ASK_NICKNAME"
                elif is_nickname_response == "no":
                    #STATE = "FIND_SALON"
                    STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_NICKNAME":
            print("JJJJJ")
            out_msg = ask_nickname_fun()
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {"type" : "input", "question": out_msg, "message_type": "none","qid": "ask_nickname"}
            return_list_of_dicts.append(out_dict)
            STATE = "NICKNAME_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)

            return out_json

        if STATE == "NICKNAME_ASKED":
            print("KKKKKK")
            cust_nickname = inp_msg
            nickname_status,out_msg = check_name(cust_nickname)
            if nickname_status == 1:
                cust_responses["nickname"] = cust_nickname
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_nickname, "message_type": "none","qid": "ask_nickname"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "FIND_SALON"
                
                STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_BIRTHDAY":
            if cust_responses["is_nickname"] == "yes": 
            
                out_msg_1,out_msg_2 = ask_birthday_fun(cust_responses)
                STATE = "BIRTHDAY_ASKED"
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {
                    "type" : "text", 
                    "question": out_msg_1, 
                    "message_type": "none", 
                    "qid": "ask_birthday_1"
                }
                return_list_of_dicts.append(out_dict)
                
                out_dict = {
                    "type" : "input", 
                    "question": out_msg_2, 
                    "message_type": "date", 
                    "place_holder": "1993年06月09日",
                    "qid": "ask_birthday_2"
                }

                return_list_of_dicts.append(out_dict)
                out_json = json.dumps(return_dict,ensure_ascii= False)
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else: 
                out_msg = ask_birthday_fun(cust_responses)
                STATE = "BIRTHDAY_ASKED"
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {
                    "type" : "input", 
                    "question": out_msg, 
                    "message_type": "date", 
                    "place_holder": "1993年06月09日",
                    "qid": "ask_birthday_wo_nn"
                }
                return_list_of_dicts.append(out_dict)
                out_json = json.dumps(return_dict,ensure_ascii= False)
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "BIRTHDAY_ASKED":
            cust_birthday_inp = inp_msg
            jap = 0
            cust_birthday_inp_plus_day_sym = cust_birthday_inp + "日"
            #cust_birthday_inp_plus_day_sym = cust_birthday_inp 
            
            try:
                check_cust_birthday = datetime.datetime.strptime(cust_birthday_inp, '%Y-%m-%d')
            except:
                birthday_status,birthday_obj,out_msg = get_date_in_ddmmyyyy_format(cust_birthday_inp)
                birthday_str = str(birthday_obj)
                jap = 1

            if jap != 1:
                birthday_obj,birthday_status,out_msg = check_date(cust_birthday_inp)
                birthday_str = str(birthday_obj)

            
            if birthday_status == 1:

            
                cust_responses["birthday"] = birthday_str
                
                cust_zodiac = get_zodiac(birthday_obj) 
                cust_responses["zodiac"] = cust_zodiac 
                zodiac_eng = zodiac_jap_to_eng[cust_zodiac]
                cust_responses["zodiac_eng"] = zodiac_eng
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "status": "success", 
                    "answer": cust_birthday_inp_plus_day_sym, 
                    "message_type": "none",
                    "qid": "ask_birthday"
                }

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_PHONE"
                STATE = "IS_BELIEVE_IN_SIGNS"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "IS_BELIEVE_IN_SIGNS":
            out_msg_1,out_msg_2,option_list = is_believe_in_signs_fun(cust_responses)

            STATE = "IS_BELIEVE_IN_SIGNS_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none", 
                "qid": "is_believe_in_signs_1"
            }
            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "option", 
                "question": out_msg_2,
                "option_list": option_list, 
                "message_type": "none", 
                "qid": "is_believe_in_signs_2"
            }
            return_list_of_dicts.append(out_dict)
            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "IS_BELIEVE_IN_SIGNS_ASKED":

            print("Here---------------")
            is_believe_in_signs_menu_int = inp_msg
            
            ibis_status,ibis_response,ibis = check_is_believe_in_signs(is_believe_in_signs_menu_int)


            if ibis_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": ibis_response, "message_type": "none","qid": "is_belive_in_signs"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                if ibis == 0:
                    cust_responses["is_believe_in_signs"] = "no"
                    #STATE = "IS_SPECIFIC_SALON"
                    STATE = "ASK_PHONE"

                if ibis == 1:
                    cust_responses["is_believe_in_signs"] = "yes"
                    STATE = "IS_DAILY_HOROSCOPE"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "IS_DAILY_HOROSCOPE":
            out_msg,option_list = is_daily_horoscope_fun()


            STATE = "IS_DAILY_HOROSCOPE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "message_type": "none", 
                "option_list": option_list,
                "qid": "is_daily_horoscope"
            }
            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "IS_DAILY_HOROSCOPE_ASKED":
            is_daily_horoscope_menu_int = inp_msg
            
            idh_status,idh_response,idh = check_is_daily_horoscope(is_daily_horoscope_menu_int)


            if idh == 0:
                cust_responses["is_daily_horoscope"] = "no"

            if idh == 1:
                cust_responses["is_daily_horoscope"] = "yes"

            if idh_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": idh_response, "message_type": "none","qid": "is_daily_horoscope"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "IS_SPECIFIC_SALON"
                STATE = "ASK_PHONE"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "IS_SPECIFIC_SALON":

            #out_msg_1,out_msg_2,option_list = is_specific_salon_fun(cust_responses)
            out_msg,option_list = is_specific_salon_fun(cust_responses)
            STATE = "IS_SPECIFIC_SALON_ASKED"


            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "message_type": "none", 
                "option_list": option_list,
                "qid": "is_specific_salon"
            }
            return_list_of_dicts.append(out_dict)
            
            """
            if cust_responses["is_believe_in_signs"] == "no":
                STATE = "IS_SPECIFIC_SALON_ASKED"
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {
                    "type" : "option", 
                    "question": out_msg_2, 
                    "message_type": "none", 
                    "option_list": option_list,
                    "qid": "is_specific_salon"
                }
                return_list_of_dicts.append(out_dict)
            
            else:

                STATE = "IS_SPECIFIC_SALON_ASKED"
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "question": out_msg_1, 
                    "message_type": "none", 
                    "qid": "is_specific_salon_1"
                }
                return_list_of_dicts.append(out_dict)
                
                out_dict = {
                    "type" : "option", 
                    "question": out_msg_2, 
                    "message_type": "none", 
                    "option_list": option_list,
                    "qid": "is_specific_salon_2"
                }
                return_list_of_dicts.append(out_dict)
            """ 
            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "IS_SPECIFIC_SALON_ASKED":
            is_specific_salon_menu_int = inp_msg
            
            iss_status,iss_response,iss = check_is_specific_salon(is_specific_salon_menu_int)

            if iss_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": iss_response, "message_type": "none","qid": "is_specific_salon"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                if iss == 0:
                    cust_responses["is_specific_salon"] = "no"
                    #STATE = "ASK_PHONE"
                    STATE = "FIND_SALON"

                if iss == 1:
                    cust_responses["is_specific_salon"] = "yes"
                    STATE = "ASK_SPECIFIC_SALON"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_SPECIFIC_SALON":
            out_msg = ask_specific_salon_fun()

            STATE = "SPECIFIC_SALON_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "input", 
                "question": out_msg, 
                "message_type": "none", 
                "qid": "ask_specific_salon"
            }
            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "SPECIFIC_SALON_ASKED":
            ss_response = inp_msg

            print(ss_response)

            #if ss_response == "Majestic Beauty" or ss_response == "マジェスティックビューティー":
            if "Majestic" in ss_response or "majestic" in ss_response or  "マジェスティッ" in ss_response:
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 102

            elif "ハイパーナイフ痩身小顔専門店salon de me" in ss_response or "salon de me" in ss_response or "ハイパーナイフ痩身小顔専門店" in ss_response:
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 592 
            
            elif "LunaTiara" in ss_response or "lunatiara" in ss_response or "tiara" in ss_response or "luna tiara" in ss_response:
                print("Inside LunaTiarra")
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 626 
            
            elif "La Luna" in ss_response or "la luna" in ss_response or "laluna" in ss_response or "LaLuna" in ss_response:
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 627 
            
            elif "cellestia" in ss_response or "Cellestia" in ss_response or "cell" in ss_response or "Cell" in ss_response:
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 628 
            
            else:
                cust_responses["salon_found"] = "no"
                cust_responses["user_id"] = 102

            ss_status = 1

            if ss_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": ss_response, "message_type": "none","qid": "ask_specific_salon"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                #STATE = "ASK_PHONE"

                if cust_responses["salon_found"] == "yes":
                    STATE = "CONFIRM_SPECIFIC_SALON"
                
                if cust_responses["salon_found"] == "no":
                    STATE = "USE_RECOMMENDED_SALON"
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "CONFIRM_SPECIFIC_SALON":
            out_msg_1,out_msg_2,option_list_1,option_list_2 = confirm_specific_salon_fun(cust_responses)

            STATE = "CONFIRM_SPECIFIC_SALON_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {
                "type" : "gallery_option", 
                "question": out_msg_1, 
                "gallery_list": option_list_1,
                "message_type": "gallery", 
                "qid": "confirm_specific_salon_1"
            }

            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list_2,
                "message_type": "none", 
                "qid": "confirm_specific_salon_2"
            }

            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)


            print("YAAAAAHAAAAAAN HOOOOON BC")




            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "CONFIRM_SPECIFIC_SALON_ASKED":
            css_status = 1 
            css_response = inp_msg


            if css_response == "1":
                css_answer = "はい"
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 102
            if css_response == "2":
                css_answer = "いいえ"
                cust_responses["salon_found"] = "no"
                cust_responses["user_id"] = 0 


            if css_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": css_answer, "message_type": "none","qid": "confirm_specific_salon"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_responses["salon_found"] == "yes":
                    STATE = "IS_RESERVATION_NOW"
                if cust_responses["salon_found"] == "no":
                    STATE = "ASK_SALON_AGAIN"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json
        
        if STATE == "ASK_SALON_AGAIN":
            out_msg = ask_salon_again_fun()

            STATE = "SALON_AGAIN_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "input", 
                "question": out_msg, 
                "message_type": "none", 
                "qid": "ask_salon_again"
            }
            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "SALON_AGAIN_ASKED":
            sa_response = inp_msg

            if sa_response == "Majestic Beauty" or sa_response == "マジェスティックビューティー":
                cust_responses["salon_found"] = "no"
                cust_responses["user_id"] = 0 
            else:
                cust_responses["salon_found"] = "no"
                cust_responses["user_id"] = 0 
            # The above code block looks bizarre because currently there's just one salon

            sa_status = 1

            if sa_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": sa_response, "message_type": "none","qid": "ask_salon_again"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                #STATE = "ASK_PHONE"

                #if cust_responses["salon_found"] == "yes":
                #    STATE = "CONFIRM_SPECIFIC_SALON"
                
                if cust_responses["salon_found"] == "no":
                    STATE = "USE_RECOMMENDED_SALON"
                     
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "USE_RECOMMENDED_SALON":
            out_msg,option_list = use_recommended_salon_fun()

            STATE = "USE_RECOMMENDED_SALON_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list,
                "message_type": "none", 
                "qid": "use_recommended_salon"
            }

            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "USE_RECOMMENDED_SALON_ASKED":
            urs_status = 1 
            urs_response = inp_msg


            if urs_response == "1":
                urs_answer = "はい"
                cust_responses["salon_found"] = "yes"
                cust_responses["user_id"] = 102

            if urs_response == "2":
                urs_answer = "いいえ"
                cust_responses["salon_found"] = "no"
                cust_responses["user_id"] = 0 


            if urs_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": urs_answer, 
                    "message_type": "none",
                    "qid": "use_recommended_salon"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_responses["salon_found"] == "yes":
                    STATE = "IS_RESERVATION_NOW"
                if cust_responses["salon_found"] == "no":
                    STATE = "IS_TIME_FOR_MORE_ASKED_2"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "FIND_SALON":
            out_msg,option_list = find_salon_fun()

            STATE = "FIND_SALON_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {
                "type" : "gallery_option", 
                "question": out_msg, 
                "gallery_list": option_list,
                "message_type": "gallery", 
                "qid": "find_salon"
            }

            return_list_of_dicts.append(out_dict)

            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            return out_json

        if STATE == "FIND_SALON_ASKED":
            fs_response = inp_msg

            if fs_response == "1":
                fs_salon = "マジェスティックビューティ"
                cust_responses["salon"] = fs_salon 
                cust_responses["user_id"] = 102

            if fs_response == "2":
                fs_salon = "ハイパーナイフ痩身小顔専門店salon de me"
                cust_responses["salon"] = fs_salon 
                cust_responses["user_id"] = 592 

            if fs_response == "3":
                fs_salon = "LunaTiara"
                cust_responses["salon"] = fs_salon 
                cust_responses["user_id"] = 626 

            if fs_response == "4":
                fs_salon = "La Luna"
                cust_responses["salon"] = fs_salon 
                cust_responses["user_id"] = 627 

            if fs_response == "5":
                fs_salon = "Cellestia"
                cust_responses["salon"] = fs_salon 
                cust_responses["user_id"] = 628 
            
            ss_status = 1

            if ss_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": fs_salon, "message_type": "none","qid": "ask_specific_salon"}
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "IS_TIME_FOR_MORE_2"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_PHONE":
            out_msg_1,out_msg_2 = ask_phone_fun(cust_responses)
            STATE = "PHONE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
           
            #CHANGE_TEL 
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none", 
                "qid": "ask_phone_1"
            }
            
            #out_dict = {
            #    "type" : "text", 
            #    "question": out_msg_1, 
            #    "message_type": "none", 
            #    "qid": "ask_email_1"
            #}
        
            return_list_of_dicts.append(out_dict)
           
            #CHANGE_TEL 
            out_dict = {
                "type" : "input", 
                "question": out_msg_2, 
                "message_type": "phone", 
                "place_holder": "XXX-XXXX-XXXX",
                "qid": "ask_phone_2"
            }
            
            #out_dict = {
            #    "type" : "input", 
            #    "question": out_msg_2, 
            #    #"message_type": "phone", 
            #    #"place_holder": "XXX-XXXX-XXXX",
            #    "qid": "ask_email_2"
            #}

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "PHONE_ASKED":
            cust_phone = inp_msg
            phone_status,out_msg = check_phone(cust_phone)
           
            if "user_id" in cust_responses:
                user_id = cust_responses["user_id"]
            else:
                user_id = 0 

            if phone_status == 1:
                cust_responses["phone"] = cust_phone
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                # CHANGE_TEL 
                out_dict = {"type" : "text", "answer": cust_phone, "message_type": "none","qid": "ask_phone"}
                #out_dict = {"type" : "text", "answer": cust_phone, "message_type": "none","qid": "ask_email"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
            
                cust_firstname = cust_responses["first_name"]
                cust_lastname = cust_responses["last_name"]
                #cust_name = cust_responses["name"]
                cust_name = cust_lastname + " " + cust_firstname 
                
                if "birthday" in cust_responses:
                    cust_birthday = cust_responses["birthday"]
                else:
                    cust_birthday = "1990-01-01"

                cust_phone = cust_responses["phone"]
                
                if cust_responses["is_nickname"] == "no":
                    cust_responses["nickname"] = ""
                    cust_nickname = ""
                else:
                    cust_nickname = cust_responses["nickname"]

                if "is_daily_horoscope" in cust_responses:
                    if cust_responses["is_daily_horoscope"] == "yes":
                        is_daily_horoscope = 1
                    else:
                        is_daily_horoscope = 0
                else:
                    is_daily_horoscope = 0
                try:
                    cust_zodiac_eng = cust_responses["zodiac_eng"]
                except:
                    cust_zodiac_eng = "cancer"
                
                device_id = cust_responses["device_id"]
                device_type = cust_responses["device_type"]

                c_id = insert_into_customers_table(cust_name,cust_nickname,cust_birthday,cust_phone,user_id,is_daily_horoscope,cust_zodiac_eng,device_id,device_type)
                
                #c_id = insert_into_customers_table(cust_name,cust_nickname,cust_birthday,cust_phone,user_id,is_daily_horoscope,cust_zodiac_eng)
       
                cust_responses["customer_id"] = c_id 
           
           
                STATE = "ASK_EMAIL"
                #STATE = "IS_TIME_FOR_MORE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "IS_TIME_FOR_MORE":
            out_msg_1, out_msg_2, option_list = is_time_for_more_fun()
            STATE = "IS_TIME_FOR_MORE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
 
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "is_time_for_more_1"
            }
            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list,
                "message_type": "none",
                "qid": "is_time_for_more_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "IS_TIME_FOR_MORE_ASKED":
            print("inside is time for more asked")
            is_time_for_more_menu_int = inp_msg
            is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
            if is_time_for_more_status == 1:
                cust_responses["is_time_for_more"] = is_time_for_more_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                if is_time_for_more_response == "yes":
                    is_time_for_more_response_jap = "はい"
                else:
                    is_time_for_more_response_jap = "いいえ"
                    
                out_dict = {"type" : "text", "status":"success", "answer": is_time_for_more_response_jap, "message_type": "none","qid": "is_time_for_more"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_time_for_more_response == "yes":
                    STATE = "ASK_TYPE_OF_SALON"
                
                elif is_time_for_more_response == "no":
                    STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json
        
        if STATE == "IS_TIME_FOR_MORE_2":
            out_msg_1,out_msg_2,option_list = is_time_for_more_2_fun()
            
            STATE = "IS_TIME_FOR_MORE_ASKED_2"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "is_time_for_more_2"
            }
            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "is_time_for_more_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
       

        if STATE == "IS_TIME_FOR_MORE_ASKED_2":

            is_time_for_more_menu_int = inp_msg
            is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
            
            if is_time_for_more_status == 1:
                cust_responses["is_time_for_more"] = is_time_for_more_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                if is_time_for_more_response == "yes":
                    is_time_for_more_response_jap = "はい"
                else:
                    is_time_for_more_response_jap = "いいえ"
                    
                out_dict = {
                    "type" : "text", 
                    "status":"success", 
                    "answer": is_time_for_more_response_jap, 
                    "message_type": "none",
                    "qid": "is_time_for_more_2"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"

                if is_time_for_more_response == "yes":
                    STATE = "ASK_COLOR"
                elif is_time_for_more_response == "no":
                    cust_responses["good_bye_msg"] = "ありがとうございます"
                    #STATE = "GOOD_BYE_FOR_NOW"
                    STATE = "NEW_WELCOME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_COLOR":
            #out_msg, option_list = ask_color(cust_responses)
            out_msg_1,out_msg_2, option_list = ask_color(cust_responses)
            STATE = "COLOR_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {
                "type" : "text", 
                "question": out_msg_1,
                "message_type": "none",
                "qid": "ask_color_1"
            }
            return_list_of_dicts.append(out_dict)
            
            
            out_dict = {
                "type" : "option", 
                "question": out_msg_2,
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_color"
            }

            return_list_of_dicts.append(out_dict)

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            #time.sleep(2) 
            return out_json

        if STATE == "COLOR_ASKED":
            cust_color = inp_msg
            
            color_status,color_response,color_idea,out_msg = check_color(cust_color)
            if color_status == 1:
                print("Inside ColorStatus 1")
                color_idea = color_idea
                cust_responses["color"] = color_response
                cust_responses["color_idea"] = color_idea
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": color_response, "message_type": "none","qid": "ask_color"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_TYPE_OF_SALON"
                STATE = "ASK_HOBBIES"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_HOBBIES":
            color_idea = cust_responses["color_idea"]
            #out_msg = ask_hobbies_fun(color_idea)
            out_msg_1,out_msg_2 = ask_hobbies_fun(color_idea)
            STATE = "HOBBIES_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            #out_dict = {"type" : "input", "question": out_msg,"message_type": "none","qid": "ask_hobbies"}
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1,
                "message_type": "none",
                "qid": "ask_hobbies_1"
            }
            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "input", 
                "question": out_msg_2,
                "message_type": "none",
                "qid": "ask_hobbies_2"
            }
            return_list_of_dicts.append(out_dict)
 
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "HOBBIES_ASKED":
            cust_hobbies = inp_msg
            
            hobby_status,hobby_idea,out_msg = check_hobby(cust_hobbies)
            
            if hobby_status == 1:
                cust_responses["hobby"] = cust_hobbies 
                #cust_responses["hobby_idea"] = hobby_idea

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_hobbies, "message_type": "none","qid": "ask_hobbies"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                STATE = "GOOD_BYE_FOR_NOW"
                out_msg = hobby_idea +"\nすべての情報をありがとう。"
                cust_responses["good_bye_msg"] = out_msg
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json
        
        if STATE == "GOOD_BYE_FOR_NOW":
            if "good_bye_msg" in cust_responses:
                out_msg =  cust_responses["good_bye_msg"]
            else:
                out_msg = ""

            out_msg = out_msg + "\nまたお話しましょう。\nさようなら。"

            if "booked_just_now" in cust_responses:
                if cust_responses["booked_just_now"] == 1:
                    rsv_id = cust_responses["rsv_id"]
                    return_dict["rid"] = str(rsv_id)
                cust_responses["booked_just_now"] = 0  




            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "text", "question": out_msg, "qid": "goodbye_bye_for_now"}
            return_list_of_dicts.append(out_dict)
            
            STATE = "NEW_WELCOME"

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json


        if STATE == "NEW_WELCOME":
            out_msg_1,out_msg_2,option_list = new_welcome_fun(cust_responses)
            STATE = "NEW_WELCOME_ASKED"
            
            return_dict["rid"] = ""

            if "booked_just_now" in cust_responses:
                if cust_responses["booked_just_now"] == 1:
                    rsv_id = cust_responses["rsv_id"]
                    return_dict["rid"] = str(rsv_id)
                cust_responses["booked_just_now"] = 0  
            
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "new_welcome_1"
            }
            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "new_welcome_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
       
        
        if STATE == "NEW_WELCOME_ASKED":
            new_welcome_menu_int = inp_msg
            new_welcome_status,new_welcome_response = check_new_welcome(new_welcome_menu_int,cust_responses)
            
            if new_welcome_response == "new_reservation":
                new_welcome_response_jap = "新しい予約"
                STATE = "ASK_DATE"

            if new_welcome_response == "cancel_reservation":
                new_welcome_response_jap = "予約をキャンセルする"
                STATE = "CANCEL_RESERVATION"
            
            if new_welcome_response == "change_reservation":
                new_welcome_response_jap = "予約変更"
                STATE = "CHANGE_RESERVATION"

            if new_welcome_response == "what_do_you_know":
                new_welcome_response_jap = "登録されている情報が知りたい"
                STATE = "GOOD_BYE_FOR_NOW"
            
            if new_welcome_response == "chat_more":
                new_welcome_response_jap = "もっとお互いを知るためにチャットがしたいだけ"
                STATE = "CHAT_MORE"

            if new_welcome_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": new_welcome_response_jap, "message_type": "none","qid": "new_welcome"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "CHAT_MORE":
            out_msg_1,out_msg_2,option_list = chat_more_fun()
            STATE = "CHAT_MORE_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "chat_more_1"
            }
            return_list_of_dicts.append(out_dict)
            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "chat_more_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json
       
        if STATE == "CHAT_MORE_ASKED":
            
            chat_more_menu_int = inp_msg
            chat_more_status,chat_more_response,is_working = check_chat_more(chat_more_menu_int)

            if is_working == 0:
                cust_responses["is_working"] = "no"

            if is_working == 1:
                cust_responses["is_working"] = "yes"

            if chat_more_status == 1:
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": chat_more_response, "message_type": "none","qid": "chat_more"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_FREE_DAYS"
                STATE = "ASK_FREE_TIME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_FREE_DAYS":
            #out_msg_1,out_msg_2,option_list = ask_free_days_fun(cust_responses)
            out_msg,option_list = ask_free_days_fun(cust_responses)
            
            STATE = "FREE_DAYS_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
           
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_free_days_2"
            }
            return_list_of_dicts.append(out_dict)


            """ 
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "ask_free_days_1"
            }
            return_list_of_dicts.append(out_dict)


            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_free_days_2"
            }
            return_list_of_dicts.append(out_dict)
            """  
                      
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "FREE_DAYS_ASKED":
            free_days_menu_int = inp_msg
            free_days_status,free_days_response = check_free_days(free_days_menu_int)
            

            if free_days_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": free_days_response, "message_type": "none","qid": "ask_free_days"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_FREE_TIME"
                STATE = "ASK_OFTEN_SERVICE"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_FREE_TIME":
            out_msg, option_list = ask_free_time_fun()
            
            STATE = "FREE_TIME_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_free_time"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "FREE_TIME_ASKED":

            free_time_menu_int = inp_msg
            free_time_status,free_time_response = check_free_time(free_time_menu_int)

            if free_time_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": free_time_response, "message_type": "none","qid": "ask_free_time"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                #STATE = "ASK_OFTEN_SERVICE"

                if cust_responses["is_working"] == "yes":
                    STATE = "ASK_WORK_ADDRESS"
                else:
                    #cust_responses["good_bye_msg"] = "ありがとうございます"
                    #STATE = "GOOD_BYE_FOR_NOW"
                    STATE = "NEW_WELCOME"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_OFTEN_SERVICE":
            out_msg, option_list = ask_often_service_fun()
            
            STATE = "OFTEN_SERVICE_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "multiple_choice",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_often_service"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "OFTEN_SERVICE_ASKED":
            often_service_csl = inp_msg
            often_service_list = often_service_csl.split(",")

            often_service_arr = [0,0,0,0,0]
            for service in often_service_list:
                service_ind = int(service) - 1
                often_service_arr[service_ind] = 1
            
            cust_responses["often_service_arr"] = often_service_arr
                
            
            often_service_status, often_service_long_list = check_often_service(often_service_list)
            often_service_string = "\n".join(often_service_long_list)
            
            if often_service_status == 1:
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": often_service_string, "message_type": "none","qid": "ask_often_service"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                STATE,cust_responses = find_often_service_state(cust_responses)
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_HAIR_FREQUENCY":
            out_msg, option_list = ask_hair_frequency_fun()
            
            STATE = "HAIR_FREQUENCY_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_hair_frequency"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "HAIR_FREQUENCY_ASKED":
            hair_frequency_menu_int = inp_msg
            hair_frequency_status,hair_frequency_response = check_hair_frequency(hair_frequency_menu_int)

            if hair_frequency_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": hair_frequency_response, "message_type": "none","qid": "ask_hair_frequency"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE,cust_responses = find_often_service_state(cust_responses)

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_NAILS_FREQUENCY":
            out_msg, option_list = ask_nails_frequency_fun()
            
            STATE = "NAILS_FREQUENCY_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_nails_frequency"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "NAILS_FREQUENCY_ASKED":
            nails_frequency_menu_int = inp_msg
            nails_frequency_status,nails_frequency_response = check_nails_frequency(nails_frequency_menu_int)

            if nails_frequency_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": nails_frequency_response, "message_type": "none","qid": "ask_nails_frequency"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE,cust_responses = find_often_service_state(cust_responses)

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_EYELASH_FREQUENCY":
            out_msg, option_list = ask_eyelash_frequency_fun()
            
            STATE = "EYELASH_FREQUENCY_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_eyelash_frequency"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "EYELASH_FREQUENCY_ASKED":
            eyelash_frequency_menu_int = inp_msg
            eyelash_frequency_status,eyelash_frequency_response = check_eyelash_frequency(eyelash_frequency_menu_int)

            if eyelash_frequency_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": eyelash_frequency_response, "message_type": "none","qid": "ask_eyelash_frequency"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE,cust_responses = find_often_service_state(cust_responses)

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json



        if STATE == "ASK_RELAXATION_FREQUENCY":
            out_msg, option_list = ask_relaxation_frequency_fun()
            
            STATE = "RELAXATION_FREQUENCY_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_relaxation_frequency"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "RELAXATION_FREQUENCY_ASKED":
            relaxation_frequency_menu_int = inp_msg
            relaxation_frequency_status,relaxation_frequency_response = check_relaxation_frequency(relaxation_frequency_menu_int)

            if relaxation_frequency_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": relaxation_frequency_response, 
                    "message_type": "none",
                    "qid": "ask_relaxation_frequency"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE,cust_responses = find_often_service_state(cust_responses)
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_AESTHETIC_FREQUENCY":
            out_msg, option_list = ask_aesthetic_frequency_fun()
            
            STATE = "AESTHETIC_FREQUENCY_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_aesthetic_frequency"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "AESTHETIC_FREQUENCY_ASKED":
            aesthetic_frequency_menu_int = inp_msg
            aesthetic_frequency_status,aesthetic_frequency_response = check_aesthetic_frequency(aesthetic_frequency_menu_int)

            if aesthetic_frequency_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": aesthetic_frequency_response, 
                    "message_type": "none",
                    "qid": "ask_aesthetic_frequency"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE,cust_responses = find_often_service_state(cust_responses)
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_EMAIL":
            out_msg_1, out_msg_2 = ask_email_fun(cust_responses)  
            STATE = "EMAIL_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text",
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "ask_email_1"
            }

            return_list_of_dicts.append(out_dict)


            out_dict = {
                "type" : "input",
                "question": out_msg_2, 
                "message_type": "none",
                "qid": "ask_email_2"
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "EMAIL_ASKED":
            cust_email = inp_msg
            cust_responses["email"] = cust_email
            email_status = 1

            if email_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": cust_email, 
                    "message_type": "none",
                    "qid": "ask_email"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_HOME_ADDRESS"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_HOME_ADDRESS":
            out_msg_1,out_msg_2 = ask_home_address_fun(cust_responses)  
            
            STATE = "HOME_ADDRESS_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text",
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "ask_home_address_1"
            }

            return_list_of_dicts.append(out_dict)

            out_dict = {
                "type" : "input",
                "question": out_msg_2, 
                "message_type": "none",
                "qid": "ask_home_address_2",
            }

            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "HOME_ADDRESS_ASKED":
            cust_home_address = inp_msg
            cust_responses["home_address"] = cust_home_address
            email_status = 1

            if email_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": cust_home_address, 
                    "message_type": "none",
                    "qid": "ask_home_address"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "ASK_FREE_DAYS"
                #if cust_responses["is_working"] == "yes":
                #    STATE = "ASK_WORK_ADDRESS"
                #else:
                #    cust_responses["good_bye_msg"] = "ありがとうございます"
                #    STATE = "GOOD_BYE_FOR_NOW"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_WORK_ADDRESS":
            out_msg = ask_work_address_fun()  
            
            STATE = "WORK_ADDRESS_ASKED"
            
            return_dict["rid"] = ""
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "input",
                "question": out_msg, 
                "message_type": "none",
                "qid": "ask_work_address"
            }

            return_list_of_dicts.append(out_dict)

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            
            return out_json

        if STATE == "WORK_ADDRESS_ASKED":
            cust_work_address = inp_msg
            cust_responses["work_address"] = cust_work_address
            email_status = 1

            if email_status == 1:

                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": cust_work_address, 
                    "message_type": "none",
                    "qid": "ask_work_address"
                }
                
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                cust_responses["good_bye_msg"] = "ありがとうございます"
                #STATE = "GOOD_BYE_FOR_NOW"
                STATE = "NEW_WELCOME"

                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "CANCEL_RESERVATION":
            user_id = cust_responses["user_id"]
            cust_id = cust_responses["customer_id"] 

            print("cust_id")
            print(cust_id)

            out_msg,option_list,exist_rsv_dict = cancel_change_reservation_fun(cust_responses,user_id,"cancel")

            STATE = "CANCEL_RESERVATION_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list,
                "message_type": "none",
                "qid": "cancel_ask_id"
            }
            
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "CANCEL_RESERVATION_ASKED":
            cancel_menu_int = inp_msg

            cust_id = cust_responses["customer_id"]
            is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id)

            for key in exist_rsv_dict:
                #if key == int(cancel_menu_int):
                if key == cancel_menu_int:
                    selected_option = key

            cancel_rsv_id = exist_rsv_dict[selected_option]["r_id"] 

            rsv_status = delete_from_reservations_table(cancel_rsv_id)
            
            change_serv_id = exist_rsv_dict[key]["serv_id"]
            change_emp_id = exist_rsv_dict[key]["emp_id"]
            change_start_date = exist_rsv_dict[key]["start_date"]
            change_start_date_jap = convert_date_from_yyyymmdd_to_jap(change_start_date) 
            change_start_time = exist_rsv_dict[key]["start_time"]

            select_sql1 = """select name from services where id = %s"""
            select_tuple1 = (change_serv_id,)
            
            mydb,mycursor = create_sql_conn()
            mycursor.execute(select_sql1,select_tuple1)
            myresult_list = mycursor.fetchall()
            mycursor.close()
            mydb.close()


            tuple0 = myresult_list[0]
            change_serv_name1 = tuple0[0]
            change_serv_name = change_serv_name1.decode() ; change_serv_name

            select_sql2 = """select name from employees where id = %s"""
            select_tuple2 = (change_emp_id,)
            
            
            mydb,mycursor = create_sql_conn()
            mycursor.execute(select_sql2,select_tuple2)
            myresult_list = mycursor.fetchall()
            mycursor.close()
            mydb.close()


            tuple0 = myresult_list[0]
            change_emp_name1 = tuple0[0]
            print("change_emp_name1")
            print(change_emp_name1)
            print(type(change_emp_name1))

            change_emp_name = change_emp_name1.decode() ; change_emp_name

            print("change_emp_name")
            print(change_emp_name)
            print(type(change_emp_name))
            print(type(change_serv_name))

            #answer = change_serv_name + " と " + change_emp_name  + " に " + change_start_date +  " で " + change_start_time  
            answer = change_serv_name + " と " + change_emp_name  + " に " + change_start_date_jap +  " で " + change_start_time  
            #value = serv_name + " と " + emp_name + " に " + start_date + " で " + start_time 
            if rsv_status == 1:
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": answer, "message_type": "none","qid": "cancel_ask_id"}

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                cust_responses["good_bye_msg"] = "あなたの予約はキャンセルされました。"

                
                STATE = "GOOD_BYE_FOR_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_msg = "そのような予約は見つかりませんでした。 有効な予約番号を入力してください。"
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "CHANGE_RESERVATION":
            cust_id = cust_responses["customer_id"] 
            user_id = cust_responses["user_id"]
            out_msg,option_list,exist_rsv_dict = cancel_change_reservation_fun(cust_responses,user_id,"change")
            STATE = "CHANGE_RESERVATION_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list,
                "message_type": "none",
                "qid": "change_ask_id"
            }
            
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
       
       
        if STATE == "CHANGE_RESERVATION_ASKED":
            change_menu_int = inp_msg

            cust_id = cust_responses["customer_id"]
            is_rsv, exist_rsv_dict = get_reservations_for_customer(cust_id)

            for key in exist_rsv_dict:
                #if key == int(cancel_menu_int):
                if key == change_menu_int:
                    selected_option = key

            change_rsv_id = exist_rsv_dict[selected_option]["r_id"] 
            
            rsv_status = delete_from_reservations_table(change_rsv_id)
            
            change_serv_id = exist_rsv_dict[key]["serv_id"]
            change_emp_id = exist_rsv_dict[key]["emp_id"]
            change_start_date = exist_rsv_dict[key]["start_date"]
            change_start_date_jap = convert_date_from_yyyymmdd_to_jap(change_start_date) 
            change_start_time = exist_rsv_dict[key]["start_time"]

            select_sql1 = """select name from services where id = %s"""
            select_tuple1 = (change_serv_id,)
            
            
            mydb,mycursor = create_sql_conn()
            mycursor.execute(select_sql1,select_tuple1)
            myresult_list = mycursor.fetchall()
            mycursor.close()
            mydb.close()


            tuple0 = myresult_list[0]
            change_serv_name1 = tuple0[0]
            change_serv_name = change_serv_name1.decode() ; change_serv_name

            select_sql2 = """select name from employees where id = %s"""
            select_tuple2 = (change_emp_id,)
            
            mydb,mycursor = create_sql_conn()
            mycursor.execute(select_sql2,select_tuple2)
            myresult_list = mycursor.fetchall()
            mycursor.close()
            mydb.close()


            tuple0 = myresult_list[0]
            change_emp_name1 = tuple0[0]
            change_emp_name = change_emp_name1.decode() ; change_emp_name
            
            #answer = change_serv_name + " と " + change_emp_name  + " に " + change_start_date +  " で " + change_start_time
            answer = change_serv_name + " と " + change_emp_name  + " に " + change_start_date_jap +  " で " + change_start_time
            #answer = change_serv_name + " with " + change_emp_name  + " on " + change_start_date +  " at " + change_start_time  
            
            if rsv_status == 1:
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": answer, "message_type": "none","qid": "cancel_ask_id"}

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "ASK_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_msg = "そのような予約は見つかりませんでした。 有効な予約番号を入力してください。"
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_TYPE_OF_SALON":
            out_msg_1,out_msg_2,option_list = ask_type_of_salon()
            STATE = "TYPE_OF_SALON_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "ask_type_of_salon_1"
            }
            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "multiple_choice", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_type_of_salon_2"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "TYPE_OF_SALON_ASKED":
            cust_type_of_salon_csl = inp_msg
            cust_type_of_salon_list = cust_type_of_salon_csl.split(",")
            
            cust_type_of_salon_status,type_of_salon_list,out_msg = check_cust_type_of_salon(cust_type_of_salon_list)
            
            cust_type_of_salon = "\n".join(type_of_salon_list)
            
            if cust_type_of_salon_status == 1:
                cust_responses["type_of_salon"] = cust_type_of_salon
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": cust_type_of_salon, "message_type": "none","qid": "ask_type_of_salon"}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "IS_RESERVATION_NOW":
            #out_msg,option_list = is_reservation_now_fun()
            out_msg_1,out_msg_2,option_list = is_reservation_now_fun()
            STATE = "IS_RESERVATION_NOW_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            #out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_reservation_now"}
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none",
                "qid": "is_res_now_1"
            }
            
            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "option", 
                "question": out_msg_2, 
                "option_list": option_list, 
                "message_type": "none", 
                "qid": "is_res_now_2"
            }
            
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json


        if STATE == "IS_RESERVATION_NOW_ASKED":
            is_reservation_now_menu_int = inp_msg
            is_reservation_now_status,is_reservation_now_response,out_msg = check_is_reservation_now(is_reservation_now_menu_int)
            if is_reservation_now_status == 1:
                cust_responses["is_reservation_now"] = is_reservation_now_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if is_reservation_now_response == "yes":
                    is_reservation_now_response_jap = "はい"
                else:
                    is_reservation_now_response_jap = "いいえ"
              
                out_dict = {
                    "type" : "text", 
                    "answer": is_reservation_now_response_jap, 
                    "message_type": "none",
                    "qid": "is_reservation_now"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"

                if is_reservation_now_response == "yes":
                    STATE = "ASK_DATE"
                elif is_reservation_now_response == "no":
                    STATE = "IS_TIME_FOR_MORE_ASKED_2"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_DATE":
            #out_msg = ask_date()
            out_msg_1, out_msg_2 = ask_date()

            STATE = "DATE_ASKED"
            
            out_dict = {
                "type" : "text", 
                "question": out_msg_1, 
                "message_type": "none", 
                "qid": "ask_date_1"
            }
            return_list_of_dicts.append(out_dict)
            
            out_dict = {
                "type" : "input", 
                "question": out_msg_2, 
                "message_type": "rsv_date", 
                "place_holder": "06月21日",
                "qid": "ask_date_2"
            }
            return_list_of_dicts.append(out_dict)
            
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json


        if STATE == "DATE_ASKED":
            print("Inside Date Asked")

            cust_date_inp = inp_msg
            cust_date_inp_plus_day_sym = cust_date_inp + "日"
            jap = 0
            
            """ 
            try:
                check_cust_date = datetime.datetime.strptime(cust_date_inp, '%Y-%m-%d')
            except:
                cust_date_status,cust_date_obj,out_msg = get_date_in_ddmmyyyy_format(cust_date_inp)
                cust_date_str = str(cust_date_obj)
                jap = 1
            """
            
            jap = 1
            cust_date_status,cust_date_obj,out_msg = get_date_in_ddmmyyyy_format(cust_date_inp)
            cust_date_str = str(cust_date_obj)

           
            """
            if jap != 1:
                cust_date_obj,cust_date_status,out_msg = check_date(cust_date_inp)
                cust_date_str = str(cust_date_obj)
            """
            
            if cust_date_status == 1:
                cust_responses["date"] = cust_date_str
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text",
                    "answer": cust_date_inp_plus_day_sym, 
                    "message_type": "none",
                    "qid": "ask_date"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_SERVICE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_SERVICE":
            user_id = cust_responses["user_id"]
            out_msg,option_list,service_dict = ask_service_fun(user_id)
            STATE = "SERVICE_ASKED"
            cust_responses["service_dict"] = service_dict
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_service"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json


        if STATE == "SERVICE_ASKED":
            user_id = cust_responses["user_id"]
            cust_service_menu_int = inp_msg
            serv_status,serv_id,serv_name,out_msg = check_service(cust_service_menu_int,cust_responses)
            
            if serv_status == 1:
                cust_responses["service"] = serv_id
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {
                    "type" : "text", 
                    "answer": serv_name, 
                    "id": serv_id, 
                    "message_type": "none",
                    "qid": "ask_service"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"
                
                sub_service_dict = get_sub_services(serv_id,user_id)
                cust_responses["sub_service_dict"] = sub_service_dict
                
                #super_service_dict = get_super_services(serv_id,user_id)
                #cust_responses["super_service_dict"] = super_service_dict
                
                STATE = "ASK_SUB_SERVICE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_SUPER_SERVICE":
            
            out_msg,option_list = ask_sub_service_fun(cust_responses)

            STATE = "SUPER_SERVICE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "ask_sub_service"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "SUPER_SERVICE_ASKED":
            print("sub service asked") 
            #print(cust_responses)
            
            ss_menu_int = inp_msg
            ss_status,ss_id,ss_name,ss_dur,cust_price,out_msg = check_sub_service(ss_menu_int,cust_responses)
            #print("\n\n\n\n\n CHECK SUB SERVICE ENDS \n\n\n\n\n\n\n\n") 
            
            print("ss_dur")
            print(ss_dur)
            
            if ss_status == 1:
                
                cust_responses["sub_service"] = ss_id
                cust_responses["duration"] = ss_dur
                cust_responses["price"] = cust_price
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text",
                    "answer": ss_name,
                    "id": ss_id,
                    "message_type": "none",
                    "qid": "ask_sub_service"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"
                
                print("cust_responses[service]")
                print(cust_responses["service"])
                
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                #return "nothing"
                duration_in_hours = int(int(ss_dur) / 60)
                #duration = 2
                print("ss_dur,duration_in_hours")
                print(ss_dur,duration_in_hours)
                #return "nothing"

                cust_date_str = cust_responses["date"]
                cust_date_obj = datetime.datetime.strptime(cust_date_str, '%Y-%m-%d %H:%M:%S')
                
                avail_emp_dict = check_new_availability(cust_date_obj,relevant_employee_list,duration_in_hours,user_id)
                #return "nothing" 
                emp_name_dict = find_employee_name(user_id)

                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")

                print("avail_emp_dict")
                print(avail_emp_dict)
                
                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")
                
                
                cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(avail_emp_dict,emp_name_dict)
                #return "nothing" 
                cust_responses["cust_avail_msg"] = cust_avail_msg 
                cust_responses["cust_avail_display_options"] = cust_avail_display_options 
                
                STATE = "SHOW_AVAIL_OPTIONS"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_SUB_SERVICE":
            
            out_msg,option_list = ask_sub_service_fun(cust_responses)

            STATE = "SUB_SERVICE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option",
                "question": out_msg,
                "option_list": option_list,
                "message_type": "none",
                "qid": "ask_sub_service"
            }
            return_list_of_dicts.append(out_dict)
            
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "SUB_SERVICE_ASKED":
            user_id = cust_responses["user_id"]
            print("user_id")
            print(user_id)

            print("sub service asked") 
            #print(cust_responses)
            
            ss_menu_int = inp_msg
            ss_status,ss_id,ss_name,ss_dur,cust_price,out_msg = check_sub_service(ss_menu_int,cust_responses)
            #print("\n\n\n\n\n CHECK SUB SERVICE ENDS \n\n\n\n\n\n\n\n") 
            
            print("ss_dur")
            print(ss_dur)
            
            if ss_status == 1:
                
                cust_responses["sub_service"] = ss_id
                cust_responses["duration"] = ss_dur
                cust_responses["price"] = cust_price
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {
                    "type" : "text", 
                    "answer": ss_name,
                    "id":ss_id, 
                    "message_type": "none",
                    "qid": "ask_sub_service"
                }
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                print("cust_responses[service]")
                print(cust_responses["service"])
                
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                #return "nothing"
                duration_in_hours = int(int(ss_dur) / 60)
                #duration = 2
                print("ss_dur,duration_in_hours")
                print(ss_dur,duration_in_hours)
                #return "nothing"

                cust_date_str = cust_responses["date"]
                cust_date_obj = datetime.datetime.strptime(cust_date_str, '%Y-%m-%d %H:%M:%S')
                
                avail_emp_dict = check_new_availability(cust_date_obj,relevant_employee_list,duration_in_hours,user_id)
                #return "nothing" 
                emp_name_dict = find_employee_name(user_id)

                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")

                print("avail_emp_dict")
                print(avail_emp_dict)
                
                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")
                
                
                cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(avail_emp_dict,emp_name_dict)
                #return "nothing" 
                cust_responses["cust_avail_msg"] = cust_avail_msg 
                cust_responses["cust_avail_display_options"] = cust_avail_display_options 
                
                STATE = "SHOW_AVAIL_OPTIONS"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "SHOW_AVAIL_OPTIONS":
            print("Inside Show Avail Options")

            cust_avail_msg = cust_responses["cust_avail_msg"]
            print("cust_responses")
            print(cust_responses)
            
            out_msg = cust_avail_msg
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": cust_avail_option_list, 
                "message_type": "none",
                "qid": "show_avail_options"
            }
            return_list_of_dicts.append(out_dict)
            
            STATE = "AVAIL_OPTIONS_SHOWN"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "AVAIL_OPTIONS_SHOWN":
            cust_avail_options_menu_int = inp_msg
            cust_avail_display_options = cust_responses["cust_avail_display_options"]
            print("cust_avail_display_options")
            print(cust_avail_display_options)
            cust_avail_options_status, cust_selected_option, out_msg = check_avail_options(cust_avail_options_menu_int,cust_avail_display_options)
            
            if cust_avail_options_status == 1:
                print("cust_selected_option")
                print(cust_selected_option)
                #return "nothing"
                cust_responses["avail_options"] = cust_selected_option
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                if cust_selected_option[1] != "none":
                    sel_emp = cust_selected_option[1]
                    slot = cust_selected_option[2]
                    select_sql = """select name from employees where id = %s"""
                    select_tuple = (sel_emp,)
                    
                    mydb,mycursor = create_sql_conn()
                    mycursor.execute(select_sql,select_tuple)
                    myresult_list = mycursor.fetchall()
                    mycursor.close()
                    mydb.close()


                    a1 = myresult_list[0]
                    a2 = a1[0]
                    sel_emp_name = a2.decode() ; sel_emp_name  
                    
                    sel_time = slot_list[slot]

                    long_option = sel_emp_name + " で " + str(sel_time) 
                else:
                    long_option = "上記の時間のどれも私には合いません。"

                out_dict = {
                    "type" : "text",
                    "answer": long_option, 
                    "message_type": "none",
                    "qid": "show_avail_options"
                }

                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_selected_option[1] == "none":
                    STATE = "ASK_ALT_TIME"
                    #STATE = "ASK_IF_ALT_SALON"
                else: 
                    STATE = "IS_CONFIRM"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

           
        if STATE == "ASK_IF_ALT_SALON":
            out_msg, option_list = ask_if_alt_salon_fun()
            #out_msg, option_list = is_confirm_fun()
            STATE = "IS_CONFIRM_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list, "message_type": "none","qid": "is_confirm"}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "IF_ALT_SALON_ASKED":
            print("inside is confirm asked")
            cust_is_confirm_menu_int = inp_msg
            cust_is_confirm_status, cust_is_confirm_response, out_msg = check_is_confirm(cust_is_confirm_menu_int)
            
            if cust_is_confirm_status == 1:
                cust_responses["is_confirm"] = cust_is_confirm_response
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if cust_is_confirm_response == "yes":
                    cust_is_confirm_response_jap = "はい"

                if cust_is_confirm_response == "no":
                    cust_is_confirm_response_jap = "他の日付を確認する"

                if cust_is_confirm_response == "stop":
                    cust_is_confirm_response_jap = "今、予約をとるのをやめる"
                #else:
                #    cust_is_confirm_response_jap = "いいえ"
              
                
                out_dict = {
                    "type" : "text", 
                    "answer": cust_is_confirm_response_jap, 
                    "message_type": "none",
                    "qid": "is_confirm"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"

                if cust_is_confirm_response == "yes":
                    STATE = "ENTER_DB"
                if cust_is_confirm_response == "no":
                    STATE = "ASK_DATE"
                if cust_is_confirm_response == "stop":
                    STATE = "IS_TIME_FOR_MORE_2"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json


        if STATE == "ASK_ALT_TIME":
            out_msg = ask_alt_time_fun()
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "input", 
                "question": out_msg, 
                "place_holder": "19:00", 
                "message_type": "time"
            }
            return_list_of_dicts.append(out_dict)
            
            STATE = "ALT_TIME_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "ALT_TIME_ASKED":
            user_id = cust_responses["user_id"]

            print("inside alt time asked")
            cust_alt_time = inp_msg
            time_obj, time_status,out_msg = check_time(cust_alt_time) 
            if time_status == 1:

                cust_selected_option = inp_msg
                cust_responses["cust_alt_time"] = cust_selected_option 
                today = datetime.datetime.now()

                next_seven_day_list = [today,]
                for i in range(1,15):
                    new= today + datetime.timedelta(days=i)
                    next_seven_day_list.append(new)
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                alt_avail_days = []

                for day in next_seven_day_list:
                    employee_schedule_dict = get_employee_schedule_for_date(day,relevant_employee_list)
                    start_time = cust_alt_time
                    time_duration_in_mins = int(cust_responses["duration"])
                    time_duration_in_hours = int(time_duration_in_mins/60)
                    emp_avail_dict = check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours)
                    
                    any_emp_avail_on_day = 0
                    
                    for emp in emp_avail_dict:
                        if len(emp_avail_dict[emp]) != 0:
                            any_emp_avail_on_day = 1

                    if any_emp_avail_on_day == 1:
                        day_format = day.strftime("%Y-%m-%d")
                        alt_avail_days.append(day_format)

                print("alt_avail_days")
                print(alt_avail_days)

                option_list = []
                serial = 1 

                for avail_day in alt_avail_days:
                    option = {"key": serial, "value": avail_day}
                    option_list.append(option)
                    serial += 1
                
                jap_option_list = []
                serial = 1 
                for avail_day in alt_avail_days:
                    x = avail_day[:4] + '年' + avail_day[5:]
                    y = x[:7] + '月' + x[8:]
                    z = y + "日"
                    option = {"key": serial, "value": z}
                    jap_option_list.append(option)
                    serial += 1


                cust_responses["alt_avail_days_list"] = alt_avail_days
                cust_responses["alt_avail_days"] = option_list 
                cust_responses["jap_option_list"] = jap_option_list 

                cust_responses["cust_alt_time"] = cust_selected_option
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {
                    "type" : "text",
                    "answer": cust_alt_time, 
                    "message_type": "none"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"

                STATE = "ASK_ALT_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ASK_ALT_DATE":
            out_msg,option_list = ask_alt_date_fun(cust_responses)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none"
            }
            return_list_of_dicts.append(out_dict)
            
            STATE = "ALT_DATE_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        
        if STATE == "ALT_DATE_ASKED":
            user_id = cust_responses["user_id"] 

            print("inside alt date asked")
            cust_alt_date = inp_msg
            days_list = cust_responses["alt_avail_days_list"]
            cust_alt_time = cust_responses["cust_alt_time"] 
            date_index = int(cust_alt_date) - 1
            selected_date = days_list[date_index]
            
            x = selected_date[:4] + '年' + selected_date[5:]
            y = x[:7] + '月' + x[8:]
            z = y + "日"
            selected_date_jap = z 

            print(selected_date) 
            date_obj = datetime.datetime.strptime(selected_date, "%Y-%m-%d")

            relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
            employee_schedule_dict = get_employee_schedule_for_date(date_obj,relevant_employee_list)
            
            print("\n\n----------------------\n\n")
            print("employee_schedule_dict")
            print(employee_schedule_dict)
            print("\n\n----------------------\n\n")

            start_time = cust_alt_time
            time_duration_in_mins = int(cust_responses["duration"])
            time_duration_in_hours = int(time_duration_in_mins/60)
            
            emp_avail_dict = check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours)

            print(emp_avail_dict)
            
            emp_name_dict = find_employee_name(user_id)
            
            cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(emp_avail_dict,emp_name_dict)

            cust_responses["date"] = str(date_obj)
            cust_responses["cust_avail_msg"] = cust_avail_msg 
            cust_responses["cust_avail_display_options"] = cust_avail_display_options 
            print(cust_avail_msg)
            print(cust_avail_display_options)
            print(cust_avail_option_list)

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {"type" : "text","answer": selected_date_jap, "message_type": "none"}
            return_list_of_dicts.append(out_dict)
            return_list_of_dicts[-2]["type"] = "text"

            STATE = "SHOW_AVAIL_OPTIONS"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))


        if STATE == "IS_CONFIRM":
            out_msg, option_list = is_confirm_fun()
            STATE = "IS_CONFIRM_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {
                "type" : "option", 
                "question": out_msg, 
                "option_list": option_list, 
                "message_type": "none",
                "qid": "is_confirm"
            }
            return_list_of_dicts.append(out_dict)

            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

        if STATE == "IS_CONFIRM_ASKED":
            print("inside is confirm asked")
            cust_is_confirm_menu_int = inp_msg
            cust_is_confirm_status, cust_is_confirm_response, out_msg = check_is_confirm(cust_is_confirm_menu_int)
            
            if cust_is_confirm_status == 1:
                cust_responses["is_confirm"] = cust_is_confirm_response
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                if cust_is_confirm_response == "yes":
                    cust_is_confirm_response_jap = "はい"

                if cust_is_confirm_response == "no":
                    cust_is_confirm_response_jap = "他の日付を確認する"

                if cust_is_confirm_response == "stop":
                    cust_is_confirm_response_jap = "今、予約をとるのをやめる"
                #else:
                #    cust_is_confirm_response_jap = "いいえ"
              
                
                out_dict = {
                    "type" : "text", 
                    "answer": cust_is_confirm_response_jap, 
                    "message_type": "none",
                    "qid": "is_confirm"
                }
                return_list_of_dicts.append(out_dict)
                
                return_list_of_dicts[-2]["type"] = "text"

                if cust_is_confirm_response == "yes":
                    STATE = "ENTER_DB"
                if cust_is_confirm_response == "no":
                    STATE = "ASK_DATE"
                if cust_is_confirm_response == "stop":
                    STATE = "IS_TIME_FOR_MORE_2"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                out_json = failure_msg_fun(return_dict,out_msg,return_list_of_dicts,ip,STATE,cust_responses)
                return out_json

        if STATE == "ENTER_DB":
            print ("inside enter db")
            user_id = cust_responses["user_id"]


            if "is_nickname" in cust_responses:
                if cust_responses["is_nickname"] == "no":
                    cust_responses["nickname"] = ""

            if "is_time_for_more" in cust_responses:
                if cust_responses["is_time_for_more"] == "no":
                    cust_responses["type_of_salon"] = ""

            if "is_reservation_now" in cust_responses:
                if cust_responses["is_reservation_now"] == "no":
                    cust_responses["date"] = ""
                    cust_responses["avail_options"] = [0,0,0]
                    ust_responses["service"] = 0

            
            cust_res_date = cust_responses["date"]
            cust_slot = cust_responses["avail_options"][2]
            cust_res_time = slot_list[cust_slot]
            cust_service_id = cust_responses["service"]
            cust_sub_service_id = cust_responses["sub_service"]
            cust_emp_id = cust_responses["avail_options"][1]
            cust_is_confirm = cust_responses["is_confirm"]
            cust_duration_in_mins = cust_responses["duration"]
            cust_price = cust_responses["price"]
           
           
            
            c_id = cust_responses["customer_id"] 
            
            i_u_id=int(user_id)
            i_c_id=c_id
            i_s_id=int(cust_service_id)
            i_ss_id=int(cust_sub_service_id)
            i_e_id=str(cust_emp_id)
            #i_s_date=str(cust_res_date)
            start_date=str(cust_res_date)
            #i_e_date=str(cust_res_date)
            end_date=str(cust_res_date)
           
            start_slot = int(cust_slot)
            start_time = slot_list[start_slot] 
            
            slots_needed = int(int(cust_duration_in_mins) / 30)
            next_slot = start_slot + slots_needed
            end_time = slot_list[next_slot]
            i_s_time=str(start_time)
            i_e_time=str(end_time)
            start_date_wo_0s = start_date[:-9] 
            end_date_wo_0s = end_date[:-9] 
            i_s_date=str(start_date_wo_0s)
            i_e_date=str(end_date_wo_0s)
            i_total= cust_price
            rsv_num,rsv_id = insert_into_reservations_table(i_u_id,i_c_id,i_s_id,i_ss_id,i_e_id,i_s_date,i_e_date,i_s_time,i_e_time,i_total)

            ##### CODE TO SEND PUSH NOTIFICATION ##############
            URL = "https://api.jtsboard.com/web_servicesv42/push_notification_mirai"
            r_id = rsv_id
            PARAMS = {'reservation_id':r_id}
            r = requests.get(url = URL, params = PARAMS)
            ####################################################
            cust_responses["rsv_id"] = rsv_id

            #if "color" not in cust_responses:
            #    out_msg,option_list = confirmed_fun(rsv_num)
            #
            #    return_dict["status"] = "success"
            #    return_dict["error_msg"] = ""
            #    return_dict["chat"] = return_list_of_dicts
            #    return_dict["rid"] = str(rsv_id)
            #    out_dict = {"type" : "option", "question": out_msg,"message_type": "none","option_list":option_list,"qid": "confirmed_ask_if_more"}
            #    return_list_of_dicts.append(out_dict)
            #    STATE = "IS_TIME_FOR_MORE_ASKED_2" 
            #    update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            #    
            #    out_json = json.dumps(return_dict,ensure_ascii= False)
            #    return out_json
            #else:
            #    out_msg = confirmed_without_more_fun(rsv_num)
            #    cust_responses["good_bye_msg"] = out_msg
            #    cust_responses["booked_just_now"] = 1
            #    STATE = "GOOD_BYE_FOR_NOW"
            #    update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
    
            return_dict["rid"] = str(rsv_id)
            cust_responses["booked_just_now"] = 1
            STATE = "NEW_WELCOME" 
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
    return "Cheese"

########################################################################################
########## CHAT BOT API ENDS HERE
########################################################################################


if __name__ == '__main__':
    app.run(debug=True)                                                         # For Dev Server  
    #context = ('fullchain1.pem','privkey1.pem')                                # For QA and Live Server
    #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5001)            # For QA Server 
    #app.run(debug=True,host='0.0.0.0',ssl_context=context,port=5000)            # For Live Server


