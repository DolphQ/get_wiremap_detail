import requests
import html2text

class wiremap_detail(object):

    def __init__(self, hostname):
        self._hostname = hostname

    def get_info(self):

        wiremap_url= "http://labsdb.eng.vmware.com/wiremap/index.php?action=search&page=0&dev_type=like&dev_name="+self._hostname

        html_1 = requests.get(wiremap_url).text



        wiremap_html2text = html2text.html2text(requests.get(wiremap_url).text, bodywidth=100)



        with open('wiremap_html2text','w', encoding='utf-8') as write_text:
            write_text.write(wiremap_html2text)



def main():
    wiremap=wiremap_detail("pek2-hs1-a0101")
    wiremap.get_info()

if __name__ == '__main__':
    main()
