from flask import Flask,request
from flask_restful import Api,Resource, abort,reqparse,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db =SQLAlchemy(app)


class VideoModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    views=db.Column(db.Integer,nullable=False)
    likes=db.Column(db.Integer,nullable=False)
    
    def __repr__(self):
        return f"Video(name={self.name},views={self.views},likes={self.likes})"

#db.create_all()

video_put_args=reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="Name of the Video is Required",required=True)
video_put_args.add_argument("likes",type=int,help="likes of the Video is Required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the Video is Required ",required=True)

video_update_args=reqparse.RequestParser()
video_update_args.add_argument("name",type=str,help="Name of the Video is Required")
video_update_args.add_argument("likes",type=int,help="likes of the Video is Required")
video_update_args.add_argument("views",type=int,help="Views of the Video is Required")


resource_fields={
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}
        
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result=VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message="Wrong Id Enter Again")
        return result
    
    @marshal_with(resource_fields)
    def post(self,video_id):
        args=video_put_args.parse_args()
        result=VideoModel.query.filter_by(id=video_id).first()
        if result:
             abort(409,message="Video id taken")
        Video=VideoModel(id=video_id,name=args['name'],views=args['views'],likes=args['likes'])
        db.session.add(Video)
        db.session.commit()
        return Video,201
    
    @marshal_with(resource_fields)
    def patch(self,video_id):
        args=video_update_args.parse_args()
        result=VideoModel.query.filter_by(id=video_id).first()
        if not result:
             abort(404,message="Cannot Update The Video Id")
        if args['name']:
            result.name=args['name']
        if args['views']:
            result.views=args['views']
        if args['likes']:
            result.likes=args['likes']
        
        db.session.commit()
        return result
    
    def delete(self,video_id):
        result=VideoModel.query.filter_by(id=video_id).first()
        if not result:
             abort(404,message="Id Does Not Exists")
        db.session.delete(result)
        db.session.commit
        return 204

class VideoGetAll(Resource):
      @marshal_with(resource_fields)
      def get(self,comment):
          result=VideoModel.query.all()
          return result
         
    
api.add_resource(Video,"/video/<int:video_id>")
api.add_resource(VideoGetAll,"/video/<string:comment>")

if __name__ == "__main__":
    app.run(debug=True)
