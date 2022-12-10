-- DB作成
DROP DATABASE IF EXISTS hanpen;
CREATE DATABASE hanpen TEMPLATE template0 ENCODING 'UTF-8' LC_COLLATE 'ja_JP.UTF-8' LC_CTYPE 'ja_JP.UTF-8';

-- 作成したDBへ切り替え
\c hanpen

-- スキーマ作成
CREATE SCHEMA sasukeschema;

-- ロールの作成
CREATE ROLE sasuke WITH LOGIN PASSWORD 'KeMTcdcqQF9H';

-- 権限追加
GRANT ALL PRIVILEGES ON SCHEMA sasukeschema TO sasuke;