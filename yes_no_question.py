#1.是不是...(呢)?
#國於是不是草包(呢)?
#2.是否..
#國魚是否為草包?
#3.是...嗎?
#國於是草包嗎?

import pandas as pd
data=pd.read_excel('FGC_1_week.xlsx',encoding='utf-8-sig')
data.columns
#data['QTEXT'][0]
#yes_no=data[data['QTEXT'].str.contains("是否")]
#yes_no=data[(data.correct_answer=='是')|(data.correct_answer=='否')]
#set1=set('是否嗎呢不')
#set(yes_no.iloc[0])&set1
def Yes_no(question):
    global set1
    set1=set('是否嗎')
    compare=len((set(question)&set1))/len(set1)
    
    if '是不是' in question or compare>=0.5:
        return '是是非題'
    else:
        return '不是是非題'
    

answer=[]
Yes_no('這個問題是不是為yes no 問題')  
Yes_no('若沒有從母姓，我的外甥女的姓氏和我是否一樣？')
Yes_no('若沒有從母姓，我的外甥女的姓氏和我是否一樣？')
Yes_no('4. 疾管署民眾應遵守「二不一要」，請問「二不」是什麼?')

answer=[]
for i in data['QTEXT']:
#    print(i)
    answer.append((Yes_no(i)))
data=pd.concat([data,pd.DataFrame(answer,columns=['判斷結果'])],axis=1)
