from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.epsmx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 저장 - 예시
doc = {'name':'bobby','age':21}
#  저장하고 싶은 곳
db.users.insert_one(doc)

# 한 개 찾기 - 예시
#                           조건문
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
#                    조건문 없음 => 전부찾기
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
#                       조건문             이걸로 바꿔줘
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
#                           조건문
db.users.delete_one({'name':'bobby'})