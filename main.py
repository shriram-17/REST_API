from flask import Flask,request
from flask_restful import Api,Resource,reqparse

app=Flask(__name__)
api=Api(app)

video_put_args=reqparse.RequestParser()

video_put_args.add_argument("name",type=str,help="Name of the Video is Required",required=True)
video_put_args.add_argument("likes",type=int,help="likes of the Video is Required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the Video is Required ",required=True)

videos={}

class Video(Resource):
    def get(self,video_id):
        return videos[video_id]
    def post(self,video_id):
        args=video_put_args.parse_args()
        return {video_id:args}
 
api.add_resource(Video,"/video/<int:video_id>")
  
if __name__ == "__main__":
    app.run(debug=True)
