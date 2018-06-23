import sys
import json
import scrapy 
from scrapy.http import Request
from forbes.items import ForbesItem


class ForbesSpider(scrapy.Spider):
  custom_settings = {
    'FEED_EXPORT_FIELDS' : ['position','name','lastName', 'age', 'country','gender', 'wealthSource', 'industry',
    'worth','worthChange', 'realTimeWorth', 'realTimePosition', 'image']
      
       }
  name= 'forbes'
 
  domain = 'https://www.forbes.com/'
  
  def __init__(self,year='2018',  *args, **kwargs):
    super(ForbesSpider, self).__init__(*args, **kwargs)
    self.year = year
    
  def start_requests(self):
    #https://www.forbes.com/ajax/list/data?year=2018&&uri=billionaires&type=person
    url = self.domain + 'ajax/list/data?year={}&&uri=billionaires&type=person'.format(self.year)
    yield Request(url, self.parse_products)
    
  def parse_products(self, response):
    #inspect_response(response, self)
    j_parser = json.loads(response.body)
    for person in j_parser :
      
      item = ForbesItem()
      age = None
      country = None
      gender = None
      wealth_source = None
      name = None
      last_name = None
      worth_change = None
      position = None
      worth = None
     
      if 'age' in person:
        age = person['age']
      wealth_source = person['source']
      if 'industry' in person :
        industry = person['industry']
      country = person['country']
      if 'gender' in person :
        gender = person['gender']
  
      name = person['name']
      last_name = person['lastName']
      if 'worthChange' in person :
        worth_change = person['worthChange']
 
      if 'squareImage' in person :
        image = 'https:' + person['squareImage']
      if 'position' in person :  
        position = person['position']
      
      if 'worth' in person : 
        worth = person['worth']
        
      if 'realTimeWorth' in person : 
        real_time_worth = person['realTimeWorth']
      if 'realTimePosition' in person :
        real_time_position = person['realTimePosition']
      
        
        
        
      item['age'] = age
      item['country'] = country
      item['image'] = image
      item['gender'] = gender
      item['wealthSource'] = wealth_source
      item['name'] = name
      item['lastName'] = last_name
      item['worthChange'] = worth_change
      item['industry'] = industry
      item['worth'] = worth
      item['realTimePosition'] = real_time_position
      item['position'] = position
      item['realTimeWealth'] = real_time_worth
      
      yield item
        
        
      
    
  
    