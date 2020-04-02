from requests_html import HTMLSession
from bs4 import BeautifulSoup

SESSION = HTMLSession()
URL = 'http://119.92.116.147/registrar'
URL_INFO = 'http://119.92.116.147/registrar/parts/dtsubject.php'
URL_SCHED = 'http://119.92.116.147/registrar/studentlist.php?schedcode=' # + sched code
    

PAGE = 1
START = '0'         # int(LENGTH) * (PAGE - 1)
LENGTH = '20'       # Can be 20, 25, 50, -1; CAN BE ANY NUMBER???????
KEYWORD = ''        # Search keywords
SCHED_CODE = ''


TABLE_HEADERS = ['Subject Code', 'Subject Title', 'Schedule Code', 'Section', 'Available Slots']

def new_cookie(Type='a'):
    get_url = SESSION.get(URL)
    new = get_url.cookies.values()

    if len(new) != 0:
        with open('cookies.txt', Type) as cookie_file:
            print(new[0], file=cookie_file)

    return new[0]

def get_cookie():
    cookie = ''

    try:    
        with open('cookies.txt', 'r') as cookie_file:
            lines = cookie_file.readlines()
            cookie = new_cookie() if len(lines) == 0 else lines[-1].strip()
    except FileNotFoundError:
        new_cookie('w')
        
    return cookie

cookies = {
    'PHPSESSID': get_cookie() # 'fflara9pp4h2bmk1bbbg93i1tv',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://119.92.116.147',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://119.92.116.147/registrar/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
    'draw': '1',
    'columns[0][data]': '0',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'true',
    'columns[0][search][value]': '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': '1',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'false',
    'columns[1][search][value]': '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': '2',
    'columns[2][name]': '',
    'columns[2][searchable]': 'true',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': '3',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'false',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': '4',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'true',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'order[0][column]': '0',
    'order[0][dir]': 'asc',
    'start': START,
    'length': LENGTH,
    'search[value]': KEYWORD,
    'search[regex]': 'false'
}

def get_response(L, K, S):
    L, K, S = [str(i) for i in (L, K, S)]
        
    D = data
    D['length'] = L
    D['search[value]'] = K
    D['start'] = S

    response = SESSION.post(URL_INFO,
##                            headers=headers,
                            cookies=cookies,
                            data=D,
                            verify=False)
    return response

def tag_parse_text(string):
    return BeautifulSoup(string, 'html.parser').get_text()

