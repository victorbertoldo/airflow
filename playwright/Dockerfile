# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

COPY ./teste_playwright.py /home/pwuser/

COPY ./seccomp_profile.json /home/pwuser/

# COPY ./teste.py /home/pwuser/

USER root

RUN pip install playwright && \
    playwright install chrome firefox && \
    pip install ipython nest_asyncio

USER pwuser

# COPY ./teste.py /home/pwuser/
# CMD [ "python", "teste.py" ]
# WORKDIR /home/pwuser

