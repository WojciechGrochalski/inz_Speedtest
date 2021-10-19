FROM python:3.8-alpine


RUN apk add --no-cache --update \
	    apache2 \
 		&& pip install  --no-cache-dir speedtest-cli 

EXPOSE 80 
LABEL Config Apache server

ARG interval=1
ENV interval ${interval}
WORKDIR /var/www/localhost/htdocs/
COPY speedtest.html index.html
COPY data.json data.json
RUN echo "ServerName localhost" >> /etc/apache2/httpd.conf
WORKDIR /
COPY script.py ./
COPY autostart.sh ./
RUN chmod +x autostart.sh

CMD ["sh", "autostart.sh"]
