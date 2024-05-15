# Problem 3 Defang IP address
def defang_ip_address(address):
  return address.replace(".", "[.]")
# Test examples
print(defang_ip_address("108.109.0.2"))
print(defang_ip_address("100.105.0.33"))
print(defang_ip_address("155.122.0.1.1.225"))
