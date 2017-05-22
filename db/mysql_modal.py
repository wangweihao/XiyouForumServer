# -*- coding: utf-8 -*-
# Created by wwh on 2017/5/21


from datetime import datetime
from server import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True)
    account = db.Column(db.String(64), unique=True, nullable=False)
    passwd = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    head = db.Column(db.String(128))
    sex = db.Column(db.Boolean)
    school = db.Column(db.String(64))
    major = db.Column(db.String(64))
    trade = db.Column(db.String(64))
    blog = db.Column(db.String(64))
    email = db.Column(db.String(64))


class UserAchieve(db.Model):
    __tablename__ = 'user_achieve'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    agree_count = db.Column(db.Integer, default=0)
    thanked_count = db.Column(db.Integer, default=0)
    favorited_count = db.Column(db.Integer, default=0)
    follower_count = db.Column(db.Integer, default=0)
    following_count = db.Column(db.Integer, default=0)
    answer_count = db.Column(db.Integer, default=0)


class Question(db.Model):
    __tablename__ = 'user_question'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)
    agree_count = db.Column(db.Integer, default=0)
    answer_count = db.Column(db.Integer, default=0)
    scan_count = db.Column(db.Integer, default=0)
    favorited_count = db.Column(db.Integer, default=0)
    follower_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<title %r>' % self.title


class QuestionCollect(db.Model):
    __tablename__ = 'question_collect'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger)
    ques_id = db.Column(db.BigInteger)


class QuestionFollow(db.Model):
    __tablename__ = 'question_follow'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger)
    ques_id = db.Column(db.BigInteger)


class Answer(db.Model):
    __tablename__ = 'question_answer'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger)
    ques_id = db.Column(db.BigInteger)
    create_time = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text)
    agree_count = db.Column(db.Integer, default=0)
    oppose_count = db.Column(db.Integer, default=0)


class Article(db.Model):
    __tablename__ = 'user_article'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)
    agree_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<title %r>' % self.title


class Commit(db.Model):
    __tablename__ = 'article_commit'
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    arti_id = db.Column(db.BigInteger, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.Text, nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.BigInteger, primary_key=True)
    content = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<category %r>' % self.content


class QuestionCategory(db.Model):
    __tablename__ = 'question_category_rela'
    id = db.Column(db.BigInteger, primary_key=True)
    ques_id = db.Column(db.BigInteger, nullable=False)
    cate_id = db.Column(db.BigInteger, nullable=False)


class ArticleCategory(db.Model):
    __tablename__ = 'article_category_rela'
    id = db.Column(db.BigInteger, primary_key=True)
    arti_id = db.Column(db.BigInteger, nullable=False)
    cate_id = db.Column(db.BigInteger, nullable=False)


# db.create_all()