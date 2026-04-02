class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_em=set()
        for email in emails:
            local,domain=email.split('@')
            cl_local=local.split('+')[0]
            cl_local=cl_local.replace('.','')
            unique_em.add((cl_local,domain))
        return len(unique_em)