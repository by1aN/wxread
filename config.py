# config.py 自定义配置
import os
import re

"""
github action部署或本地部署
从环境变量获取值,如果不存在使用默认本地值
每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM', '120'))
# pushplus or telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# push-plus
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# 复制的curl_bath命令
curl_str = os.getenv('WXREAD_CURL')

# 对应替换
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ptcz=d2f50f1c5ba8f8f0bb49cf54ba7de63a2f422849a3a52c105f6b57bf45ef1dee; _qpsvr_localtk=0.6737422069660328; luin=null; lskey=null; user_id=null; session_id=null; pgv_pvid=3554525522; mail5k=b357edac; _qimei_uuid42=1810e142916100be438d3b390e36009b5d76caea6c; _qimei_fingerprint=ca967fd4f5554f62ca0487b3bd04d275; _qimei_q36=; _qimei_h38=59a98b40438d3b390e36009b0200000d91810e; it_c=0; verifysession=h0167899be8cdcea0b41388bab3049af3bd031ce389564e0f4faa07c3bb1021b902c371bf71a9533e10; fqm_pvqid=72648f4e-56e5-4771-afbb-7f2720f46a8d; fqm_sessionid=55ff9be4-1f61-4a1b-a642-3bf4dc250b02; login_type=1; iip=0; eas_sid=W1j7o2M0L6w1v521q1J0I5I9y2; LW_uid=y1M7C2t0O6o1K5c1V1S1M5d1s6; pgv_info=ssid=s2206093482&pgvReferrer=; lolqqcomrouteLine=a20180929awards_a20180929awards_a20180929awards_a20180929awards_a20180929awards_index-tool_main; LOLWebSet_AreaBindInfo_1076862106=%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221076862106%2522%252C%2522rolename%2522%253A%2522by1aN%252328677%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1076862106%257C5%257C1076862106*%257C%257C%257C%257Cby1aN%25252328677*%257C%257C%257C1720615313%257C%2522%252C%2522md5str%2522%253A%2522E535E0FEB74191E0B4D257E348DBA10D%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D; LOLWebSet_AreaBindInfo_CDFC43B945046B08F2D5604F6CE4F2AE=%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221076862106%2522%252C%2522rolename%2522%253A%2522by1aN%252328677%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1076862106%257C5%257C1076862106*%257C%257C%257C%257Cby1aN%25252328677*%257C%257C%257C1720615313%257C%2522%252C%2522md5str%2522%253A%2522E535E0FEB74191E0B4D257E348DBA10D%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D; tokenParams=%3FADTAG%3Dlolweb.v3; RK=y3t8C1+zTP; rv2=806AC2F353D1D0C71DA8900C85222EDCD28AF72F3E90B443FA; property20=01FC7137D349DED177F1E092A3037EE92D4CD808BC8B686768634B3FB659E0AF7CB59D47AE387A72; qq_domain_video_guid_verify=a7d765b89e4388c8; vversion_name=8.2.95; video_omgid=a7d765b89e4388c8; o_cookie=1076862106; LW_sid=w1Y762S1j5o6t4j5K4x8B52875; ied_qq=o1076862106; 101qqcomrouteLine=main_main; mwegameqqcomrouteLine=a20240702jnh_a20240702jnh_a20240702jnh; _clck=1aalvld|1|fnz|0; pac_uid=0_9DmjhXCBpNAkd; suid=user_0_9DmjhXCBpNAkd; uin=o1076862106; skey=@2ce9Lus58; wr_fp=3376082629; wr_gid=203077143; wr_vid=373432258; wr_skey=oeF_0uyu; wr_pf=0; wr_rt=web%40R4XEmIf3PH4gMiRM73F_AL; wr_localvid=9b732220816421fc29b7588; wr_name=%E5%8D%9A%E5%B0%94%E8%B5%AB%E6%96%AF; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0011-~jg8hZqfs_GZBRN1RxEkGe6%2F0; wr_gender=1',
    'Origin': 'https://weread.qq.com',
    'Pragma': 'no-cache',
    'Referer': 'https://weread.qq.com/web/reader/787328c0813ab9683g0195cfk8f132430178f14e45fce0f7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=c92fb6026639435093955507ce7d5b3d',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sentry-trace': 'c92fb6026639435093955507ce7d5b3d-8d7e017fe1287c9e',
}
#
# #对应替换
cookies = {
    'ptcz': 'd2f50f1c5ba8f8f0bb49cf54ba7de63a2f422849a3a52c105f6b57bf45ef1dee',
    '_qpsvr_localtk': '0.6737422069660328',
    'luin': 'null',
    'lskey': 'null',
    'user_id': 'null',
    'session_id': 'null',
    'pgv_pvid': '3554525522',
    'mail5k': 'b357edac',
    '_qimei_uuid42': '1810e142916100be438d3b390e36009b5d76caea6c',
    '_qimei_fingerprint': 'ca967fd4f5554f62ca0487b3bd04d275',
    '_qimei_q36': '',
    '_qimei_h38': '59a98b40438d3b390e36009b0200000d91810e',
    'it_c': '0',
    'verifysession': 'h0167899be8cdcea0b41388bab3049af3bd031ce389564e0f4faa07c3bb1021b902c371bf71a9533e10',
    'fqm_pvqid': '72648f4e-56e5-4771-afbb-7f2720f46a8d',
    'fqm_sessionid': '55ff9be4-1f61-4a1b-a642-3bf4dc250b02',
    'login_type': '1',
    'iip': '0',
    'eas_sid': 'W1j7o2M0L6w1v521q1J0I5I9y2',
    'LW_uid': 'y1M7C2t0O6o1K5c1V1S1M5d1s6',
    'pgv_info': 'ssid=s2206093482&pgvReferrer=',
    'lolqqcomrouteLine': 'a20180929awards_a20180929awards_a20180929awards_a20180929awards_a20180929awards_index-tool_main',
    'LOLWebSet_AreaBindInfo_1076862106': '%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221076862106%2522%252C%2522rolename%2522%253A%2522by1aN%252328677%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1076862106%257C5%257C1076862106*%257C%257C%257C%257Cby1aN%25252328677*%257C%257C%257C1720615313%257C%2522%252C%2522md5str%2522%253A%2522E535E0FEB74191E0B4D257E348DBA10D%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D',
    'LOLWebSet_AreaBindInfo_CDFC43B945046B08F2D5604F6CE4F2AE': '%257B%2522areaid%2522%253A%25225%2522%252C%2522areaname%2522%253A%2522%25E7%258F%25AD%25E5%25BE%25B7%25E5%25B0%2594%25E5%259F%258E%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221076862106%2522%252C%2522rolename%2522%253A%2522by1aN%252328677%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1076862106%257C5%257C1076862106*%257C%257C%257C%257Cby1aN%25252328677*%257C%257C%257C1720615313%257C%2522%252C%2522md5str%2522%253A%2522E535E0FEB74191E0B4D257E348DBA10D%2522%252C%2522roleareaid%2522%253A%25225%2522%252C%2522sPartition%2522%253A%25225%2522%257D',
    'tokenParams': '%3FADTAG%3Dlolweb.v3',
    'RK': 'y3t8C1+zTP',
    'rv2': '806AC2F353D1D0C71DA8900C85222EDCD28AF72F3E90B443FA',
    'property20': '01FC7137D349DED177F1E092A3037EE92D4CD808BC8B686768634B3FB659E0AF7CB59D47AE387A72',
    'qq_domain_video_guid_verify': 'a7d765b89e4388c8',
    'vversion_name': '8.2.95',
    'video_omgid': 'a7d765b89e4388c8',
    'o_cookie': '1076862106',
    'LW_sid': 'w1Y762S1j5o6t4j5K4x8B52875',
    'ied_qq': 'o1076862106',
    '101qqcomrouteLine': 'main_main',
    'mwegameqqcomrouteLine': 'a20240702jnh_a20240702jnh_a20240702jnh',
    '_clck': '1aalvld|1|fnz|0',
    'pac_uid': '0_9DmjhXCBpNAkd',
    'suid': 'user_0_9DmjhXCBpNAkd',
    'uin': 'o1076862106',
    'skey': '@2ce9Lus58',
    'wr_fp': '3376082629',
    'wr_gid': '203077143',
    'wr_vid': '373432258',
    'wr_skey': 'oeF_0uyu',
    'wr_pf': '0',
    'wr_rt': 'web%40R4XEmIf3PH4gMiRM73F_AL',
    'wr_localvid': '9b732220816421fc29b7588',
    'wr_name': '%E5%8D%9A%E5%B0%94%E8%B5%AB%E6%96%AF',
    'wr_avatar': 'https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0011-~jg8hZqfs_GZBRN1RxEkGe6%2F0',
    'wr_gender': '1',
}

# 保留| 默认读三体，其它书籍自行测试时间是否增加
data = {
    "appId": "wb182564874663h296931602",
    "b": "2bb32ff0813ab6ffcg014315",
    "c": "115328e02df115f89503b27",
    "ci": 5,
    "co": 15196,
    "sm": "县政治必须农民起来才能澄清，广东的海丰已",
    "pr": 4,
    "rt": 11,
    "ts": 1740666137106,
    "rn": 735,
    "sg": "5240973c23567bd83cd25d1151e3f04012aafe8f377201362456150751ba4768",
    "ct": 1740666137,
    "ps": "a78326f07a600bb4g01332a",
    "pc": "a78326f07a600bb4g01332a",
    "s":"17267eae",
}


def convert(curl_command):
    """提取headers与cookies"""
    # 提取 headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    cookie_string = headers.pop('cookie', '')
    for cookie in cookie_string.split('; '):
        key, value = cookie.split('=', 1)
        cookies[key] = value

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
