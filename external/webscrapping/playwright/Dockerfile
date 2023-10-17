# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

# COPY /home/victor/pipelines/airflow/external/webscrapping /home/pwuser/

COPY ./teste_playwright.py /home/pwuser/

COPY ./seccomp_profile.json /home/pwuser/

RUN mkdir /home/pwuser/downloads
# VOLUME /home/pwuser/downloads


# COPY ./teste.py /home/pwuser/

USER root

RUN pip install playwright && \
    playwright install chrome firefox && \
    pip install ipython nest_asyncio pandas

RUN chown -R pwuser:pwuser /home/pwuser/    

USER pwuser
RUN ls -la /home/pwuser/
# COPY ./teste.py /home/pwuser/
# CMD [ "python", "teste.py" ]
# WORKDIR /home/pwuser

