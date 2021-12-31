FROM python:3.7-slim
WORKDIR /code
COPY . .
RUN pip install requests bs4 pyqt5 ui sys
ENV PATH=/root/.local:$PATH
ENTRYPOINT ["python3", "./main.py"]