
def urlencode(parameters):
    st = ''
    for (key,value) in parameters.items():
        st = st + key + '=' + str(value) + '&'
    st = st[:-1]
    return st

token = 123
search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
query_id = {
'action': 'search_biz',
'token' : token,
'lang': 'zh_CN',
'f': 'json',
'ajax': '1',
'random': 456,
'query': 'hao',
'begin': '0',
'count': '5'
}
print(search_url + urlencode(query_id))
