server {
    charset utf-8;
    listen 80;
    server_name starmountain.ink;

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

server {
    charset utf-8;
    listen 443 ssl;
    server_name starmountain_ssh.ink;
    ssl on;
    ssl_certificate   /etc/nginx/cert/starmountain.ink.pem;
    ssl_certificate_key /etc/nginx/cert/starmountain.ink.key;
    ssl_session_timeout 5m;
    ssl_protocols SSLv2 SSLv3 TLSv1;
    ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
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



