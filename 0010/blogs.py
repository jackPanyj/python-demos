#! /usr/bin/en python
# coding:utf-8

import requests
import pymysql
'''
    从我的learning仓库中抓取所有的issue存到本地mysql中
'''
def get_issues():
    base_url = 'https://api.github.com'
    owner = 'jackpanyj'
    repo = 'learning-note'
    url = f'{base_url}/repos/{owner}/{repo}/issues?per_page=65535'
    res = requests.get(url) # 请求接口拿到数据
    return res.json()

def save_to_mysql():
    issues = get_issues()
    
    db = pymysql.connect(host='localhost', user='root', password='', db='music', charset='utf8')
    sql = '''
            INSERT INTO `blogs` (`title`, `content`, `created_at`, `number`, `comments_url`, `updated_at`, `url`)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
          '''
    try:
        with db.cursor() as cursor:
            cursor.execute('DELETE FROM `blogs`')
            for issue in issues:
                cursor.execute(sql, (issue['title'], issue['body'], issue['created_at'], issue['number'], issue['comments_url'], issue['updated_at'], issue['url']))
            db.commit()
    except Exception:
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    save_to_mysql()