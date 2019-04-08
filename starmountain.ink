server {
    charset utf-8;
    listen 80;
    server_name starmountain.ink;

    location /static { ②
        alias /home/yangxg/sites/demo.zmrenwu.com/django-blog-tutorial/static; 
    }

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

server {
    charset utf-8;
    listen 443 ssl;
    server_name starmountain_ssl.ink;
    ssl on;
    ssl_certificate   /home/guozirui/starmountain.ink/starmountain/2031386_starmountain.ink_nginx/2031386_istarmountain.ink.pem;
    ssl_certificate_key /home/guozirui/starmountain.ink/starmountain/2031386_starmountain.ink_nginx/2031386_starmountain.ink.key;
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
