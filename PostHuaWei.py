# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
import collections
def huaWei():
        
        #data={"signType":"RSA","amount":"0.01","returnCode":"0","time":"1374756304385","orderID":"A21354D84555S7854FCV45","requestId":"2013-07-25-08-44-16-847","errMsg":"success","userName":"wuhao"}
      
        
        privateKey="MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxnWw4Hore2epvudcY1bwR88safssIPphX2+0hK5bvyxmxP6O5aAwV6h6lKISueA9p1v8ULlBJUDD9zB/Yv1gBjcHctL+30c01XlqHtiQ9gQwZv6nQdoTbq8QCfAu/KxNyKlnLCGMl9LCFlSqQZYTSpUFf5xBNu6wqWmKZHdJv3xOg51UqHRls31SwzRC+txLtm7QnyL1Md390GGCRYDJouXufHjuEVZWEsSQHQILxqkJongDGEQJG2yITtXRIcwhBopNog8GhdivxdQkPVR5ub7+Vka6YeqSVcvDXufkv70QQM88pkGWxWQoQGHaW3Oq+b9CbVrcepMxDjkhPWz/RAgMBAAECggEASrU6hchjBSWH9IKotOuB9dMjxPs8DzW1Ao+hCGi7ThWRsvpftWbMXpNhXHrUhEY/xXcHR8fLQWsXkElBw/uH2u9zcZAdbAY1WJNdZOP6DlyvaE0z8llHvNZc1eazUi+eOFET/9CBU7++WBHMG3x4B9o2y033j5q26gGmo1zl3OO15Z0AidhrsYUZcKI6gJp0ZfRhXPS39xrYHiOX1qxCjE9s0r7qpBG5oQ4fKxLCftYHs1R/HYYVXfrNtrMQYNNyMlgeBHfXPwLuXxw/M7pYT2kgLyUXzwA8JGot4hSxcqzE8RqdWRty/2/p643kKu+WNX01K9bgs2dUXZCvD5KKWQKBgQDoRWdJAXH3qZBeAOJoj/fJBhaU8zkDBnCogGfbqpwvrgIi4cEO2sjgSuFtwc+LcUV4Cv+w/qXKzkaTYvo1Y8RGhMrcNXHfUkTwV0zHjMDO5i5u6QsUuxnTye9p6OO7nFwd8PTLeOVJzMkGo3bJyHPpa1LuMHtP/3AZYLhjq7P9iwKBgQDDwpgLDh4uWzuxoguT0XYxN1xXMTxqnOzTQ+SeSgDm9N7S10uNxkeUaudap7cDChyzi3AKaAg/jMlrs8nyKrAtbeukST+A4gPYO6YlF7rGuKnG37PpaiWqqEbTZegrHsNs3r5/23RfHvyVAlrphAZxaAg5dlEGQgf1BLQ7YCkbkwKBgD8CzQFGLhfE3VBTJxi8rbjQOQIRdY73iUp9Ay/ZeeOJbjTuT4RrIAGQ7tTqthYbFYB6Y2Etw+ZfzU+gk0Y2mYGT9sCEky7FT8RvunmMGqZGVaRq/kGSfHAzIQr3TgiQY4EP5Cjq1DEQKBzv7YLSKXfSUL4jUuCh6FRKI9uOMhb/AoGBALR4+vj+K/7qpy7NSMUfD0qyUhQkVSGoyIDAj80KRqilyaMxTvtGeAkxQVcHVaactPclrsY5QJlt7ue3GY+DoWZQdzS/PqdQNuErpLF/nfbEmei5pcCj1lPtzVXpFlBijSIafB+drzxecdfiEvRDfjkhAqwPEwWk7HcLvikbLuq3AoGAPICdTFOWA0Is4qWAJySdsOnlvw6RaAWIpsP4ISeQuNsRLti5jy2sFdrg5DDhgBprW9GveqkR2V3L2WGqJug35EnMoSk8FMC3JBnLOZHKAn/W3bfODscY/AXuBeceXooGhCnlaoY+dqhcfoUJU6cYKl/TmSLADxTW2qD85uGiDow="
        publictKey="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsZ1sOB6K3tnqb7nXGNW8EfPLGn7LCD6YV9vtISuW78sZsT+juWgMFeoepSiErngPadb/FC5QSVAw/cwf2L9YAY3B3LS/t9HNNV5ah7YkPYEMGb+p0HaE26vEAnwLvysTcipZywhjJfSwhZUqkGWE0qVBX+cQTbusKlpimR3Sb98ToOdVKh0ZbN9UsM0QvrcS7Zu0J8i9THd/dBhgkWAyaLl7nx47hFWVhLEkB0CC8apCaJ4AxhECRtsiE7V0SHMIQaKTaIPBoXYr8XUJD1Uebm+/lZGumHqklXLw17n5L+9EEDPPKZBlsVkKEBh2ltzqvm/Qm1a3HqTMQ45IT1s/0QIDAQAB"

        str='中文lPmxt8hlyXDeg8UwXLG8rPAeiX28ZQvheo3hOwxPuMT+qvKGQIhpVP2SJaoBKurvX2QKltzLEaDoZuFhtTCoHlVSIbWz4I7NGjSbN48VyMhw+agTMJrq85LQWzlXlW7JF8a8n2xcwbjv/ClI7BV806+pmELMHeeEjdDlJxtXmXbfP5W7cuPDlnodCYJ92gfMUPAdVSzV6zTHQirjQMy0qHZAzDShaQ4IRjJyrqAuwGC5k2wbey+wDGiUXfIgy8Nes38oG4KpV4DIDysM+dGc7U2wRVB4TWt66PhL34vtQT8SDEwnU8WB8Qi/uu3Ppu3My6biaInY22/hGWh3sRIWTQ=='
        str1=urllib.urlencode({"sign":str})
        data2="signType=R&amount=0.01&returnCode=0&time=1374756304385&orderID=A21354D84555S7854FCV45&requestId=2013-07-25-08-44-16-847&errMsg=success&userName=wuhao"+'&'+str1
        data2.encode("utf-8")
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        content="accessMode=0&amount=1.00&notifyTime=1520220738928&orderId=WW4546546&orderTime=2018-03-05 11:32:18&payType=6&productName=中文&requestId=WW4546546&result=0&spending=0.01&tradeTime=2018-03-05 11:32:18&userName=890086000001005899"+'&'+str1
        request = urllib2.Request(url='http://192.168.1.158:8080/HuaWei/HaweiPay', headers=headers, data=content)
        response = urllib2.urlopen(request)
        print response.read()


