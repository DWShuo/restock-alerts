FROM archlinux:latest
COPY requirements.txt requirements.txt
COPY discord-restock-alerts.py /
RUN pacman -Syu --noconfirm python python-pip firefox geckodriver
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/python", "discord-restock-alerts.py"]