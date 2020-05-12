import pymysql

def data_wash(list):
        list[2] = str(list[2])[:-2]
        list[3] = str(list[3][2:-3])
        list[7] = list[7].replace('.','-')
        return(list)

def to_mysql(data_list):

    data_list = data_wash(data_list)
    
    conn = pymysql.connect(host='localhost', port=3306,
                           database='house_price', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute(
                                    'insert into tb_sold_house values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',data_list
                                    )

        if result == 1:
            print('添加成功！')

        conn.commit()
    except Exception as e:
        print(e)
        print('入库异常，跳过该记录...')

    
    finally:
        conn.close()
def main():
    data_list = ['知春路57号院', '662', '76.5平米', '单价86536元/平', '2室1厅', '南 北', '2019-12-25', '2020.01.22', 'https://bj.lianjia.com/chengjiao/101106617894.html', '101106617895']
    to_mysql(data_list)

if __name__ == '__main__':
    main()