from flask import Blueprint
from flask import Flask, request, jsonify
from . import reply_main

big_reply = reply_main.big_reply

blue_main_menu = Blueprint("main_menu", __name__, url_prefix="/main_menu")

@blue_main_menu.route("/")
def main_menu_check():
    return "main_menu"

@blue_main_menu.route("/main", methods=['GET', 'POST'])
def main_menu_1():
    body = request.get_json()
    
    res = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "basicCard": {
          "title": "메인메뉴",
          "description": "원하는 메뉴를 선택해주세요.",
          "thumbnail": {
            "imageUrl": ""
          },
          "profile": {
            "imageUrl": "",
            "nickname": "메인메뉴"
          },
          "buttons": [
            {
              "label": "주택복지 목록 보기",
              "action": "block",
              "blockId": big_reply['주택복지']
            },
            {
              "label": "공공주택 목록 보기",
              "action": "block",
              "blockId": big_reply['공공주택'],
              "extra": {"page_type" : "before"}
            }
          ]
        }
      }
    ]
  }
}
    return jsonify(res)