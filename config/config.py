import logging
import re

# Logger config
log_level = logging.DEBUG
log_fhandler = logging.FileHandler("url_crawler.log")
log_fhandler.setLevel(log_level)
log_formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
)
log_fhandler.setFormatter(log_formatter)
log_shandler = logging.StreamHandler()
log_shandler.setLevel(logging.WARNING)

root_log = logging.getLogger()
root_log.addHandler(log_fhandler)

# Starting point URL
start_url = "https://www.zoomit.ir/"

# Allowed domains
allowed_domains = ["zoomit.ir"]

# Regex for URLs to keep
regex_url = re.compile("http(s?)://" + ".*" + allowed_domains[0] + ".*/?")

# Common URL regex
# regex = re.compile(
# "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")
# Max depth for links
max_depth = 2

# HTTP request headers
request_headers = {
    "Host": "www.zoomit.ir",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Celery broker - Redis
BROKER_URL = "redis://localhost:6379"
