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
        proxy_pass http: //unix:/tmp/starmountain.ink.socket;
    }
}


