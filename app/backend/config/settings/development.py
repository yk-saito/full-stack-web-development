from .base import *

DATABASES = {
  'default': {
    # MySQLを使用する設定
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'app',
    'USER': 'root',
    'PASSWORD': 'password',
    # コンテナからホストを参照するための設定
    'HOST': 'host.docker.internal',
    'PORT': '53306',
    # データベースの「処理の一貫性」を保証する設定（トランザクション管理）
    # `True`を設定すると、処理の最後まで到達した場合にデータベースをCOMMIT（確定）するようになる
    'ATOMIC_REQUESTS': True
  }
}