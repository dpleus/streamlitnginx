# Inspired by https://ngbala6.medium.com/deploy-streamlit-app-on-nginx-cfa327106050

FROM continuumio/miniconda3
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update
RUN DEBIAN_FRONTEND='noninteractive' apt-get -y install nginx ufw

COPY . .
# Nginx config
COPY config/streamlitnginxconf /etc/nginx/sites-available/streamlitnginxconf
RUN ln -s /etc/nginx/sites-available/streamlitnginxconf /etc/nginx/sites-enabled
RUN ufw allow 9000

# Streamlit config
COPY config/config.toml /root/.streamlit/config.toml

EXPOSE 9000
CMD nginx; streamlit run sample/ui.py