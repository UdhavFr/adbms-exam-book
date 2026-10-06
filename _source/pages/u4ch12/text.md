# 12. MongoDB Aggregation

Source: ADBMS_MasterNotes.docx — folder `u4ch12`

### 12. MongoDB Aggregation
_(p. 25)_
The aggregation framework processes documents through a sequence of stages called a pipeline. Each stage transforms, filters, groups, sorts, or joins data.
COLLECTION
   ↓
$match → filter
   ↓
$group → aggregate
   ↓
$project → shape fields
   ↓
$sort → order
   ↓
$limit → restrict
   ↓
RESULT
Example: db.sales.aggregate([{$match:{status:'paid'}}, {$group:{_id:'$product', total:{$sum:'$amount'}}}, {$sort:{total:-1}}])
This pipeline filters paid sales, groups them by product, calculates the total sales amount, and sorts the products by total in descending order.
- $match filters documents.
- $group groups documents and calculates aggregates.
- $project includes/excludes/computes fields.
- $sort orders documents.
- $limit restricts result count.
- $skip skips documents.
- $unwind expands array elements.
- $lookup performs a join-like lookup with another collection.
## UNIT 5 — NoSQL STORES, INDEXING AND ORDERING DATA SETS
_(p. 27)_
