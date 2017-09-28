"""
This file was created at Smartbuzz Inc.
For more information visit http://www.smartbuzzinc.com
"""
import requests
from oauth2_provider.models import Application


class GenerateToken(object):

	def __init__(self, accessToken, backend, ):
		self.access_token = accessToken
		self.backend = backend
		self.app = Application.objects.get(name="GeneralApp")

	def generate_jwt(self):
		data = {"client_id": self.app.client_id, "client_secret":self.app.client_secret, "backend":self.backend, "grant_type":"convert_token", "token":self.access_token}
		url = ""
		res = requests.post(url=url,)


"""
{"client_id":"b2VwUpiCGWePrap3y1fg1QdDuxVcmNdtcBOGfZ9a","client_secret":"IxYEGPIuKNR0aq99IzP77ItgOa8R21LpTDbSVy3ppaolHBGY8hMKz74HTB4NzXbmPxhBtAFRO4Co1pUudD2R0Zbpj5IAOK35vrizKe7Q66QdMcT9qhRIeCLktwRNKTua","grant_type":"convert_token","token":"ya29.GlvUBELg3TfwbKj7H2UQwdP2XX4WeNYvP69Q0WEQJaSdgCsrUPIvJczbQozbSHaUlyw3EndVjPT3_73mTKz22U1vjGnEF5FxxPJTSGj4r7o0PSmtEjAC8p6EkCsm", "backend":"google-oauth2"}
"""