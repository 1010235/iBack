FROM        wnrhd114/docker_ubuntu_pip
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

RUN         /root/.pyenv/versions/app_env/bin/python /srv/app/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

CMD         supervisord -n

EXPOSE      80 8000