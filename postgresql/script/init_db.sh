# 開発環境用のDocker postgresqlの起動設定を変更する
# 本番DBにあわせた設定にする


set -e

# sed -i -e"s/^lc_messages = 'en_US.utf8'.*$//" /var/lib/postgresql/data/tagarasu/postgresql.conf
sed -i -e"s/^lc_monetary = 'en_US.utf8'.*$/lc_monetary = 'ja_JP.utf8'/" /var/lib/postgresql/data/tagarasu/postgresql.conf
sed -i -e"s/^lc_numeric = 'en_US.utf8'.*$/lc_numeric = 'ja_JP.utf8'/" /var/lib/postgresql/data/tagarasu/postgresql.conf
sed -i -e"s/^lc_time = 'en_US.utf8'.*$/lc_time = 'ja_JP.utf8'/" /var/lib/postgresql/data/tagarasu/postgresql.conf