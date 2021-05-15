from douyin import AwemeSDK

token = 'xxxxxxxx'
host  = 'http://xxxxx.xx.xx'
sdk   = AwemeSDK(token,host)

result = sdk.GetUserInfo('100000004548')
print(result)