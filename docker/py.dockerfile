FROM python:3.13-slim-bullseye

# install modules a unprivileged user
RUN useradd -m api
USER api

RUN pip install fastapi uvicorn

# bindmount directory
WORKDIR /app 

ENTRYPOINT [ "/home/api/.local/bin/uvicorn" ]
CMD [ "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