show_menu = True
while show_menu:
    Online = True
    if Online: 
        response = get_response(LENGTH, KEYWORD, START)
        json_dict = response.json()
    else:
        response_json = {'draw': 1, 'recordsTotal': 3904, 'recordsFiltered': 3904, 'data': [["<a href='studentlist.php?schedcode=201921773' target='_blank'>ABEN 22</a>", 'MATERIALS AND PROCESS FOR ABE', '201921773', 'BSABE2-1', '13'], ["<a href='studentlist.php?schedcode=201921781' target='_blank'>ABEN 22</a>", 'MATERIALS AND PROCESS FOR ABE', '201921781', 'BSABE2-2', '22'], ["<a href='studentlist.php?schedcode=201922171' target='_blank'>ACTG 1</a>", 'FUNDAMENTALS OF ACCOUNTING', '201922171', 'BSIT3-1', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201922180' target='_blank'>ACTG 1</a>", 'FUNDAMENTALS OF ACCOUNTING', '201922180', 'BSIT3-2', '13'], ["<a href='studentlist.php?schedcode=201922189' target='_blank'>ACTG 1</a>", 'FUNDAMENTALS OF ACCOUNTING', '201922189', 'BSIT3-3', '19'], ["<a href='studentlist.php?schedcode=201922302' target='_blank'>ACTG 101</a>", 'FINANCIAL ACCOUNTING', '201922302', 'BSIE1-1', '4'], ["<a href='studentlist.php?schedcode=201922311' target='_blank'>ACTG 101</a>", 'FINANCIAL ACCOUNTING', '201922311', 'BSIE1-2', '6'], ["<a href='studentlist.php?schedcode=201922320' target='_blank'>ACTG 102</a>", 'MANAGERIAL ACCOUNTING', '201922320', 'BSIE2-1', '3'], ["<a href='studentlist.php?schedcode=201922329' target='_blank'>ACTG 102</a>", 'MANAGERIAL ACCOUNTING', '201922329', 'BSIE2-2', '7'], ["<a href='studentlist.php?schedcode=201920906' target='_blank'>ACTG 200</a>", 'INTERNSHIP / ACCOUNTING THESIS', '201920906', 'BSACC5-1', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201920919' target='_blank'>ACTG 22</a>", 'PARTNERSHIP AND CORPORATION ACCOUNTING', '201920919', 'IRREG', '25'], ["<a href='studentlist.php?schedcode=201920255' target='_blank'>ACTG 23A</a>", 'CONCEPTUAL FRAMEWORK AND ACCOUNTING STANDARDS', '201920255', 'BSACC1-1', '3'], ["<a href='studentlist.php?schedcode=201920264' target='_blank'>ACTG 23A</a>", 'CONCEPTUAL FRAMEWORK AND ACCOUNTING STANDARDS', '201920264', 'BSACC1-2', '3'], ["<a href='studentlist.php?schedcode=201920273' target='_blank'>ACTG 23A</a>", 'CONCEPTUAL FRAMEWORK AND ACCOUNTING STANDARDS', '201920273', 'BSACC1-3', '1'], ["<a href='studentlist.php?schedcode=201920282' target='_blank'>ACTG 23A</a>", 'CONCEPTUAL FRAMEWORK AND ACCOUNTING STANDARDS', '201920282', 'BSACC1-4', '40'], ["<a href='studentlist.php?schedcode=201920257' target='_blank'>ACTG 24A</a>", 'INTERMEDIATE ACCOUNTING 1', '201920257', 'BSACC1-1', '2'], ["<a href='studentlist.php?schedcode=201920266' target='_blank'>ACTG 24A</a>", 'INTERMEDIATE ACCOUNTING 1', '201920266', 'BSACC1-2', '4'], ["<a href='studentlist.php?schedcode=201920275' target='_blank'>ACTG 24A</a>", 'INTERMEDIATE ACCOUNTING 1', '201920275', 'BSACC1-3', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201920284' target='_blank'>ACTG 24A</a>", 'INTERMEDIATE ACCOUNTING 1', '201920284', 'BSACC1-4', '40'], ["<a href='studentlist.php?schedcode=201920253' target='_blank'>ACTG 26A</a>", 'STRATEGIC COST MANAGEMENT', '201920253', 'BSACC1-1', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201920262' target='_blank'>ACTG 26A</a>", 'STRATEGIC COST MANAGEMENT', '201920262', 'BSACC1-2', '6'], ["<a href='studentlist.php?schedcode=201920271' target='_blank'>ACTG 26A</a>", 'STRATEGIC COST MANAGEMENT', '201920271', 'BSACC1-3', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201920280' target='_blank'>ACTG 26A</a>", 'STRATEGIC COST MANAGEMENT', '201920280', 'BSACC1-4', '40'], ["<a href='studentlist.php?schedcode=201920291' target='_blank'>ACTG 27A</a>", 'INTERMEDIATE ACCOUNTING 3', '201920291', 'BSACC2-1', '4'], ["<a href='studentlist.php?schedcode=201920300' target='_blank'>ACTG 27A</a>", 'INTERMEDIATE ACCOUNTING 3', '201920300', 'BSACC2-2', '3'], ["<a href='studentlist.php?schedcode=201920309' target='_blank'>ACTG 27A</a>", 'INTERMEDIATE ACCOUNTING 3', '201920309', 'BSACC2-3', '40'], ["<a href='studentlist.php?schedcode=201920292' target='_blank'>ACTG 28A</a>", 'GOVERNANCE, BUSINESS ETHICS, RISK MANAGEMENT AND INTERNAL CONTROL', '201920292', 'BSACC2-1', '2'], ["<a href='studentlist.php?schedcode=201920301' target='_blank'>ACTG 28A</a>", 'GOVERNANCE, BUSINESS ETHICS, RISK MANAGEMENT AND INTERNAL CONTROL', '201920301', 'BSACC2-2', '3'], ["<a href='studentlist.php?schedcode=201920310' target='_blank'>ACTG 28A</a>", 'GOVERNANCE, BUSINESS ETHICS, RISK MANAGEMENT AND INTERNAL CONTROL', '201920310', 'BSACC2-3', '40'], ["<a href='studentlist.php?schedcode=201920315' target='_blank'>ACTG 30</a>", 'MANAGEMENT ACCOUNTING, PART 1', '201920315', 'BSACC4-1', '27'], ["<a href='studentlist.php?schedcode=201920316' target='_blank'>ACTG 31</a>", 'MANAGEMENT ACCOUNTING, PART 2', '201920316', 'BSACC4-1', '27'], ["<a href='studentlist.php?schedcode=201920317' target='_blank'>ACTG 33</a>", 'ADVANCED FINANCIAL ACCOUNTING AND REPORTING, PART 1', '201920317', 'BSACC4-1', '27'], ["<a href='studentlist.php?schedcode=201920319' target='_blank'>ACTG 34</a>", 'ADVANCED FINANCIAL ACCOUNTING AND REPORTING, PART 2', '201920319', 'BSACC4-1', '27'], ["<a href='studentlist.php?schedcode=201920320' target='_blank'>ACTG 99</a>", 'ACCOUNTING SYNTHESIS', '201920320', 'BSACC5-1', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201920321' target='_blank'>ACTG REVIEW</a>", 'ACCOUNTING REVIEW', '201920321', 'BSACC5-1', "<font color='#ff0000'>0</font>"], ["<a href='studentlist.php?schedcode=201922338' target='_blank'>ACTG23</a>", 'FINANCIAL ACCOUNTING', '201922338', 'BSIE3-1', '34'], ["<a href='studentlist.php?schedcode=201923831' target='_blank'>AEAP 50</a>", 'SWINE PRODUCTION ENTERPRISE', '201923831', 'BAE-IRREG', '37'], ["<a href='studentlist.php?schedcode=201923833' target='_blank'>AEAP 90</a>", 'SPECIAL TOPICS', '201923833', 'BAE-IRREG', '39'], ["<a href='studentlist.php?schedcode=201923832' target='_blank'>AEAP 99</a>", 'SEMINAR', '201923832', 'BAE-IRREG', '22'], ["<a href='studentlist.php?schedcode=201920721' target='_blank'>AECO 200</a>", 'UNDERGRADUATE THESIS / FARM PRACTICE', '201920721', 'BSECON3-AE', '34'], ["<a href='studentlist.php?schedcode=201920736' target='_blank'>AECO 200A</a>", 'UNDERGRADUATE THESIS', '201920736', 'BSECON4-AE', '35'], ["<a href='studentlist.php?schedcode=201920716' target='_blank'>AECO 55</a>", 'AGRICULTURAL BUSINESS ACCOUNTING', '201920716', 'BSECON3-AE', '32'], ["<a href='studentlist.php?schedcode=201920717' target='_blank'>AECO 60</a>", 'RESEARCH METHODS AND TECHNIQUES IN AGRICULTURAL ECONOMICS', '201920717', 'BSECON3-AE', '34'], ["<a href='studentlist.php?schedcode=201920718' target='_blank'>AECO 65</a>", 'PROJECT ANALYSIS AND EVALUATION', '201920718', 'BSECON3-AE', '32'], ["<a href='studentlist.php?schedcode=201920719' target='_blank'>AECO 75</a>", 'AGRICULTURAL FINANCE', '201920719', 'BSECON3-AE', '32'], ["<a href='studentlist.php?schedcode=201920720' target='_blank'>AECO 85</a>", 'AGRICULTURAL PRODUCTION ECONOMICS', '201920720', 'BSECON3-AE', '32'], ["<a href='studentlist.php?schedcode=201923747' target='_blank'>AECP199B</a>", 'OCCUPATIONAL INTERNSHIP', '201923747', 'BAE4-1AP', '18'], ["<a href='studentlist.php?schedcode=201923748' target='_blank'>AECP199B</a>", 'OCCUPATIONAL INTERNSHIP', '201923748', 'BAE4-1CP', '15'], ["<a href='studentlist.php?schedcode=201923698' target='_blank'>AENG 11</a>", 'FUNDAMENTAL OF AGRICULTURAL ENGINEERING', '201923698', 'BSA3-1', '35'], ["<a href='studentlist.php?schedcode=201923707' target='_blank'>AENG 11</a>", 'FUNDAMENTAL OF AGRICULTURAL ENGINEERING', '201923707', 'BSA3-2', '32'], ["<a href='studentlist.php?schedcode=201921788' target='_blank'>AENG 120</a>", 'TRACTOR & AGRICULTURAL EQUIPMENT OPERATION', '201921788', 'BSAE5-1', '16'], ["<a href='studentlist.php?schedcode=201921787' target='_blank'>AENG 125</a>", 'FOREST PRODUCTS ENGINEERING', '201921787', 'BSAE5-1', '24'], ["<a href='studentlist.php?schedcode=201921786' target='_blank'>AENG 130</a>", 'AQUACULTURE ENGINEERING', '201921786', 'BSAE5-1', '22'], ["<a href='studentlist.php?schedcode=201921785' target='_blank'>AENG 135</a>", 'AGRICULTURAL WASTE MANAGEMENT', '201921785', 'BSAE5-1', '19'], ["<a href='studentlist.php?schedcode=201921789' target='_blank'>AENG 140</a>", "AGRICULTURAL ENG'G LAW AND PROFESSIONAL ETHICS", '201921789', 'BSAE5-1', '22'], ["<a href='studentlist.php?schedcode=201921790' target='_blank'>AENG 198</a>", 'A E   COMPETENCY APPRAISAL 3', '201921790', 'BSAE5-1', '16'], ["<a href='studentlist.php?schedcode=201921791' target='_blank'>AENG 200</a>", 'UNDERGRADUATE THESIS', '201921791', 'BSAE5-1', '22'], ["<a href='studentlist.php?schedcode=201922636' target='_blank'>AENG 24</a>", 'ENVIRONMENTAL SCIENCE', '201922636', 'BSAE4-IRREG', '39'], ["<a href='studentlist.php?schedcode=201922625' target='_blank'>AENG 24A</a>", 'ENVIRONMENTAL ENGINEERING', '201922625', 'IRREG', '39'], ["<a href='studentlist.php?schedcode=201922493' target='_blank'>AENG 26</a>", 'ENVIRONMENTAL ENGINEERING', '201922493', 'BIT-AT4-1', '21'], ["<a href='studentlist.php?schedcode=201922499' target='_blank'>AENG 26</a>", 'ENVIRONMENTAL ENGINEERING', '201922499', 'BIT-AT4-2', '15'], ["<a href='studentlist.php?schedcode=201922554' target='_blank'>AENG 26</a>", 'ENVIRONMENTAL ENGINEERING', '201922554', 'BIT-ELEC4-1', '2'], ["<a href='studentlist.php?schedcode=201922597' target='_blank'>AENG 26</a>", 'ENVIRONMENTAL ENGINEERING', '201922597', 'BIT-ELEX4-1', '26'], ["<a href='studentlist.php?schedcode=201922627' target='_blank'>AENG 27</a>", 'METHODS OF RESEARCH WITH EXPERIMENTAL DESIGN', '201922627', 'IRREG', '39'], ["<a href='studentlist.php?schedcode=201922637' target='_blank'>AENG 70A</a>", 'ARGICULTURAL POWER AND ENERGY RESOURCE', '201922637', 'BSAE4-IRREG', '39'], ["<a href='studentlist.php?schedcode=201922628' target='_blank'>AENG115</a>", 'DESIGN AND MGT. OF AGRICULTURAL BUILDINGS', '201922628', 'IRREG', '32'], ["<a href='studentlist.php?schedcode=201922643' target='_blank'>AENG196</a>", 'A E   COMPETENCY APPRAISAL 1', '201922643', 'BSAE4-IRREG', '38'], ["<a href='studentlist.php?schedcode=201922638' target='_blank'>AENG75</a>", 'REFRIGERATION ENGINEERING', '201922638', 'BSAE4-IRREG', '39'], ["<a href='studentlist.php?schedcode=201922639' target='_blank'>AENG80</a>", 'AGRICULTURAL STRUCTURES ENGINEERING', '201922639', 'BSAE4-IRREG', '37'], ["<a href='studentlist.php?schedcode=201822640' target='_blank'>AENG85</a>", 'AGRICULTURAL MACHINERY DESIGN', '201822640', '0', '40'], ["<a href='studentlist.php?schedcode=201922640' target='_blank'>AENG85</a>", 'AGRICULTURAL MACHINERY DESIGN', '201922640', 'BSAE4-IRREG', '37'], ["<a href='studentlist.php?schedcode=201922641' target='_blank'>AENG90</a>", 'IRRIGATION AND DRAINAGE ENGINEERING', '201922641', 'BSAE4-IRREG', '38'], ["<a href='studentlist.php?schedcode=201922642' target='_blank'>AENG95</a>", 'PROCESSING, HANDLING, STORAGE OF AGRICULTURAL PRODUCTS 1', '201922642', 'BSAE4-IRREG', '34'], ["<a href='studentlist.php?schedcode=201928728' target='_blank'>AG EXT 230</a>", 'SOCIOLOGY OF DEVELOPMENT', '201928728', 'MSAG EXT', '34'], ["<a href='studentlist.php?schedcode=201928729' target='_blank'>AG EXT 235</a>", 'PROBLEMS OF RURAL DEVELOPMENT', '201928729', 'MSAG EXT', '34']]}
        json_dict = response_json
    
    json_data = json_dict['data']

    print('{:<15.15} {:<23.20} {:<15.15} {:<10.10} {:<15.15}'.format(*TABLE_HEADERS))
    for data_row in json_data:
        data_row = [tag_parse_text(d) for d in data_row]

        print('{:<15.15} {:<23.20} {:<15.15} {:<10.10} {:<15.15}'.format(*data_row))

    print('', 'MENU LOLOLOLOL [If no data, try to refresh cookies]',
          f'Number of rows to display: {LENGTH}',
          f'Searching for the keywords: {KEYWORD}',
          '[1] Next page',
          '[2] Previous page',
          '[3] Change number of displayed rows',
          '[4] Search for a keyword',
          '[5] Search for a schedule code',
          '[6] Refresh cookies',
          '[0] End program', sep='\n')

    selection = input('Please make a selection: '); print()
    if selection.isdigit(): selection = int(selection)

    if selection == 1:
        PAGE += 1
        START = int(START) + int(LENGTH)

    elif selection == 2:
        if PAGE == 1:
            print('This is the start of the entries!')
        else:
            PAGE -= 1
            START = int(START) - int(LENGTH)

    elif selection == 3:
        user = input('Enter number of rows desired: ')
        if user.isdigit(): LENGTH = int(user)

    elif selection == 4:
        KEYWORD = input('Enter keyword(s) to search for: ')
        PAGE = 1
        START = 0

    elif selection == 5:
