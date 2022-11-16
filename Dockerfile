# ベースイメージ
FROM --platform=linux/x86_64 python:3.8

# 環境変数
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y locales git procps
RUN locale-gen ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo
WORKDIR /LINE-Chatbot
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 各種パッケージのインストール
RUN apt-get install build-essential sudo

# Mecab
RUN apt-get install mecab -y
RUN apt-get install libmecab-dev
RUN apt-get install mecab-ipadic-utf8 -y
# RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git 
COPY  ./mecab-ipadic-neologd .
RUN  bin/install-mecab-ipadic-neologd -y

# CRF++ (Cabochaで必要)
COPY ./CRF++-0.58.tar.gz .
RUN wget -O /tmp/CRF++-0.58.tar.gz 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ' \
    && cd /tmp/ \
    && tar zxf CRF++-0.58.tar.gz \
    && cd CRF++-0.58 \
    && ./configure \
    && make \
    && make install

# Cabocha
RUN ls
RUN export FILE_ID=0B4y35FiV1wh7SDd1Q1dUQkZQaUU
RUN export FILE_NAME=cabocha-0.69.tar.bz2
RUN curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" > /dev/null
RUN export CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
RUN curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o cabocha-0.69.tar.bz2

RUN echo "/usr/local/lib" >> /etc/ld.so.conf.d/lib.conf \
    && ldconfig
RUN apt-get install libmecab2
COPY ./cabocha-0.69.tar.bz2 .
RUN bzip2 -dc cabocha-0.69.tar.bz2 | tar xvf - \
    && cd cabocha-0.69 \ 
    && ./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8 \
    && make \
    && make check \
    && sudo make install \
    && sudo ldconfig \
    && cd python \
    && python setup.py build \
    && python setup.py install \
    && pip install mecab-python3

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN cp /etc/mecabrc /usr/local/etc/

# SHELL ["jupyter","lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''", "/bin/bash", "-c"]
#jupyter lab --ip=0.0.0.0 --allow-root --LabApp.token=''