FROM        wnrhd114/1010235_python
MAINTAINER  wnrhd114@gmail.com

ENV         LANG C.UTF-8

COPY         . /srv/app
WORKDIR     /srv/app


#supervisor 안에 파일 넣기
COPY        .config/supervisor/supervisor.conf /etc/supervisor/conf.d/

COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default

CMD         supervisord -n

EXPOSE      80 8000