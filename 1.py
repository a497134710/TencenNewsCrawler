import requestsfrom lxml import etreedef firstPage(url):    response = requests.get('一级页面的url', params='请求头的参数')    first_page_html = etree.HTML(response.text)    # 二级页面的url列表    second_page_urlList = first_page_html.xpath('解析一级页面的a标签')    item_dic_list = []    for second_page_url in second_page_urlList:        res = requests.get(second_page_url)        second_page_html = etree.HTML(res.text)        # 然后再解析相应的字段        item_dic = parseSecondPage(second_page_html)        # 将每一个页面解析得到的东西添加进去        item_dic_list.append(item_dic)        '''        在这里你可以再写一个存储的方法,        存json,或者存数据库                '''def parseSecondPage(second_page_html):    item_dic = {}    # 比如二手房的名字和价格    item_dic['name'] = second_page_html.xpath('../div//..../text()')[0]    item_dic['price'] = second_page_html.xpath('.//.....')    return item_dic