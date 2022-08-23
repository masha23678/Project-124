{
    "data": [
        {
            "Contact": "9987644456"
            "Name": "Raju"
            "done" false
            "id": 1
        },
        {
            "Contact": "9876543222"
            "Name": "Rahul"
            "done" false
            "id": 2
        }
    ]
}




@app.route('/add-data',methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'Error',
            'message':"Please provide the data",
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    