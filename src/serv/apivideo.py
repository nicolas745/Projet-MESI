from serv.serv import serv , url
from sql.video import video
from flask import Flask, request
from flask import Flask, request, jsonify
class apivideo(serv):
    def __init__(self, app: Flask):
        super().__init__(app)
    @url("/api/video/list",['GET'])
    def listvideo(self):
        if('page' in request.args):
            return video().list_videos(10,request.args.get('page'))
        return video().list_videos(10,0)
    @url("/api/video", ['GET'])
    def video(self):
        return video().getinfo(request.args.get('id'))


app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    query = f"%{query}%"
    results = query_db("SELECT contenu_id, titre, description, image FROM contenu WHERE titre LIKE ? OR contenu_id IN (SELECT contenu_id FROM Auteur WHERE nom LIKE ?)", (query, query))
    
    movies = [
        {
            'id': row['contenu_id'],
            'title': row['titre'],
            'description': row['description'],
            'image': row['image']
        }
        for row in results
    ]
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True)