def aliBaBa():
        paramData={"tradeId":"AS454212","tradeTime":"20150527130000","orderId":"OID444121","gameId":"15412","amount":"1.00","payType":"2","attachInfo":"202cb962234w4ers2aa","orderStatus":"S","failedDesc":"reason"};
        param={"ver":"1","sign":"2ca00965263d86ef6880bccb643c30b1"};
        param["data"]=paramData;
        headers={'Content-Type':'application/json'}
        request=urllib2.Request(url='http://192.168.1.158:8080/HuaWei/ALiPay',headers=headers,data=json.dumps(param))
        print json.dumps(param)
        response=urllib2.urlopen(request);
        print response.read()

def baidu():
        #字典也是无序的，如果非json传递数据的话，需要注意传的时候应该是有序的字典
        paramData="appid=134&orderid=tzqgEpl6luIxdwp&amount=100&unit=fen&jfd=478&status=success&paychannel=ct_sfdx&phone=15305000062&channel=CUCC&from=gsdk&sign=145d1821d9ac5d4381fd6f568034f65d&extchannel=17575&cpdefinepart=cporderinfo"
        param={
                "appid":"134",
                "orderid":"tzqgEpl6luIxdwp",
                "amount":"100",
                "unit":"fen",
                "jfd":"478",
                "status":"success",
                "paychannel":"ct_sfdx",
                "phone":"15305000062",
                "channel":"CUCC",
                "from":"gsdk",
                "sign":"145d1821d9ac5d4381fd6f568034f65d",
                "extchannel":"17575",
                "cpdefinepart":"1234567"
                }
        #有序字典
        d1 = collections.OrderedDict()
        d1["appid"]="134"
        d1["orderid"]="tzqgEpl6luIxdwp"
        d1["amount"]="100"
        d1["unit"]="fen"
        d1["jfd"]="478"
        d1["status"]="success"
        d1["paychannel"]="ct_sfdx"
        d1["phone"]="15305000062"
        d1["channel"]="CUCC"
        d1["from"]="gsdk"
        d1["sign"]="2dda8ea178bcd33e0dd5346e8f45faaf"
        d1["extchannel"]="17575"
        d1["cpdefinepart"]="1234567"
        headers={"Content-Type":"application/urlencoded"}
        request=urllib2.Request(url='http://192.168.1.155:8080/HuaWei/BaiduPay',headers=headers,data=urllib.urlencode(d1))
        print urllib.urlencode(d1)
        response=urllib2.urlopen(request)
        print response.read()


if __name__=="__main__":
        huaWei()
        #aliBaBa()
        #baidu()
