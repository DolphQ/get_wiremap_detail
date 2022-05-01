# -*- coding:utf-8 -*-
import requests, re


class wiremap_detail(object):

    def __init__(self, hostname):
        self._hostname = hostname

    def get_wiremap(self):

        wiremap_url = "http://labsdb.eng.vmware.com/wiremap/index.php?action=search&page=0&dev_type=like&dev_name=${query}"

        wiremap_csv = requests.get(wiremap_url, params={'dev_name':self._hostname,'output':'csv'}).text

        wiremap_info = re.sub('\"', '', wiremap_csv, flags=re.IGNORECASE)

        with open('wiremap_html2text','w', encoding='utf-8') as write_text:
            write_text.write(wiremap_info)
            wiremap_list = []

        for wiremap_line in wiremap_info.split('\n'):
            wiremap_field = wiremap_line.split(',')

            wiremap_list += [wiremap_field]

        wiremap_list.pop()
        for i in wiremap_list:
            print('%-20s %-20s %-20s %-20s %-20s' % (i[0], i[1], '<--'+ i[2] + '-->', i[3], i[4]))

def main():
    wiremap=wiremap_detail("iobj004")
    wiremap.get_wiremap()

if __name__ == '__main__':
    main()


