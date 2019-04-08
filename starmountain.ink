server {
    charset utf-8;
    listen 443 ssl;
    server_name starmountain.ink;
    ssl on;
    ssl_certificate   /etc/nginx/cert/2031386_istarmountain.ink.pem;
    ssl_certificate_key /etc/nginx/cert/2031386_starmountain.ink.key;
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
        proxy_pass http: //unix:/tmp/starmountain.ink.socket;
    }
}
