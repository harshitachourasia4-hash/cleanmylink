from urllib.parse import urlparse,urlencode,parse_qs,urlunparse
UTM_PARAMS={"utm_source","utm_medium","utm_campaign","utm_term","utm_content"}

whitelist={
    "youtube.com":{"t","v","list"},
           "youtu.be":{"t"}
           }
def clean_url(url):
    parsed=urlparse(url)
    domain=parsed.netloc.replace("www.","")
    safe_keys=whitelist.get(domain,set())
    params=parse_qs(parsed.query)
    clean_params={
        k:v for k,v in params.items() if k not in UTM_PARAMS or k in safe_keys      
    }
    new_query = urlencode(clean_params,doseq=True) #doseq parameter to arrange or convert list(multiple data) in url 
    #join all parts of url back
    clean=urlunparse((parsed.scheme,domain,parsed.path,"",new_query,"")) #urlunnparse take single argument -tuple so (())   
    return clean