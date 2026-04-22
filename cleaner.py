from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


TRACKING_PARAMS = {
    "fbclid", "gclid", "igshid", "mc_cid", "mc_eid"
}


WHITELIST = {
    "youtube.com": {"v", "t", "list"},
    "youtu.be": {"t"},
    "google.com": {"q"}  
}

def normalize_domain(netloc):
    netloc = netloc.split(":")[0]
    parts = netloc.split(".")
    return ".".join(parts[-2:])

def is_tracking_param(key):
    return key.startswith("utm_") or key.lower() in TRACKING_PARAMS

def clean_url(url):
    parsed = urlparse(url)
    domain = normalize_domain(parsed.netloc)

    params = parse_qs(parsed.query, keep_blank_values=True)

    whitelist_keys = WHITELIST.get(domain)
    clean_params = {}

    for k, v in params.items():

        if is_tracking_param(k):
            continue

        if whitelist_keys is not None:
            if k in whitelist_keys:
                clean_params[k] = v
        else:
            clean_params[k] = v

    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        "",
        urlencode(clean_params, doseq=True),
        ""
    ))