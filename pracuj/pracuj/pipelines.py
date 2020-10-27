# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from psycopg2 import sql


class PracujPipeline:

    fields = tuple()
    val = tuple()
    def open_spider(self, spider):
        hostname = '192.168.0.16'
        username = 'role_pracuj_wr'
        password = ']Tu8U@!.!@2wfqe%'  # your password
        database = 'pracuj'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.execute(
            sql.SQL("insert into warszawa.IT({}) values({})").format(
                                                               sql.SQL(', ').join(map(sql.Identifier, self.fields)), sql.SQL(', ').join(map(int, self.val))))
        self.connection.commit()
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if item:
            self.fields = self.fields + (item['kat_mias'][0],)
            self.val = self.val + (item['liczba'][0],)
            return self.fields, self.val


#sql.Identifier(item['kat_mias'][1].lower().strip())
#sql.Identifier(item['kat_mias'][0])), item['liczba']