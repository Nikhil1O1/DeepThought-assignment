
from urllib.parse import urlsplit


#get domain name 
def get_domain_name(url):
    #print('in program')
    result = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    #print('step res')
    result = result.split('/')
    #print('step res.spl')
    result=result[2].split('.')
    #print('step res after')
    print(result[-2]+'.'+result[-1])

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


