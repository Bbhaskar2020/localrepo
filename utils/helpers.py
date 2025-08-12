import os
from datetime import datetime

def capture_screenshot(page, name):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{now}.png"
    page.screenshot(path=path)
    return path
