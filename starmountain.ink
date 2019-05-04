server {
    charset utf-8;
    listen 443;
    server_name starmountain.ink;
    ssl on;
    ssl_certificate   /usr/local/nginx/conf/cert/starmountain.ink.pem;
    ssl_certificate_key /usr/local/nginx/conf/cert/starmountain.ink.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    location /static {
        alias /home/guozirui/starmountain.ink/starmountain/static;
    }

    location /media {
        alias /home/guozirui/starmountain.ink/starmountain/media;
    }
    location / {
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/starmountain.ink.socket;
    }

}

