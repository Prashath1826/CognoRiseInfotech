import pyqrcode
url="https://in.linkedin.com/company/cognoriseinfotech"
a=pyqrcode.create(url)
a.svg('QR.svg',scale=5)
