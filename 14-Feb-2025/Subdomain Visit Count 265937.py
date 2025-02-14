# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dm = defaultdict(int)
    
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                dm[subdomain] += count
        
        result = [f"{count} {domain}" for domain, count in dm.items()]
        return result
        