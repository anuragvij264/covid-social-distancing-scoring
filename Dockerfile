FROM tiangolo/uwsgi-nginx:python3.6

LABEL maintainer="Jitendra Singh <jitendra.singh@decimal.co.in>"

ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV STATIC_INDEX 0

ADD ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

COPY start.sh /start.sh
RUN chmod +x /start.sh

RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]