from flask import Flask,jsonify,request,render_template, abort
from scripts import find_by_id, find_by_title, find_by_year, _suggest

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


f = open('data.tsv', encoding='utf-8')

data = f.readlines()

f.close()



@app.route('/movie_id/<string:_id>', methods=['GET'])
def get_movie_by_id(_id):
    ans = find_by_id(_id, data)
    if (ans):
        return jsonify(find_by_id(_id, data))
    else:
        abort(404)



@app.route('/movie/<string:title>', methods=['GET'])
def get_movies_by_title(title):
    ans = find_by_title(title, data)

    if (len(ans)) == 0:
        abort(404)

    return jsonify(ans)



@app.route('/year/<int:year>' , methods=['GET'])
def get_movies_by_year(year):
  ans = find_by_year(year, data)
  
  if (len(ans)) == 0:
        abort(404)

  return jsonify(ans)




@app.route('/suggest/<int:topk>' , methods=['POST'])
def suggest(topk):

    if topk >= len(data) and topk <= 0:
        abort(404)

    ans = _suggest(topk, request.get_json(), data)
    sorted_dict = dict(sorted(ans.items(), key=lambda item: item[1], reverse=True))

    return jsonify({'ratings':sorted_dict})


app.run(debug=True, host='0.0.0.0', port=5000)