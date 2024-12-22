FROM sunpeek/poetry:py3.12-slim

WORKDIR /home/sinage
COPY . .
RUN poetry install
CMD poetry shell
CMD tail -f /dev/null
#ENTRYPOINT ["/bin/bash", "run.sh"]
