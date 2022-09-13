FROM nginx

RUN apt update


RUN apt --yes install python3

RUN apt-get install -y python3-pip

RUN apt-get install -y libmariadb3 libmariadb-dev

RUN pip3 install cgi-tools

RUN pip install mariadb

RUN apt-get update && apt-get install -y spawn-fcgi fcgiwrap

RUN mkdir /usr/share/nginx/bdd

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

COPY nginx.conf /etc/nginx/

COPY index.cgi /usr/share/nginx/bdd/

COPY afficher.cgi /usr/share/nginx/bdd/

RUN chmod 755 /usr/share/nginx/bdd/index.cgi

RUN chmod 755 /usr/share/nginx/bdd/afficher.cgi

RUN mkdir /etc/nginx/ssl

COPY  fastcgi_params /etc/nginx/

COPY server.crt /etc/nginx/ssl/

COPY server.key /etc/nginx/ssl/

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
