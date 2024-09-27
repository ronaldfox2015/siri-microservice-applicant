from app.domain.entities.post import Post
from app.domain.repositories.post_repository import PostRepository
from app.infrastructure.db.models import PostModel, db


class PostRepositoryImpl(PostRepository):
    def get_by_id(self, post_id: int) -> Post:
        post_model = PostModel.query.get(post_id)
        if post_model:
            return Post(id=post_model.id, title=post_model.title, content=post_model.content, user_id=post_model.user_id)
        return None

    def add(self, post: Post) -> None:
        new_post = PostModel(title=post.title, content=post.content, user_id=post.user_id)
        db.session.add(new_post)
        db.session.commit()
        post.id = new_post.id
