from pymongo import MongoClient

client = MongoClient("mongodb://mongorides:27017/")
db = client["ridesmicroservice"]

places = open("AreaNameEnum.csv", "r")
areas = places.read()
areas = areas.split('\n')
for i in range(len(areas)):
    areas[i] = areas[i].split(',')
areas.pop(0)
areas.pop(-1)

ip_port = '127.0.0.1:80'
rides_dns_name = "ec2-52-91-42-82.compute-1.amazonaws.com"
load_balancer = "CC-ass-3-531473334.us-east-1.elb.amazonaws.com"