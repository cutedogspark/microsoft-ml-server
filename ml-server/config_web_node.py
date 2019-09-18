import os
import json

from collections import OrderedDict

sqlserverConnection = os.environ["ConnectionString"]
thumbprint = os.environ["Thumbprint"]

webNodeAppSettingsFilePath = "/opt/microsoft/mlserver/9.4.7/o16n/Microsoft.MLServer.WebNode/appsettings.json"

data = json.loads(open(webNodeAppSettingsFilePath, "r").read().decode("utf-8-sig").encode("utf-8").replace("\r\n",""), object_pairs_hook=OrderedDict)

data["ConnectionStrings"]["sqlserver"]["Enabled"] = True
data["ConnectionStrings"]["sqlserver"]["Connection"] = sqlserverConnection
data["ConnectionStrings"]["defaultDb"]["Enabled"] = False

data["Authentication"]["JWTSigningCertificate"]["Enabled"] = True
data["Authentication"]["JWTSigningCertificate"]["StoreName"] = "Root"
data["Authentication"]["JWTSigningCertificate"]["StoreLocation"] = "CurrentUser"
data["Authentication"]["JWTSigningCertificate"]["SubjectName"] = "CN=LOCALHOST"
data["Authentication"]["JWTSigningCertificate"]["Thumbprint"] = thumbprint

with open(webNodeAppSettingsFilePath, "w") as f:
    json.dump(data, f, indent=2, sort_keys=False)
