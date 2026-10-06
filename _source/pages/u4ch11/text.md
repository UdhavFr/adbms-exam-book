# 11. MongoDB CRUD

Source: ADBMS_MasterNotes.docx — folder `u4ch11`

### 11. MongoDB CRUD
_(p. 25)_
#### Create
_(p. 25)_
db.students.insertOne({name:'Ravi', age:22, course:'MCA'})
db.students.insertMany([{name:'Asha',age:23},{name:'John',age:21}])
#### Read
_(p. 25)_
db.students.find({age:{$gt:21}})
db.students.findOne({name:'Ravi'})
#### Update
_(p. 25)_
db.students.updateOne({name:'Ravi'}, {$set:{age:23}})
db.students.updateMany({course:'MCA'}, {$inc:{age:1}})
#### Delete
_(p. 25)_
db.students.deleteOne({name:'Ravi'})
db.students.deleteMany({course:'MCA'})
#### Common operators
_(p. 25)_
- Comparison: $gt, $gte, $lt, $lte, $eq, $ne
- Membership: $in, $nin
- Logical: $and, $or, $not, $nor
- Update: $set, $unset, $inc, $push, $pull
