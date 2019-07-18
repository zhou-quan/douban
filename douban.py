import requests

def get_pages(category, tag, page_num):
    url_base = 'https://movie.douban.com/j/search_subjects?type=%s&tag=%s&sort=recommend&page_limit=20&page_start='
    try:
        url = url_base % (category, tag) + str(page_num)
        try:
            result = requests.get(url).text
            jresult = json.loads(result)
            pages = jresult.get('subjects')
        except:
            print('爬取' + urlbase + str(page_num) + '失败！')
        time.sleep(2)
        return pages
    except:
        print('获取第%s页电影列表失败' % page_num)

        
def save_to_file(content_list, file_name): 
    with open(file_name,"w") as f:
        for content in content_list:
            f.write(content + "\n")
    f.close()
    print("write over!")


if __name__ == '__main__':
    # 豆瓣每项电视剧只有前500部
    page_nums = 25  
            
    url_base = 'https://movie.douban.com/j/search_subjects?type=%s&tag=%s&sort=recommend&page_limit=20&page_start='
    
    tv_url_list = ['美剧', '英剧', '韩剧', '日剧', '国产剧', '港剧', '日本动画', '综艺', '纪录片']
    movie_url_list = ['热门','最新', '经典', '豆瓣高分', '冷门佳片', '华语', '欧美', '韩国', '日本', '动作', '喜剧', '爱情', '科幻', '悬疑', '恐怖', '治愈']
    
    for cate in ['tv', 'movie']:
        for tag in eval('%s_url_list'%cate):
            print('*' * 10, cate, tag, '*' * 10)
            results = []
            for i in range(page_nums):
                re_list = get_pages(cate, tag, i * 20)
                punc = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.():：。· "
                punctuation = punc
                for l in re_list:
                    l['title'] = re.sub(r"[%s]+" % punctuation, "", l.get('title'))
                    results.append(l['title'])
                print((i+1)*100.0/pages,"%")
            save_to_file(results, '%s_titles/%s_%s.txt'%(cate, tag, str(page_nums * 20)))