class Solution:
    def defang_ip_addr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)


if __name__ == '__main__':
    print(Solution().defang_ip_addr('1.100.24'))