def count_domains(cpdomains):
    """
    O(N)
    """
    domains = {}

    for count_domain in cpdomains:
        count, url = count_domain.split(' ')

        splited_domains = url.split('.')
        total_domains = len(splited_domains)
        for i in range(total_domains):
            domain = '.'.join(splited_domains[i:total_domains])
            domains[domain] = domains.get(domain, 0) + int(count)

    return ['%s %s' % (v, k) for k, v in domains.items()]

if __name__ == '__main__':
    print(count_domains(cpdomains = ["9001 discuss.leetcode.com"]))
    print(count_domains(cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
