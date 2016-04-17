import requests
import secrets
import hmac
import hashlib
import binascii

sts = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&AWSAccessKeyId="+secrets.access+"&AssociateTag="+secrets.associate+"&Operation=ItemSearch&Keywords=the%20hunger%20games&SearchIndex=Books&Timestamp=2016-04-20T08:30:20Z&Signature="

def sign(key, msg):
  return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey():
    kDate = sign(("AWS4" + secrets.secret).encode('utf-8'), "20160417")
    kRegion = sign(kDate, "us-east-1")
    kService = sign(kRegion, "AWSECommerceService")
    kSigning = sign(kService, "aws4_request")
    return kSigning

signature = binascii.hexlify(sign(getSignatureKey(), sts))
sts += signature

print signature

r = requests.get(sts)

print(r.status_code)
