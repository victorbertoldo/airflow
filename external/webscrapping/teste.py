import docker
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

cwd = os.getcwd()
local_downloads = '{}/downloads'.format(cwd)
sel_downloads = '/home/seluser/downloads'
client = docker.from_env()
container = client.containers.run('selenium/standalone-chrome',
        #command=['usermod', '-u 1000 {}'.format(sel_downloads)],
        #user='1000'
        volumes=['{}:{}'.format(local_downloads, sel_downloads),
                 '/dev/shm:/dev/shm'],
        ports={'4444/tcp':4444},
        network='container_bridge',
        detach=True)
cli = docker.APIClient()

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
chrome_driver = '{}:4444/wd/hub'.format('http://127.0.0.1') # This is only required for local development
#chrome_driver = '{}:4444/wd/hub'.format('http://ec2-52-31-168-109.eu-west-1.compute.amazonaws.com') # This is only required for local development

# wait for remote, unless timeout.
while True:
    try:
        driver = webdriver.Remote(
            command_executor=chrome_driver,
            desired_capabilities=DesiredCapabilities.CHROME, options=options)
        print('remote ready')
        break
    except:
        print('remote not ready, sleeping for ten seconds.')
        time.sleep(10)
        
# Enable downloads in headless chrome.
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': sel_downloads}}
command_result = driver.execute("send_command", params)