from TikTokApi import TikTokApi
# import pprint

PATH = ""
verifyFp = ""

api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

trends = api.trending()

print(trends)