##        print('To implement!')
        
        SCHEDULE_CODE = input('Enter schedule code: ')

        RESPONSE = SESSION.get(URL_SCHED + SCHEDULE_CODE)
        SOUP = BeautifulSoup(RESPONSE.html.html, 'html.parser')

        valid_code = True
        class_info = SOUP.find_all('div', {'class':'profile-info-row'})
        information = [info.get_text().strip().split('\n') for info in class_info]
        for i in information:
            if i[0] == 'Section' and len(i) == 1:
                valid_code = False

        if not valid_code:
            print('There was a problem in getting information from given schedule code.')
        else:
            print('CLASS INFORMATION')
            class_info = SOUP.find_all('div', {'class':'profile-info-row'})
            for info in class_info:
                info_text = info.get_text().strip().split('\n')

                if info_text[0] == 'Note ': continue

                print('{:<20} {}'.format(*info_text))
            print()

            print('STUDENT LIST')
            row_list = SOUP.find_all('tr')
            for row in row_list:
                row_data = row.get_text().strip().split('\n')

                print('{:<3.3} {:<30.30} {:<16.16} {:<8.8} {:<8.8} {:<10.10}'.format(*row_data))

    elif selection == 6:
        print('Trying to fetch new cookies. . .')
        new_cookie()

    elif selection == 0:
        print('Thank you very much!')
        show_menu = False

    else:
        print('You have made an invalid selection!')


    if selection not in (0, 1, 2): input('\nPress Enter to continue. . .'); print()

      





