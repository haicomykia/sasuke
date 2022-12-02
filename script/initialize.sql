CREATE DATABASE hanpen; 
-- DB作成
CREATE DATABASE kamome; 

-- 作成したDBへ切り替え
\c kamome

-- スキーマ作成
CREATE SCHEMA tagarasuschema;

-- ロールの作成
CREATE ROLE tagarasu WITH LOGIN PASSWORD 'KeMTcdcqQF9H';

-- 権限追加
GRANT ALL PRIVILEGES ON SCHEMA tagarasuschema TO tagarasu;