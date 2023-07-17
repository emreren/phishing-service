FROM python:3.11

# Crontab paketini yükle
RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY . .

# Crontab dosyasını kopyala
COPY crontab /etc/cron.d/my-cron-job

# Crontab çalıştırma komutu
RUN chmod 0644 /etc/cron.d/my-cron-job && \
    crontab /etc/cron.d/my-cron-job

# Yeni log dosyasını oluştur
RUN touch /var/log/cron.log

# Poetry komutlarını çalıştırabilmek için poetry yolu ekle
ENV PATH="/root/.local/bin:${PATH}"

# Cron servisini başlat
CMD cron && tail -f /var/log/cron.log
