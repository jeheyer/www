function FindProxyForURL(url, host)
{

    Proxy = "1690.gcp.whamola.net:3128";

    // Don't use proxy for Localhost
    if (isPlainHostName(host) || localHostOrDomainIs(host, "localhost") || dnsDomainIs(host, ".localdomain") || shExpMatch(host, "127.*.*.*"))
        return "DIRECT";

    if (dnsDomainIs(host, ".gxsonline.net") || dnsDomainIs(host, ".idldap.net") || dnsDomainIs(host, ".resldap.net"))
        return "PROXY " + Proxy + ";";
    if (dnsDomainIs(host, "jira.opentext.com") || dnsDomainIs(host, "confluence.opentext.com") || dnsDomainIs(host, "sm.opentext.com"))
        return "PROXY " + Proxy + ";";
    if (dnsDomainIs(host, ".dropbox.com") || dnsDomainIs(host, ".dropboxstatic.com") || dnsDomainIs(host, ".dropboxcaptcha.com") || dnsDomainIs(host ".dropboxexperiment.com"))
        return "PROXY " + Proxy + ";"; 
    if (dnsDomainIs(host, ".hightail.com") || dnsDomainIs(host, ".yousendit.com"))
        return "PROXY " + Proxy + ";"; 

    return "DIRECT";
}

