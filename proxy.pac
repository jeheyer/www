function FindProxyForURL(url, host)
{

    Proxy = "whamola.net:3128";

    // Localhost
    if (isPlainHostName(host) || localHostOrDomainIs(host, "localhost") || shExpMatch(host, "127.*.*.*"))
        return "DIRECT";

    // OpenText Stuff not requiring proxy
    if (dnsDomainIs(host, "lit-vaanm-q005.resldap.net"))
        return "DIRECT";
    if (dnsDomainIs(host, ".cloud.opentext.com"))
        return "DIRECT";

    // OpenText Stuff requiring proxy
    if (dnsDomainIs(host, ".gxsonline.net") || dnsDomainIs(host, ".idldap.net") || dnsDomainIs(host, ".resldap.net"))
        return "PROXY " + Proxy + ";";
    if (dnsDomainIs(host, "jira.opentext.com") || dnsDomainIs(host, "confluence.opentext.com") || dnsDomainIs(host, "sm.opentext.com"))
        return "PROXY " + Proxy + ";";

    // Hightail Stuff
    if (dnsDomainIs(host, ".ops.hightail.com") || dnsDomainIs(host, ".ops-nonprod.hightail.com"))
        return "PROXY " + Proxy + ";"; 
    if (shExpMatch(host, "10.135.*") || shExpMatch(host, "10.41.*.*")) 
        return "PROXY " + Proxy + ";"; 

    return "DIRECT";
}

